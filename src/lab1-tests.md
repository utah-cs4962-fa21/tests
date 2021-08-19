Tests for WBE Chapter 1
=======================

Chapter 1 (Downloading Web Pages) covers parsing URLs, HTTP requests
and responses, and a very very simplistic print function that writes
to the screen. This file contains tests for those components.

Here's the testing boilerplate.

    >>> import time
    >>> import test
    >>> _ = test.socket.patch().start()
    >>> _ = test.ssl.patch().start()
    >>> import web_browser
    

Testing `show`
--------------

The `show` function is supposed to print some HTML to the screen, but
skip the tags inside.

    >>> web_browser.show('<body>hello</body>')
    hello
    >>> web_browser.show('<body><wbr>hello</body>')
    hello
    >>> web_browser.show('<body>he<wbr>llo</body>')
    hello
    >>> web_browser.show('<body>hel<div>l</div>o</body>')
    hello

Note that the tags do not have to match:

    >>> web_browser.show('<body><p>hel</div>lo</body>')
    hello
    >>> web_browser.show('<body>h<p>el<div>l</p>o</div></body>')
    hello
    
Newlines should not be removed:

    >>> web_browser.show('<body>hello\nworld</body>')
    hello
    world

Testing `request`
-----------------

The `request` function makes HTTP requests.

To test it, we use the `test.socket` object, which mocks the HTTP server:

    >>> url = 'http://test.test/example1'
    >>> test.socket.respond(url, b"HTTP/1.0 200 OK\r\n" +
    ... b"Header1: Value1\r\n\r\n" +
    ... b"Body text")

Then we request the URL and test both request and response:

    >>> headers, body = web_browser.request(url)
    >>> lr = test.socket.last_request(url)
    >>> b'GET /example1 HTTP/1.0\r\n' in lr or b'GET /example1 HTTP/1.1\r\n' in lr
    True
    >>> b'Host: test.test\r\n' in lr
    True
    >>> lr.endswith(b'\r\n\r\n')
    True
    >>> body
    'Body text'
    >>> headers
    {'header1': 'Value1'}

Testing SSL support
-------------------

Here we're making sure that SSL support is enabled.

    >>> url = 'https://test.test/example2'
    >>> test.socket.respond(url, b"HTTP/1.0 200 OK\r\n\r\n")
    >>> header, body = web_browser.request(url)
    >>> body
    ''

SSL support also means some support for ports:

    >>> url = 'https://test.test:400/example3'
    >>> test.socket.respond(url, b"HTTP/1.0 200 OK\r\n\r\nHi")
    >>> header, body = web_browser.request(url)
    >>> body
    'Hi'

Requesting the wrong port is an error:

    >>> test.errors(web_browser.request, "http://test.test:401/example3")
    True


Testing Exercise `HTTP/1.1`
---------------------------

Reuse the response from earlier
    
    >>> b'Connection: close' in lr
    True
    >>> b'User-Agent: ' in lr
    True
    >>> b'GET /example1 HTTP/1.1\r\n' in lr
    True
    
Make a new request with an extra header

    >>> headers, body = web_browser.request(url, headers={"ClientHeader": "42"})
    >>> lr = test.socket.last_request(url)
    >>> b'ClientHeader: 42' in lr
    True


Testing Exercise `Redirects`
----------------------------

Test a simple redirect with a full path

    >>> url = 'http://test.test/redirect1'
    >>> redirect_target1 = 'http://test.redirect_test/target1'
    >>> test.socket.respond(url, b"HTTP/1.0 301 Moved Permanently\r\n" +
    ... "Location: {}\r\n\r\n".format(redirect_target1).encode())
    >>> test.socket.respond(redirect_target1, b"HTTP/1.0 200 Ok\r\n\r\n" +
    ... b"You found me")
    >>> headers, body = web_browser.request(url)
    >>> body
    'You found me'
    
Now a simple redirect without an explicit host

    >>> url = 'http://test.test/redirect2'
    >>> redirect_target2 = 'http://test.test/target2'
    >>> test.socket.respond(url, b"HTTP/1.0 301 Moved Permanently\r\n" +
    ... b"Location: /target2\r\n\r\n")
    >>> test.socket.respond(redirect_target2, b"HTTP/1.0 200 Ok\r\n\r\n" +
    ... b"You found me again")
    >>> headers, body = web_browser.request(url)
    >>> body
    'You found me again'
    
Now a multiple redirect

    >>> url = 'http://test.test/redirect3'
    >>> redirect_target3 = 'http://test.test/target3'
    >>> redirect_target4 = 'http://test.redirect_test/target4'
    >>> test.socket.respond(url, b"HTTP/1.0 301 Moved Permanently\r\n" +
    ... "Location: {}\r\n\r\n".format(redirect_target3).encode())
    >>> test.socket.respond(redirect_target3, b"HTTP/1.0 301 Moved Permanently\r\n" +
    ... "Location: {}\r\n\r\n".format(redirect_target4).encode())
    >>> test.socket.respond(redirect_target4, b"HTTP/1.0 200 Ok\r\n\r\n" +
    ... b"I need to hide better")    
    >>> headers, body = web_browser.request(url)
    >>> body
    'I need to hide better'
    
A self redirect loop should lead to an error

    >>> url = 'http://test.test/redirect4'
    >>> test.socket.respond(url, b"HTTP/1.0 301 Moved Permanently\r\n" +
    ... "Location: {}\r\n\r\n".format(url).encode())
    >>> try:
    ...     header, body = web_browser.request(url)
    ... except AssertionError:
    ...     print("Loop caught")
    Loop caught

A two stage loop to make sure infinite redirects aren't just caught by
looking for a direct self loop

    >>> url = 'http://test.test/redirect5'
    >>> redirect_target5 = 'http://test.test/target5'
    >>> test.socket.respond(url, b"HTTP/1.0 301 Moved Permanently\r\n" +
    ... "Location: {}\r\n\r\n".format(redirect_target5).encode())
    >>> test.socket.respond(redirect_target5, b"HTTP/1.0 301 Moved Permanently\r\n" +
    ... "Location: {}\r\n\r\n".format(url).encode())
    >>> try:
    ...     header, body = web_browser.request(url)
    ... except AssertionError:
    ...     print("Loop caught")
    Loop caught

A non 3XX status code with a location header to test that the status code is 
being checked, not just the location header

    >>> url = 'http://test.test/not_redirect'
    >>> do_not_follow = 'http://test.test/not_target'
    >>> test.socket.respond(url, b"HTTP/1.0 500 Internal Server Error\r\n" +
    ... "Location: {}\r\n\r\n".format(do_not_follow).encode() +
    ... b"Stay here")
    >>> test.socket.respond(do_not_follow, b"HTTP/1.0 200 Ok\r\n\r\n" +
    ... b"Too far")
    >>> header, body = web_browser.request(url)
    >>> body
    'Stay here'


Testing Exercise `Caching`
----------------------------

Test that a respsone is cached by changing the response

    >>> url = "http://test.test/cache_me1"
    >>> test.socket.respond(url, b"HTTP/1.0 200 Ok\r\n" +
    ... b"Cache-Control: max-age=9001\r\n\r\n" +
    ... b"Keep this for a while")
    >>> header, body = web_browser.request(url)
    >>> test.socket.respond(url, b"HTTP/1.0 200 Ok\r\n" +
    ... b"Cache-Control: max-age=9001\r\n\r\n" +
    ... b"Don't even ask for this")
    >>> header, body = web_browser.request(url)
    >>> body
    'Keep this for a while'

Make sure not everything is cached

    >>> url = "http://test.test/do_not_cache_me"
    >>> test.socket.respond(url, b"HTTP/1.0 200 Ok\r\n" +
    ... b"Cache-Control: no-store\r\n\r\n" +
    ... b"Don't cache me")
    >>> header, body = web_browser.request(url)
    >>> test.socket.respond(url, b"HTTP/1.0 200 Ok\r\n" +
    ... b"Cache-Control: no-store\r\n\r\n" +
    ... b"Ask for this")
    >>> header, body = web_browser.request(url)
    >>> body
    'Ask for this'
    
The cache should hold more than one thing

    >>> url = "http://test.test/cache_me2"
    >>> test.socket.respond(url, b"HTTP/1.0 200 Ok\r\n" +
    ... b"Cache-Control: max-age=9001\r\n\r\n" +
    ... b"Keep this for a while, also")
    >>> header, body = web_browser.request(url)
    >>> test.socket.respond(url, b"HTTP/1.0 200 Ok\r\n" +
    ... b"Cache-Control: max-age=9001\r\n\r\n" +
    ... b"Don't even ask for this")
    >>> header, body = web_browser.request(url)
    >>> body
    'Keep this for a while, also'
    >>> header, body = web_browser.request("http://test.test/cache_me1")
    >>> body
    'Keep this for a while'
    
A cache entry can be invalidated by time elapsing

    >>> url = "http://test.test/cache_me3"
    >>> test.socket.respond(url, b"HTTP/1.0 200 Ok\r\n" +
    ... b"Cache-Control: max-age=1\r\n\r\n" +
    ... b"Keep this for a short while")
    >>> header, body = web_browser.request(url)
    >>> test.socket.respond(url, b"HTTP/1.0 200 Ok\r\n" +
    ... b"Cache-Control: max-age=9001\r\n\r\n" +
    ... b"Don't ask for this immediately")
    >>> header, body = web_browser.request(url)
    >>> body
    'Keep this for a short while'
    >>> time.sleep(2)
    >>> header, body = web_browser.request(url)
    >>> body
    "Don't ask for this immediately"

The other entries should reamin

    >>> header, body = web_browser.request("http://test.test/cache_me1")
    >>> body
    'Keep this for a while'
