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
* 


Test code
---------

Boilerplate.

    >>> import test
    >>> _ = test.socket.patch().start()
    >>> _ = test.ssl.patch().start()
    >>> import browser
