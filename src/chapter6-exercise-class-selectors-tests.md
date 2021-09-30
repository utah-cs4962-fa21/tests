Tests for WBE Chapter 6 Exercise `Class Selectors`
=======================

Description
-----------

Any HTML element can have a class attribute, whose value is a space-separated 
  list of tags that apply to that element. 
A CSS class selector, like .main, affects all elements tagged main. 
Implement class selectors; give them priority 10. 
If you’ve implemented them correctly, you should see code blocks in this book 
  being syntax-highlighted.

    >>> import test
    >>> _ = test.socket.patch().start()
    >>> _ = test.ssl.patch().start()
    >>> import browser

parsing: check that .main is parsed as selector
ClassSelectgor("b").matches(
  Element("p", None, {"class": "a b"}))
  
.a ~ a b
.b ~ a b
.a !~ cat
  
check that element with mutple classes is matched correctly 

`.a p` mixed descendant

sort selectors to get priority order
p
h1 b
.foo
.foo p
