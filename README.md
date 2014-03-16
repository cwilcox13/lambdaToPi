lambdaToPi
==========

This is my initial attempt to build a program that can take a lambda expression as a string,
and convert that lambda expression into a pi calculus expression. In order to parse the initial string,
I am using the pyparsing module to separate the expression into variables, lambdas, abstractions,
and applications. This returns a nested list of all the tokens. Then, I can call the convert()
function, which takes into account the size of each portion of the return string in order to 
determine what kind of expression it is looking at. It then returns a string containing all the 
converted expressions along with coordinating variables. There are five test functions, ranging
from small to medium sized lambda expressions. You are welcome to modify or add to the test functions,
but you should be sure to keep a space between your tokens, like so (x y), or else the parser 
will not work correctly. You must also use the word 'lambda' in place of the lambda symbol.
