Tests for WBE Chapter 8 Exercise `Enter key`
============================================

Description
-----------

In most browsers, if you hit the “Enter” or “Return” key while inside a text
  entry, that submits the form that the text entry was in.
Add this feature to your browser.


Test code
---------

Boilerplate.

    >>> import test
    >>> _ = test.socket.patch().start()
    >>> _ = test.ssl.patch().start()
    >>> import browser

This is the response to the expected POST request.

    >>> url = 'http://test.test/chapter8-enter/submit'
    >>> request_body = "name=Killroy&comment=2%3D3"
    >>> test.socket.respond(url, b"HTTP/1.0 200 OK\r\n\r\n" +
    ... b"<div>Form submitted</div>", method="POST", body=request_body)

This is the form page.

    >>> url = 'http://test.test/chapter8-enter/example'
    >>> body = ("<form action=\"/chapter8-enter/submit\" method=\"POST\">" +
    ...         "  <p>Name: <input name=name value=1></p>" +
    ...         "  <p>Comment: <input name=comment value=\"2=3\"></p>" +
    ...         "  <p><button>Submit!</button></p>" +
    ...         "</form>")
    >>> test.socket.respond_200(url, body)
    >>> this_browser = browser.Browser()
    >>> this_browser.load(url)

Clicking on the input should clear its content at set focus

    >>> this_browser.handle_click(test.Event(90, 25 + browser.CHROME_PX))
    >>> this_browser.focus
    'content'
    >>> this_browser.tabs[0].focus
    <input name="name" value="">

Type in a response then press enter to perform the POST request.
This will be matched against the earlier description.

    >>> for c in "Killroy":
    ...   this_browser.handle_key(test.key_event(c))
    >>> this_browser.handle_enter(test.enter_event())

This is what the raw request should be.

    >>> test.socket.last_request('http://test.test/chapter8-enter/submit')
    b'POST /chapter8-enter/submit HTTP/1.0\r\nContent-Length: 26\r\nHost: test.test\r\n\r\nname=Killroy&comment=2%3D3'


