Tests for WBE Chapter 9 Exercise `Node.children`
============================================

Description
-----------

Add support for the children property on JavaScript Nodes.
Node.children returns the immediate Element children of a node, as an array.
Text children are not included.


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
