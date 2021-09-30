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

+ negative heights mean auto (technically a syntax error)

All these bigger, just look at layout tree

No spec

    >>> url = 'http://test.test/chapter6_example5'
    >>> test.socket.respond_200(url, 
    ...   body="<div>Auto layout</div>")
    >>> this_browser = browser.Browser()
    >>> this_browser.load(url)
    >>> browser.print_tree(this_browser.document)
     DocumentLayout()
       BlockLayout(x=13, y=18, width=774, height=15.0)
         BlockLayout(x=13, y=18, width=774, height=15.0)
           InlineLayout(x=13, y=18, width=774, height=15.0)

Width

    >>> url = 'http://test.test/chapter6_example6'
    >>> test.socket.respond_200(url, 
    ...   body='<div style="width:1000px">Set width</div>')
    >>> this_browser = browser.Browser()
    >>> this_browser.load(url)
    >>> browser.print_tree(this_browser.document)
     DocumentLayout()
       BlockLayout(x=13, y=18, width=774, height=15.0)
         BlockLayout(x=13, y=18, width=1000, height=15.0)
           InlineLayout(x=13, y=18, width=1000, height=15.0)

Height

    >>> url = 'http://test.test/chapter6_example7'
    >>> test.socket.respond_200(url, 
    ...   body='<div style="height:100px">Set height</div>')
    >>> this_browser = browser.Browser()
    >>> this_browser.load(url)
    >>> browser.print_tree(this_browser.document)
     DocumentLayout()
       BlockLayout(x=13, y=18, width=774, height=100.0)
         BlockLayout(x=13, y=18, width=774, height=100.0)
           InlineLayout(x=13, y=18, width=774, height=100.0)

Both

    >>> url = 'http://test.test/chapter6_example8'
    >>> test.socket.respond_200(url, 
    ...   body='<div style="width:900px height:200px">Set both</div>')
    >>> this_browser = browser.Browser()
    >>> this_browser.load(url)
    >>> browser.print_tree(this_browser.document)
     DocumentLayout()
       BlockLayout(x=13, y=18, width=774, height=200.0)
         BlockLayout(x=13, y=18, width=900, height=200.0)
           InlineLayout(x=13, y=18, width=900, height=200.0)

Width is negative

    >>> url = 'http://test.test/chapter6_example9'
    >>> test.socket.respond_200(url, 
    ...   body='<div style="width:-10px">Default to auto</div>')
    >>> this_browser = browser.Browser()
    >>> this_browser.load(url)
    >>> browser.print_tree(this_browser.document)
     DocumentLayout()
       BlockLayout(x=13, y=18, width=774, height=15.0)
         BlockLayout(x=13, y=18, width=774, height=15.0)
           InlineLayout(x=13, y=18, width=774, height=15.0)

Width is smaller than normal, and wraps text

    >>> url = 'http://test.test/chapter6_example10'
    >>> test.socket.respond_200(url, 
    ...   body='<div style="width:100">Wrap me since width is set</div>')
    >>> this_browser = browser.Browser()
    >>> this_browser.load(url)
    >>> browser.print_tree(this_browser.document)
     DocumentLayout()
       BlockLayout(x=13, y=18, width=774, height=15.0)
         BlockLayout(x=13, y=18, width=100, height=15.0)
           InlineLayout(x=13, y=18, width=100, height=15.0)


