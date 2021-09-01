Tests for WBE Chapter 2 Exercise `Mouse Wheel`
==============================================

Testing boilerplate:

    >>> import test
    >>> _ = test.socket.patch().start()
    >>> _ = test.ssl.patch().start()
    >>> _ = test.patch_canvas()
    >>> import browser

Testing `scrollup`
------------------

Let's override text spacing and line width to make it easy to do math
when testing:

    >>> browser.WIDTH = 1
    >>> browser.HSTEP = 1
    >>> browser.VSTEP = 2

Let's mock a URL to load:

    >>> url = 'http://test.test/example1'
    >>> test.socket.respond_200(url=url,
    ...   body="abcd")

Create a browser instance and load the url.
The text is split due to the small line width.

    >>> this_browser = browser.Browser()
    >>> this_browser.load(url)
    create_text: x=1 y=2 text=a...
    create_text: x=1 y=4 text=b...
    create_text: x=1 y=6 text=c...
    create_text: x=1 y=8 text=d...

SCROLL_STEP configures how much to scroll by each time. Let's set it to
a convenient value:

    >>> browser.SCROLL_STEP = 5

After scrolling down the a should be off screen, and the b should be just about
  to disappear.

    >>> this_browser.scrolldown({})
    create_text: x=1 y=-1 text=b...
    create_text: x=1 y=1 text=c...
    create_text: x=1 y=3 text=d...

Now we can finally scroll up!
This should show the a again.

    >>> this_browser.scrollup({})
    create_text: x=1 y=2 text=a...
    create_text: x=1 y=4 text=b...
    create_text: x=1 y=6 text=c...
    create_text: x=1 y=8 text=d...

Scrolling up again should not change anything, since we are at the top of the
content.

    >>> this_browser.scrollup({})
    create_text: x=1 y=2 text=a...
    create_text: x=1 y=4 text=b...
    create_text: x=1 y=6 text=c...
    create_text: x=1 y=8 text=d...



Event details
-------------

The \<MouseWheel\> event behaves differently for each platform, as described
  (here)[https://wiki.tcl-lang.org/page/mousewheel]:
* Windows: A mousewheel click is translated by a delta of 120. Take care, that high resolution mousepads may emit smaller values which may accumulate.
* MacOS: A mousewheel click is translated by a delta of 1.
* X11: The mousewheel triggers button 4/5 (vertical) and Shift-4/Shift-5 (horizontal)

This causes some issues with compatibility, since Windows and MacOs can both
  indicate the amount to scroll using the delta value, but X11 cannot.

Negative delta values or button 5 indicate that the page should scoll down.


Testing `scrollwheel`
---------------------

To allow testing of your scrollwheel functionality make sure to name the
  method which handles the event `scrollwheel`.
For testing purposes we will use the Mac scaling, with the delta indicating the
  multiple of `SCROLL_STEP` to move.

Move down by one unit.

    >>> e = test.mousewheel_event(delta=-1)
    >>> this_browser.scrollwheel(e)
    create_text: x=1 y=-1 text=b...
    create_text: x=1 y=1 text=c...
    create_text: x=1 y=3 text=d...

Move up by three units, which should stop at the top of the content.

    >>> e = test.mousewheel_event(delta=3)
    >>> this_browser.scrollwheel(e)
    create_text: x=1 y=2 text=a...
    create_text: x=1 y=4 text=b...
    create_text: x=1 y=6 text=c...
    create_text: x=1 y=8 text=d...

Move down by two units.

    >>> e = test.mousewheel_event(delta=-2)
    >>> this_browser.scrollwheel(e)
    create_text: x=1 y=-2 text=d...
