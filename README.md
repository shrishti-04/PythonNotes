<h1>Python Notes</h1>
<p> Here you will see some important concepts of programming using python.<p>
  
<h2>Functions and Keywords</h2>

<p>Functions and keywords are the building blocks of a language’s syntax.
Functions are pieces of code that perform a unit of work.
Keywords are reserved words that are used to construct instructions. </p>
<p> Some of the keywords are: </p>
<img src="screenshots/keywords.jpg">

<p>You can view some examples from here <a href="https://www.programiz.com/python-programming/keyword-list">examples</a></p>

<h2>Operations</h2>
<p> a + b = Adds a and b <br>
a - b = Subtracts b from a <br>
a * b = Multiplies a and b <br>
a / b = Divides a by b <br>
a ** b = Elevates a to the power of b. For non integer values of b, this becomes a root (i.e. a**(1/2) is the square root of a) <br>
a // b = The integer part of the integer division of a by b <br>
a % b = The remainder part of the integer division of a by b </p>

<h2>Data Types</h2>
<p><b>Note:</b> Do not try to add different types data types together otherwise you would get error</p>
<p>For example: print(3 + "5")</p>

<h2>Variable</h2>
<p><b>Variables:</b> Names that we give to certain values in our programs.</p>
<p><b>Assignment:</b> The process of storing a value inside a variable.</p>
<p><b>Expression:</b> A combination of numbers, symbols, or other variables that produce a result when evaluated.</p>

<h2>Functions</h2>
<p>A function is defined with the def keyword, followed by the name we want to give our function. After the name, we have the parameters, also called arguments, for the function enclosed in parentheses. A function can have no parameters, or it can have multiple parameters. Parameters allow us to call a function and pass it data, with the data being available inside the function as variables with the same name as the parameters.</p>

<h2>Comparison Operators</h2>
<p>In Python, we can use comparison operators to compare values. When a comparison is made, Python returns a boolean result, or simply a True or False. </p>

<ul>
<li>To check if two values are the same, we can use the equality operator: == </li>
<li>To check if two values are not the same, we can use the not equals operator: != </li>

<br>

<p>We can also check if values are greater than or lesser than each other using > and <. <br> <b>Note:</b> If you try to compare data types that aren’t compatible, like checking if a string is greater than an integer, Python will throw a TypeError.</p>

<p>The three main logical operators are <b>and</b>, <b>or</b>, and <b>not</b>. When using the <b>and</b> operator, both sides of the statement being evaluated must be true for the whole statement to be true. When using the <b>or</b> operator, if either side of the comparison is true, then the whole statement is true. Lastly, the <b>not</b> operator simply inverts the value of the statement immediately following it. So if a statement evaluates to True, and we put the not operator in front of it, it would become False.</p>

<h2>If, Else and Elif Statement</h2>

<p>Building off of the if and else blocks, which allow us to branch our code depending on the evaluation of one statement, the elif statement allows us even more comparisons to perform more complex branching. Very similar to the if statements, an elif statement starts with the elif keyword, followed by a comparison to be evaluated. This is followed by a colon, and then the code block on the next line, indented to the right. An elif statement must follow an if statement, and will only be evaluated if the if statement was evaluated as false. You can include multiple elif statements to build complex branching in your code to do all kinds of powerful things!</p>

<p>In Python, we branch our code using if, else and elif. This is the branching syntax:</p>

<p>if condition1:<br>
	if-block<br>
elif condition2:<br>
	elif-block<br>
else:<br>
	else-block</p>

<p><b>Note:</b> The if-block will be executed if condition1 is True. The elif-block will be executed if condition1 is False and condition2 is True. The else block will be executed when all the specified conditions are false.</p>