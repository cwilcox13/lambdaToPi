from pyparsing import *
import string

# This is my initial attempt to build a program that can take a lambda expression as a string,
# and convert that lambda expression into a pi calculus expression. In order to parse the initial string,
# I am using the pyparsing module to separate the expression into variables, lambdas, abstractions,
# and applications. This returns a nested list of all the tokens. Then, I can call the convert()
# function, which takes into account the size of each portion of the return string in order to 
# determine what kind of expression it is looking at. It then returns a string containing all the 
# converted expressions along with coordinating variables. There are five test functions, ranging
# from small to medium sized lambda expressions. You are welcome to modify or add to the test functions,
# but you should be sure to keep a space between your tokens, like so (x y), or else the parser 
# will not work correctly. You must also use the word 'lambda' in place of the lambda symbol.

def convertVar(d, v):
	return d + "!" + v


def convert(d, s, letters):
	var = []
	var.append(letters[0])
	letters = letters[1:]
	var.append(letters[0])
	letters = letters[1:]
	var.append(letters[0])
	letters = letters[1:]
	var.append(letters[0])
	letters = letters[1:]
	if not d:
		return s
	if len(d) == 1:
		if not isinstance(d[0],list) and d[0] != "lambda":
			s = convertVar(d[0],var[0])
			del var[0]
			var.append(letters[0])
			letters = letters[1:]
		else:
			s = convert(d[0],s, letters)
	elif len(d) == 3:
		if d[0] == "lambda" and not isinstance(d[1],list):
			var1 = var[0]
			del var[0]
			var.append(letters[0])
			letters = letters[1:]
			var2 = var[0]
			del var[0]
			var.append(letters[0])
			letters = letters[1:]
			if not isinstance(d[2],list):
				s+= var1 + "?" + d[1] + "." + var1 + "?" + var2 + ".(" + convertVar(d[1],var2) + ")"
			else:
				s+= var1 + "?" + d[1] + "." + var1 + "?" + var2 + ".[" + convert(d[2],s, letters) + "](" + var2 + ")" 
		else:
			return "wrong format"
	elif len(d) == 2:
		var1 = var[0]
		del var[0]
		var.append(letters[0])
		letters = letters[1:]
		var2 = var[0]
		del var[0]
		var.append(letters[0])
		letters = letters[1:]
		var3 = var[0]
		del var[0]
		var.append(letters[0])
		letters = letters[1:]
		var4 = var[0]
		del var[0]
		var.append(letters[0])
		letters = letters[1:]
		if isinstance(d[0],list) and isinstance(d[1],list):
			s+=  "new(" + var1 + "," + var2 + ").([" + convert(d[0],s,letters) + "](" + var1 + "))|(" + var1 + "!" + var2 + "." + var1 + "!" + var3 + ")|*((" + var2 + "?" + var4 + ").[" + convert(d[1],s,letters) + "](" + var4 + "))"
		elif isinstance(d[0],list) and (not isinstance(d[1],list)):
			s+= "new(" + var1 + "," + var2 + ").([" + convert(d[0],s,letters) + "](" + var1 + "))|(" + var1 + "!" + var2 + "." + var1 + "!" + var3 + ")|*((" + var2 + "?" + var4 + ").(" + convertVar(d[1],var4) + "))"
		elif (not isinstance(d[0],list)) and isinstance(d[1],list):
			s+= "new(" + var1 + "," + var2 + ").(" + convertVar(d[0],var1) + ")|(" + var1 + "!" + var2 + "." + var1 + "!" + var3 + ")|*((" + var2 + "?" + var4 + ").[" + convert(d[1],s,letters) + "](" + var4 + "))"
		elif not isinstance(d[0],list) and not isinstance(d[1],list):
			s+= "new(" + var1 + "," + var2 + ").(" + convertVar(d[0],var1) + ")|(" + var1 + "!" + var2 + "." + var1 + "!" + var3 + ")|*((" + var2 + "?" + var4 + ").(" + convertVar(d[1],var4) + "))"
		else:
			return "wrong format"
	else:
		return "wrong format"
	return s

expression = Forward()

lparen = Literal("(").suppress()
rparen = Literal(")").suppress()

variable = Word( alphas, max=1 ) 
lam = Literal("lambda")
application = (expression + expression)
abstraction = (lam + variable + expression)


expression << (OneOrMore(Group(lparen + expression + rparen)) |
	OneOrMore(variable) | OneOrMore(abstraction) | OneOrMore(application))

data1 = 'x' 
data2 = 'lambda x x'
data3 = '(x y)'
data4 = '((lambda x x)(z t))'
data5 = 'lambda x ((x x) (x x))'

letters = string.lowercase

d1 = expression.parseString(data1).asList()
d2 = expression.parseString(data2).asList()
d3 = expression.parseString(data3).asList()
d4 = expression.parseString(data4).asList()
d5 = expression.parseString(data5).asList()

print data1 + " converts to: "
print convert (d1, '', letters)
print data2 + " converts to: "
print convert (d2, '', letters)
print data3 + " converts to: "
print convert (d3, '', letters)
print data4 + " converts to: "
print convert (d4, '', letters)
print data5 + " converts to: "
print convert (d5, '', letters)





