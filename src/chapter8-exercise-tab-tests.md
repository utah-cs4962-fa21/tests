Tests for WBE Chapter 8 Exercise `Tab`
============================================

Description
-----------

In most browsers, the `<Tab>` key (on your keyboard) moves focus from one input
  field to the next.
Implement this behavior in your browser.
The “tab order” of input elements should be the same as the order of `<input>`
  elements on the page.
You can also add support for the tabindex property, which lets a web page
  change this tab order.


Extra Requirements
------------------
* Name the method in the `Browser` class that handles the enter event
  `handle_tab`


Test code
---------

Boilerplate.

    >>> import test
    >>> _ = test.socket.patch().start()
    >>> _ = test.ssl.patch().start()
    >>> import browser
