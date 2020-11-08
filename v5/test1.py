def evaluateRPN(y,x,variable):
    stack = Stack()
    eq = y.split(" ")
    eq = [x for x in eq if x]
    d_operators = ["+","-","*","/","^","log"]
    s_operators = ["sin","cos","tan",
                   "arcsin","arccos","arctan",
                   "cosec","sec","cot",
                   "!","sqrt","|",
                   "ln"]
    for i in range(len(eq)):
        if eq[i] == variable:
            eq[i] = x
        elif eq[i] == 'e':
            eq[i] = e
        elif eq[i] == 'pi':
            eq[i] = pi
    for i in eq:
        if i not in d_operators and i not in s_operators:
            stack.push(float(i))
        else:
            if i in s_operators:
                a = float(stack.pop())
                if i == s_operators[0]:
                    stack.push(math.sin(a))
                elif i == s_operators[1]:
                    stack.push(math.cos(a))
                elif i == s_operators[2]:
                    stack.push(math.tan(a))
                elif i == s_operators[3]:
                    stack.push(math.asin(a))
                elif i == s_operators[4]:
                    stack.push(math.acos(a))
                elif i == s_operators[5]:
                    stack.push(math.atan(a))
                elif i == s_operators[6]:
                    stack.push(1/(math.sin(a)))
                elif i == s_operators[7]:
                    stack.push(1/(math.cos(a)))
                elif i == s_operators[8]:
                    stack.push(1/(math.tan(a)))
                elif i == s_operators[10]:
                    stack.push(math.sqrt(a))
                elif i == s_operators[11]:
                    stack.push(abs(a))
                elif i == s_operators[12]:
                    stack.push(math.log(a,e))
            elif i in d_operators:
                b = float(stack.pop())
                a = float(stack.pop())
                if i == d_operators[0]:
                    stack.push(a+b)
                elif i == d_operators[1]:
                    stack.push(a-b)
                elif i == d_operators[2]:
                    stack.push(a*b)
                elif i == d_operators[3]:
                    stack.push(a/b)
                elif i == d_operators[4]:
                    stack.push(a**b)
                elif i == d_operators[5]:
                    stack.push(math.log(a,b))
    return stack.pop()

# Python program to convert infix expression to postfix

# Class to convert the expression
class Conversion:

    # Constructor to initialize the class variables
    def __init__(self, capacity):
        self.top = -1
        self.capacity = capacity
        # This array is used a stack
        self.array = []
        # Precedence setting
        self.output = []
        self.precedence = {'+':1, '-':1, '*':2, '/':2, '^':3}

    # check if the stack is empty
    def isEmpty(self):
        return True if self.top == -1 else False

    # Return the value of the top of the stack
    def peek(self):
        return self.array[-1]

    # Pop the element from the stack
    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.array.pop()
        else:
            return "$"

    # Push the element to the stack
    def push(self, op):
        self.top += 1
        self.array.append(op)

    # A utility function to check is the given character
    # is operand
    def isOperand(self, ch):
        return ch.isalpha()

    # Check if the precedence of operator is strictly
    # less than top of stack or not
    def notGreater(self, i):
        try:
            a = self.precedence[i]
            b = self.precedence[self.peek()]
            return True if a  <= b else False
        except KeyError:
            return False

    # The main function that
    # converts given infix expression
    # to postfix expression
    def infixToPostfix(self, exp):

        # Iterate over the expression for conversion
        for i in exp:
            # If the character is an operand,
            # add it to output
            if self.isOperand(i):
                self.output.append(i)

            # If the character is an '(', push it to stack
            elif i  == '(':
                self.push(i)

            # If the scanned character is an ')', pop and
            # output from the stack until and '(' is found
            elif i == ')':
                while( (not self.isEmpty()) and
                                self.peek() != '('):
                    a = self.pop()
                    self.output.append(a)
                if (not self.isEmpty() and self.peek() != '('):
                    return -1
                else:
                    self.pop()

            # An operator is encountered
            else:
                while(not self.isEmpty() and self.notGreater(i)):
                    self.output.append(self.pop())
                self.push(i)

        # pop all the operator from the stack
        while not self.isEmpty():
            self.output.append(self.pop())

        print "".join(self.output)

# Driver program to test above function
exp = "a+b*(c^d-e)^(f+g*h)-i"
obj = Conversion(len(exp))
obj.infixToPostfix(exp) 
