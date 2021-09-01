Tests for WBE Chapter 2 Exercise `Line Breaks`
==============================================

Testing boilerplate:

    >>> import test
    >>> _ = test.socket.patch().start()
    >>> _ = test.ssl.patch().start()
    >>> import browser

Testing `resize`
------------------

First setup the environment used in the base tests for testing `scrolldown`

Let's override text spacing and line width to make it easy to do math
when testing:

    >>> browser.WIDTH = 10
    >>> browser.HSTEP = 1
    >>> browser.VSTEP = 2

Let's install a mock canvas that prints out the x and y coordinates, plus
the text drawn:

    >>> test.patch_canvas()
    >>> this_browser = browser.Browser()

Let's mock a URL to load:

    >>> url = 'http://test.test/example1'
    >>> test.socket.respond(url=url,
    ...   response=("HTTP/1.0 200 OK\r\n" +
    ...             "Header1: Value1\r\n"
    ...             "\r\n" +
    ...             "u\r\n" +
    ...             "d").encode())

Loading that URL results in a display list:

    >>> this_browser = browser.Browser()
    >>> this_browser.load(url)
    create_text: x=1 y=2 text=u...
    create_text: x=2 y=2 text=d...
