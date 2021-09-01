Tests for WBE Chapter 2 Exercise `Zoom`
==============================================

Testing boilerplate:

    >>> import test
    >>> _ = test.socket.patch().start()
    >>> _ = test.ssl.patch().start()
    >>> import browser

Testing `resize`
------------------

To allow testing of your zoom functionality make sure to name the 
  method which handles the event for the `-` and `+` keys `zoomout` and `zoomout`, respectively.

First setup the environment used in the base tests for testing `scrolldown`

Let's override text spacing and line width to make it easy to do math
when testing:

    >>> browser.WIDTH = 1
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
    ...             "0123456789").encode())

Loading that URL results in a display list:

    >>> this_browser = browser.Browser()
    >>> this_browser.load(url)
    create_text: x=1 y=2 text=0 font=(None, 20) anchor=None
    create_text: x=1 y=4 text=1 font=(None, 20) anchor=None
    create_text: x=1 y=6 text=2 font=(None, 20) anchor=None
    create_text: x=1 y=8 text=3 font=(None, 20) anchor=None
    create_text: x=1 y=10 text=4 font=(None, 20) anchor=None
    create_text: x=1 y=12 text=5 font=(None, 20) anchor=None
    create_text: x=1 y=14 text=6 font=(None, 20) anchor=None
    create_text: x=1 y=16 text=7 font=(None, 20) anchor=None
    create_text: x=1 y=18 text=8 font=(None, 20) anchor=None
    create_text: x=1 y=20 text=9 font=(None, 20) anchor=None
    >>> 

TODO: What type of font should we have the students use?

Like above you can simply do `(<fontname>[, <size>[, <effect]]>)`
There is also the mocked `tkinter.font.Font`
