Tests for WBE Chapter 2 Exercise `Zoom`
==============================================

Testing boilerplate:

    >>> import test
    >>> _ = test.socket.patch().start()
    >>> _ = test.ssl.patch().start()
    >>> _ = test.patch_canvas()
    >>> import browser

Testing `resize`
------------------

To allow testing of your zoom functionality make sure to name the
  method which handles the event for the `-` and `+` keys `zoomout` and `zoomout`, respectively.

Reset text spacing and line width in case this is ran in series with the other
tests.

    >>> browser.WIDTH = 800
    >>> browser.HEIGHT = 600
    >>> browser.HSTEP = 13
    >>> browser.VSTEP = 18

Let's mock a URL to load:

    >>> url = 'http://test.test/example1'
    >>> test.socket.respond_200(url=url,
    ...   body="ab")

Loading that URL results in a display list:

    >>> this_browser = browser.Browser()
    >>> this_browser.load(url)
    create_text: x=13 y=18 text=a font=Font size=12 weight=None slant=None style=None anchor=None
    create_text: x=26 y=18 text=b font=Font size=12 weight=None slant=None style=None anchor=None

Calling `zoomout` should make the font size 11, and move the b slightly to the
  left.

    >>> this_browser.zoomout({})
    create_text: x=12 y=16 text=a font=Font size=11 weight=None slant=None style=None anchor=None
    create_text: x=24 y=16 text=b font=Font size=11 weight=None slant=None style=None anchor=None

Calling `zoomin` should restore the default output.

    >>> this_browser.zoomin({})
    create_text: x=13 y=18 text=a font=Font size=12 weight=None slant=None style=None anchor=None
    create_text: x=26 y=18 text=b font=Font size=12 weight=None slant=None style=None anchor=None

Calling `zoomin` again should make the font size 13, and move b slightly to the
  right.

    >>> this_browser.zoomin({})
    create_text: x=14 y=19 text=a font=Font size=13 weight=None slant=None style=None anchor=None
    create_text: x=28 y=19 text=b font=Font size=13 weight=None slant=None style=None anchor=None


Scrolling while zoomed
---------------------

Change the line width and scroll step

    >>> browser.WIDTH = 39
    >>> browser.SCROLL_STEP = 38

Let's mock a URL and load it:

    >>> url = 'http://test.test/example2'
    >>> test.socket.respond_200(url=url,
    ...   body="abcd")
    >>> this_browser.load(url)
    create_text: x=14 y=19 text=a font=Font size=13 weight=None slant=None style=None anchor=None
    create_text: x=14 y=38 text=b font=Font size=13 weight=None slant=None style=None anchor=None
    create_text: x=14 y=57 text=c font=Font size=13 weight=None slant=None style=None anchor=None
    create_text: x=14 y=76 text=d font=Font size=13 weight=None slant=None style=None anchor=None

Scroll down

    >>> this_browser.scrolldown({})
    create_text: x=14 y=-19 text=a font=Font size=13 weight=None slant=None style=None anchor=None
    create_text: x=14 y=0 text=b font=Font size=13 weight=None slant=None style=None anchor=None
    create_text: x=14 y=19 text=c font=Font size=13 weight=None slant=None style=None anchor=None
    create_text: x=14 y=38 text=d font=Font size=13 weight=None slant=None style=None anchor=None

Again

    >>> this_browser.scrolldown({})
    create_text: x=14 y=-19 text=c font=Font size=13 weight=None slant=None style=None anchor=None
    create_text: x=14 y=0 text=d font=Font size=13 weight=None slant=None style=None anchor=None

This relies on having finished the `Mouse Wheel` exercise

    >>> this_browser.scrollup({})
    create_text: x=14 y=-19 text=a font=Font size=13 weight=None slant=None style=None anchor=None
    create_text: x=14 y=0 text=b font=Font size=13 weight=None slant=None style=None anchor=None
    create_text: x=14 y=19 text=c font=Font size=13 weight=None slant=None style=None anchor=None
    create_text: x=14 y=38 text=d font=Font size=13 weight=None slant=None style=None anchor=None
