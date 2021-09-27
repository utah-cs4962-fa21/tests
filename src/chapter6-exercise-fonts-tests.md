Tests for WBE Chapter 6 Exercise `Fonts`
=======================

Description
-----------

Implement the font-family property, an inheritable property that names which 
  font should be used in an element. 
Make code fonts use some nice monospaced font like Courier.

    >>> import test
    >>> _ = test.socket.patch().start()
    >>> _ = test.ssl.patch().start()
    >>> import browser

