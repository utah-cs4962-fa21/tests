Tests for WBE Chapter 8 Exercise `Check boxes`
============================================

Description
-----------

In HTML, input elements have a type attribute.
When set to checkbox, the input element looks like a checkbox; it’s checked if
  the checked attribute is set, and unchecked otherwise.
Checkboxes are only included in the form submission when they’re checked.


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
