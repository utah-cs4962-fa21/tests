Tests for WBE Chapter 9 Exercise `createElement`
============================================

Description
-----------

The `document.createElement` method creates a new element, which can be attached
    to the document with the `appendChild` and `insertBefore` methods on Nodes;
    unlike innerHTML, there’s no parsing involved.
Implement all three methods.


Extra Requirements
------------------
* We will only call `appendChild` and `insertBefore` to add newly created
  elements using valid arguments.

Test code
---------

Boilerplate.

    >>> import test
    >>> _ = test.socket.patch().start()
    >>> _ = test.ssl.patch().start()
    >>> test.NORMALIZE_FONT = True
    >>> import browser

Show the page with no content changes by scripts.

    >>> web_url = 'http://test.test/chapter9-create-1/html'
    >>> html = "<div>Some content</div> <p>More content</p>"
    >>> test.socket.respond_200(web_url, body=html)
    >>> this_browser = browser.Browser()
    >>> this_browser.load(web_url)
    >>> browser.print_tree(this_browser.tabs[0].document)
     DocumentLayout()
       BlockLayout(x=13, y=18, width=774, height=30.0)
         BlockLayout(x=13, y=18, width=774, height=30.0)
           InlineLayout(x=13, y=18, width=774, height=15.0)
             LineLayout(x=13, y=18, width=774, height=15.0)
               TextLayout(x=13, y=20.25, width=48, height=12, font=Font size=12 weight=normal slant=roman style=None)
               TextLayout(x=73, y=20.25, width=84, height=12, font=Font size=12 weight=normal slant=roman style=None)
           InlineLayout(x=13, y=33.0, width=774, height=15.0)
             LineLayout(x=13, y=33.0, width=774, height=15.0)
               TextLayout(x=13, y=35.25, width=48, height=12, font=Font size=12 weight=normal slant=roman style=None)
               TextLayout(x=73, y=35.25, width=84, height=12, font=Font size=12 weight=normal slant=roman style=None)

Set up the webpage and script links.
Create a button and add it as a child to the `<body>` at the end.

    >>> web_url = 'http://test.test/chapter9-create-2/html'
    >>> script_url = 'http://test.test/chapter9-create-2/js'
    >>> html = ("<script src=" + script_url + "></script>"
    ...         + "<div>Some content</div> <p>More content</p>")
    >>> test.socket.respond_200(web_url, body=html)
    >>> script = """
    ... new_elt = document.createElement("button");
    ... my_body = document.querySelectorAll('body')[0];
    ... my_body.appendChild(new_elt);
    ... """
    >>> test.socket.respond_200(script_url, body=script)
    >>> this_browser = browser.Browser()
    >>> this_browser.load(web_url)
    >>> browser.print_tree(this_browser.tabs[0].document)
     DocumentLayout()
       BlockLayout(x=13, y=18, width=774, height=30.0)
         InlineLayout(x=13, y=18, width=774, height=0)
           LineLayout(x=13, y=18, width=774, height=0)
         BlockLayout(x=13, y=18, width=774, height=30.0)
           InlineLayout(x=13, y=18, width=774, height=15.0)
             LineLayout(x=13, y=18, width=774, height=15.0)
               TextLayout(x=13, y=20.25, width=48, height=12, font=Font size=12 weight=normal slant=roman style=None)
               TextLayout(x=73, y=20.25, width=84, height=12, font=Font size=12 weight=normal slant=roman style=None)
           InlineLayout(x=13, y=33.0, width=774, height=15.0)
             LineLayout(x=13, y=33.0, width=774, height=15.0)
               TextLayout(x=13, y=35.25, width=48, height=12, font=Font size=12 weight=normal slant=roman style=None)
               TextLayout(x=73, y=35.25, width=84, height=12, font=Font size=12 weight=normal slant=roman style=None)
           BlockLayout(x=13, y=48.0, width=774, height=0)


Create a button and add it inside the `<body>` before the `<div>`

    >>> web_url = 'http://test.test/chapter9-create-3/html'
    >>> script_url = 'http://test.test/chapter9-create-3/js'
    >>> html = ("<script src=" + script_url + "></script>"
    ...         + "<div>Some content</div> <p>More content</p>")
    >>> test.socket.respond_200(web_url, body=html)
    >>> script = """
    ... new_elt = document.createElement("button");
    ... my_body = document.querySelectorAll('body')[0];
    ... my_div = document.querySelectorAll('div')[0];
    ... my_body.insertBefore(new_elt, my_div);
    ... """
    >>> test.socket.respond_200(script_url, body=script)
    >>> this_browser = browser.Browser()
    >>> this_browser.load(web_url)
    >>> browser.print_tree(this_browser.tabs[0].document)
     DocumentLayout()
       BlockLayout(x=13, y=18, width=774, height=30.0)
         InlineLayout(x=13, y=18, width=774, height=0)
           LineLayout(x=13, y=18, width=774, height=0)
         BlockLayout(x=13, y=18, width=774, height=30.0)
           BlockLayout(x=13, y=18, width=774, height=0)
           InlineLayout(x=13, y=18, width=774, height=15.0)
             LineLayout(x=13, y=18, width=774, height=15.0)
               TextLayout(x=13, y=20.25, width=48, height=12, font=Font size=12 weight=normal slant=roman style=None)
               TextLayout(x=73, y=20.25, width=84, height=12, font=Font size=12 weight=normal slant=roman style=None)
           InlineLayout(x=13, y=33.0, width=774, height=15.0)
             LineLayout(x=13, y=33.0, width=774, height=15.0)
               TextLayout(x=13, y=35.25, width=48, height=12, font=Font size=12 weight=normal slant=roman style=None)
               TextLayout(x=73, y=35.25, width=84, height=12, font=Font size=12 weight=normal slant=roman style=None)

Create a button and add it inside the `<body>` before the `<p>`

    >>> web_url = 'http://test.test/chapter9-create-4/html'
    >>> script_url = 'http://test.test/chapter9-create-4/js'
    >>> html = ("<script src=" + script_url + "></script>"
    ...         + "<div>Some content</div> <p>More content</p>")
    >>> test.socket.respond_200(web_url, body=html)
    >>> script = """
    ... new_elt = document.createElement("button");
    ... my_body = document.querySelectorAll('body')[0];
    ... my_p = document.querySelectorAll('p')[0];
    ... my_body.insertBefore(new_elt, my_p);
    ... """
    >>> test.socket.respond_200(script_url, body=script)
    >>> this_browser = browser.Browser()
    >>> this_browser.load(web_url)
    >>> browser.print_tree(this_browser.tabs[0].document)
     DocumentLayout()
       BlockLayout(x=13, y=18, width=774, height=30.0)
         InlineLayout(x=13, y=18, width=774, height=0)
           LineLayout(x=13, y=18, width=774, height=0)
         BlockLayout(x=13, y=18, width=774, height=30.0)
           InlineLayout(x=13, y=18, width=774, height=15.0)
             LineLayout(x=13, y=18, width=774, height=15.0)
               TextLayout(x=13, y=20.25, width=48, height=12, font=Font size=12 weight=normal slant=roman style=None)
               TextLayout(x=73, y=20.25, width=84, height=12, font=Font size=12 weight=normal slant=roman style=None)
           BlockLayout(x=13, y=33.0, width=774, height=0)
           InlineLayout(x=13, y=33.0, width=774, height=15.0)
             LineLayout(x=13, y=33.0, width=774, height=15.0)
               TextLayout(x=13, y=35.25, width=48, height=12, font=Font size=12 weight=normal slant=roman style=None)
               TextLayout(x=73, y=35.25, width=84, height=12, font=Font size=12 weight=normal slant=roman style=None)

Create a button and add it inside the `<body>` at then end of its children
by using `insertBefore` with a reference node of null.

    >>> web_url = 'http://test.test/chapter9-create-5/html'
    >>> script_url = 'http://test.test/chapter9-create-5/js'
    >>> html = ("<script src=" + script_url + "></script>"
    ...         + "<div>Some content</div> <p>More content</p>")
    >>> test.socket.respond_200(web_url, body=html)
    >>> script = """
    ... new_elt = document.createElement("button");
    ... my_body = document.querySelectorAll('body')[0];
    ... my_body.insertBefore(new_elt, null);
    ... """
    >>> test.socket.respond_200(script_url, body=script)
    >>> this_browser = browser.Browser()
    >>> this_browser.load(web_url)
    >>> browser.print_tree(this_browser.tabs[0].document)
     DocumentLayout()
       BlockLayout(x=13, y=18, width=774, height=30.0)
         InlineLayout(x=13, y=18, width=774, height=0)
           LineLayout(x=13, y=18, width=774, height=0)
         BlockLayout(x=13, y=18, width=774, height=30.0)
           InlineLayout(x=13, y=18, width=774, height=15.0)
             LineLayout(x=13, y=18, width=774, height=15.0)
               TextLayout(x=13, y=20.25, width=48, height=12, font=Font size=12 weight=normal slant=roman style=None)
               TextLayout(x=73, y=20.25, width=84, height=12, font=Font size=12 weight=normal slant=roman style=None)
           InlineLayout(x=13, y=33.0, width=774, height=15.0)
             LineLayout(x=13, y=33.0, width=774, height=15.0)
               TextLayout(x=13, y=35.25, width=48, height=12, font=Font size=12 weight=normal slant=roman style=None)
               TextLayout(x=73, y=35.25, width=84, height=12, font=Font size=12 weight=normal slant=roman style=None)
           BlockLayout(x=13, y=48.0, width=774, height=0)
