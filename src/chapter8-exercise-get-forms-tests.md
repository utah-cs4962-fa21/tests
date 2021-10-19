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
* To choose whether GET or POST should be used for a form use the form's
  "method" attribute, which will either be "GET" or "POST"
* Default to using GET


Test code
---------

Boilerplate.

    >>> import test
    >>> _ = test.socket.patch().start()
    >>> _ = test.ssl.patch().start()
    >>> import browser
