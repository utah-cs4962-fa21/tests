Tests for WBE Chapter 8 Exercise `Enter key`
============================================

Description
-----------

In most browsers, if you hit the “Enter” or “Return” key while inside a text
  entry, that submits the form that the text entry was in.
Add this feature to your browser.


Extra Requirements
------------------
* Name the method in the `Browser` class that handles the enter event
  `handle_enter`


Test code
---------

Boilerplate.

    >>> import test
    >>> _ = test.socket.patch().start()
    >>> _ = test.ssl.patch().start()
    >>> import browser
