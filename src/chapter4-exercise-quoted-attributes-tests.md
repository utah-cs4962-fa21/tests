Tests for WBE Chapter 4 Exercise `Quoted attributes`
====================================================

Description
------------

Quoted attributes can contain spaces and right angle brackets. 
Fix the lexer so that this is supported properly.
Hint: the current lexer is a finite state machine, with two states 
  (determined by in_tag). You’ll need more states.

Testing boilerplate:

    >>> import browser
    >>> def test_parse(text):
    ...     parser = browser.HTMLParser(text)
    ...     browser.print_tree(parser.parse())

Quotes should already be supported, since `get_attributes` already checks for
  single and double quotes.
The issue when adding spaces to an attribute is how the text is split into 
  parts in that method.

    >>> test_parse("<img src=lhc.jpg alt='Les Horribles Cernettes'>")
     <html>
       <body>
         <img src="lhc.jpg" alt="Les Horribles Cernettes">

    >>> test_parse('<div foo="bar baz"></div>')
     <html>
       <body>
         <div foo="bar baz">

Allowing the greater than symbol in a quoted attribute requires the additional 
  states mentioned in the exercise.

    >>> test_parse("<br confusing='why does a <br> have an attribute?'>")
     <html>
       <body>
         <br confusing="why does a <br> have an attribute?">
