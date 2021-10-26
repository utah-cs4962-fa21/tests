Tests for WBE Chapter 9 Exercise `Event Bubbling`
============================================

Description
-----------

Right now, you can attach a click handler to a elements, but not to anything
    else.
Fix this.
One challenge you’ll face is that when you click on an element, you also click
    on all its ancestors.
On the web, this sort of quirk is handled by event bubbling: when an event is
    generated on an element, listeners are run not just on that element but
    also on its ancestors.
Implement event bubbling, and make sure listeners can call stopPropagation on
    the event object to stop bubbling the event up the tree.
Double-check that clicking on links still works, and make sure preventDefault
    still successfully prevents clicks on a link from actually following the
    link.


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
