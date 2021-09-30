Tests for WBE Chapter 6 Exercise `Shorthand Properties`
=======================

Description
-----------

CSS “shorthand properties” set multiple related CSS properties at the same time;
  for example, `font: italic bold 100% Times` sets the font-style, font-weight, 
  font-size, and font-family properties all at once. 
Add shorthand properties to your parser. 
(If you haven’t implemented font-family, just ignore that part.)

    >>> import test
    >>> _ = test.socket.patch().start()
    >>> _ = test.ssl.patch().start()
    >>> import browser

+ always give all four
must modify parser and expand in parser


only check font shorthand

single rule with multple properties

`p { font: foo bar baz bam; font-family: yolo; }`
