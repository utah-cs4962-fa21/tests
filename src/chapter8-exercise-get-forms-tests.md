Tests for WBE Chapter 8 Exercise `GET forms`
============================================

Description
-----------

Forms can be submitted via GET requests as well as POST requests.
In GET requests, the form-encoded data is pasted onto the end of the URL,
  separated from the path by a question mark, like `/search?q=hi`; GET form
  submissions have no body.
Implement GET form submissions.


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
