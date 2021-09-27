Tests for WBE Chapter 6 Exercise `Width/Height`
=======================

Description
-----------

Add support to block layout objects for the width and height properties. 
These can either be a pixel value, which directly sets the width or height of 
  the layout object, or the word auto, in which case the existing layout 
  algorithm is used.

    >>> import test
    >>> _ = test.socket.patch().start()
    >>> _ = test.ssl.patch().start()
    >>> import browser

