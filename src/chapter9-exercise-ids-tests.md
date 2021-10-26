Tests for WBE Chapter 9 Exercise `IDs`
============================================

Description
-----------

When an HTML element has an id attribute, a JavaScript variable pointing to
    that element is predefined.
So, if a page has a `<div id="foo"></div>`, then there’s a variable foo
    referring to that node.
Implement this in your browser.
Make sure to handle the case of nodes being added and removed (such as with
    innerHTML).


Extra Requirements
------------------
* 


Test code
---------

Boilerplate.

    >>> import test
    >>> _ = test.socket.patch().start()
    >>> _ = test.ssl.patch().start()
    >>> import browser
