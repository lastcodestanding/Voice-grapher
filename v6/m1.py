import numpy as np
import math
import operator
#import recognition as rec

import matplotlib.pyplot as plt

# create the recognizer



#print("What would you like to plot?")

#rec.rec()

#f = open("my_result.txt", "r")

#result = (f.read())

#print("You said:", result)

"""
fucntion word2symbol converts all the keywords
in the sentence to mathematical symbols
func=func.replace('','')

"""
def format_space(str):

    input_exp = str
    y=""
    func_list = ["log","sin", "cos", "tan", "arctan", "arcsin", "arccos", "round", "abs"]

    input_exp = input_exp.split()
    for i in range(len(input_exp)):
        if input_exp[i] in func_list and input_exp[i+1][0]!='(':
            input_exp[i] = input_exp[i]+'('
            input_exp[i+1] = input_exp[i+1]+')'
    for i in input_exp:
        y = y+i+" "
    input_exp = y[:-1].replace('( ','(')

    a = ["0 x","1 x","2 x","3 x","4 x","5 x","6 x","7 x","8 x","9 x"]
    for i in a:
        input_exp = input_exp.replace(i,i[0]+" * "+i[2])

    #print(input_exp)
    return(input_exp.rstrip())
    #return ex

print(format_space("sin x"))

def words2symbol(func):
    "basic math functions"
    func=func.replace('plus','+')
    func=func.replace('added to','+')
    func=func.replace('minus','-')
    func=func.replace('divided by','-')
    func=func.replace('upon','/')
    func=func.replace('into','*')
    func=func.replace('multiplied by','*')
    func=func.replace('times','*')
    func=func.replace('greater than','>')
    func=func.replace('greater than or equal to','>=')
    func=func.replace('less than','<')
    func=func.replace('less than or equal to','<=')


    "mathematic symbols"
    func=func.replace('parentheses open','(')
    func=func.replace('parentheses close',')')
    func=func.replace('round brackets open','(')
    func=func.replace('round brackets close',')')
    func=func.replace('braces open','{')
    func=func.replace('bracket ','(')
    func=func.replace('braces close','}')
    func=func.replace('curly brackets open','{')
    func=func.replace('curly brackets close','}')
    func=func.replace('square brackets open','[')
    func=func.replace('square brackets close',']')
    func=func.replace('brackets open','(')
    func=func.replace('brackets close',')')
    func=func.replace('equals','=')
    func=func.replace('equals to','=')

    "trignometric functions"
    func=func.replace('sin ','sin')
    func=func.replace('sign ','sin')
    func=func.replace('cosine ','cos')
    func=func.replace('cos ','cos')
    func=func.replace('tangent ','tan')
    func=func.replace('tan ','tan')
    func=func.replace('dog ','log')
    func=func.replace('lock ','log')
    func=func.replace('log ','log')
    #func=func.replace('cosecant','cosec')
    #func=func.replace('cosec','cosec')
    #func=func.replace('secant','sec')
    #func=func.replace('sec','sec')
    #func=func.replace('cotangent','cot')
    #func=func.replace('cotan','cot')
    #func=func.replace('cot','cot')
    func=func.replace('sine inverse','arcsin')
    func=func.replace('cosine inverse','arccos')
    func=func.replace('tan inverse','arctan')
    #func=func.replace('cosec inverse','arcsc')
    #func=func.replace('sec inverse','arcsec')
    #func=func.replace('cot inverse','arccot')




    "exponential and logarithmic functions"
    func=func.replace('raise to','^')
    func=func.replace('raised to','^')
    func=func.replace('raise to the power of','^')
    func=func.replace('squared','^ 2')
    func=func.replace('square','^ 2')
    func=func.replace('cubed','^ 3')
    func=func.replace('cube','^ 3')





    "other general functions"
    func=func.replace('rounded to','round')
    func=func.replace('absolute value of', 'abs')
    return func



import operator

import numpy as np

import matplotlib.pyplot as plt

import math

n=[]

def format_exp(str):

    formatted = ""

    input_exp = str
    input_exp.split()

    for i in range(len(input_exp)):

        if i < len(input_exp) -1 and  input_exp[i].isdigit() and input_exp[i+1] != "x":
             formatted = formatted + input_exp[i] + " "

        elif input_exp[i].isdigit() and i == len(input_exp):

            formatted = formatted + input_exp[i] + " "

        elif input_exp[i] == "x" and input_exp[i+1] in ["+", "-", "*", "/", "^"] and input_exp[i-1].isdigit():

            formatted = formatted + input_exp[i-1] + " " + "*" + " " + input_exp[i] + " "


        elif input_exp[i] in ["+", "-", "*", "/", "^"]:

            formatted = formatted + input_exp[i] + " "



    ex = formatted

    return ex

#print(format_exp("2 x + 3"))


def f(ex):
    def f1(expr):
        print(expr)
        x =  np.arange(0,3,0.001)

        a=[]



        def fn(str1):

            ops = {

                '+' : operator.add,

                '-' : operator.sub,

                '*' : operator.mul,

                '/' : operator.truediv,

                '^' : operator.pow

            }

            def splitter(str1):

                str2 = str1[::-1]

                p = str2.split(" ",(2))[::-1]

                for i in range(len(p)):

                    p[i] = p[i][::-1]
                print(p)
                return p



            p = splitter(str1)



            def eval_binary_expr(op1, oper, op2, get_operator_fn=ops.get):



                if op1.find(" ")<0 and op2.find(" ")<0:

                    if op2 != "x" and op2[0]!= "a" and op2[0]!= "n" and op2!="e":

                        op2 = int(op2)

                    elif op2=="e":
                        op2 = 2.1728
                    elif op2=="x":

                        op2 = x

                    elif op2[0]== "a":

                        op2 = a[int(op2[1])]

                    elif op2[0]== "n":

                        op2 = n[int(op2[1])]





                    if op1 != "x" and op1[0] != "a" and op1[0] != "n" and op1!='e':

                        op1 = int(op1)
                    elif op1=='e':
                        op1 = 2.7128

                    elif op1=="x":

                        op1 = x

                    elif op1[0] =="a":

                        op1 = a[int(op1[1])]

                    elif op1[0] =="n":

                        op1 = n[int(op1[1])]



                    return get_operator_fn(oper)(op1, op2)



                elif op1.find(" ")>=0:

                    if op2 != "x" and op2[0]!= "a" and op2[0]!= "n" and op2!='e':

                        op2 = int(op2)

                    elif op2=='e':
                        op2 = 2.7128

                    elif op2=="x":

                        op2 = x

                    elif op2[0]== "a":

                        op2 = a[int(op2[1])]

                    elif op2[0]== "n":

                        op2 = n[int(op2[1])]



                    temp = splitter(op1)

                    return get_operator_fn(oper)(eval_binary_expr(splitter(op1)[0],splitter(op1)[1],splitter(op1)[2]), op2)




            if len(p)>1:
                y = eval_binary_expr(p[0],p[1],p[2])

            else:
                if p[0] != "x" and p[0][0]!= "a" and p[0][0]!= "n" and p[0]!='e':

                        return int(p[0])

                elif p[0]=='e':
                    return 2.7128
                elif p[0]=="x":

                        return x

                elif p[0][0]== "a":

                        return a[int(p[0][1])]

                elif p[0][0]== "n":

                        return n[int(p[0][1])]

            return y



        str1 = expr

        str2 = str1

        a = []

        i=0



        while '(' in str2:

            lastb = len(str2) - str2[::-1].find('(')

            a.append(str2[lastb:lastb+str2[lastb:].find(')')])

            #if fn(a[])

            str2 = str2.replace("("+str(a[i])+")", "a"+str(i))

            a[i] = fn(a[i])

            #a[i] = fn(a[i])

            print(a)

            print(str2)

            i+=1





        y = fn(str2)
        return y

        #print(y)

        #plt.plot(x,np.power(x,x))

        #plt.show()



        #print(operator.pow(x,x))








    def fn2(str3):

        func_list = ["log","sin", "cos", "tan", "arctan", "arcsin", "arccos", "round", "abs"]

        i = 0

        #print(str3)
        y=[]
        while ("log" in str3 or "sin" in str3 or "cos" in str3 or "tan" in str3 or "arctan" in str3 or "arccos" in str3 or  "arcsin" in str3 or "round" in str3 or "abs" in str3):

            max = 0

            max_func = func_list[0]

            for f in func_list:

                last_index = len(str3) - str3[::-1].find(f[::-1])
                #print(last_index)

                if last_index <len(str3) and last_index >= max:

                    max = last_index

                    max_func = f





            first_b = max
            print(first_b)
            open = 1
            last_b = 0

            for char in str3[first_b+1:]:

                if char == "(":
                    open = open + 1

                elif char == ")":
                    open = open - 1

                if open == 0:
                   last_b = str3.index(char)
                   break


            print(last_b)
            print(str3[first_b+1: last_b])
            #y = f1(str3[first_b+1: last_b])
            if max_func == "sin":
                y = np.sin(f1(str3[first_b+1: last_b]))

            elif max_func == "cos":
                y = np.cos(f1(str3[first_b+1: last_b]))

            elif max_func == "tan":
                y = np.tan(f1(str3[first_b+1: last_b]))

            elif max_func == "arcsin":
                y = np.asin(f1(str3[first_b+1: last_b]))

            elif max_func == "arccos":
                y = np.acos(f1(str3[first_b+1: last_b]))

            elif max_func == "arctan":
                y = np.atan(f1(str3[first_b+1: last_b]))

            elif max_func == "round":
                y = round(f1(str3[first_b+1: last_b]))

            elif max_func == "abs":
                y = abs(f1(str3[first_b+1: last_b]))

            elif max_func == "log":
                y = np.log(f1(str3[first_b+1: last_b]))

            print(y)
            n.append(y)
            str3 = str3.replace(max_func+"("+str3[first_b+1: last_b]+")", "n"+str(i))
            print(str3)
            i = i + 1
        return y

    print(ex)
    if ("log" in ex or "sin" in ex or "cos" in ex or "tan" in ex or "arctan" in ex or "arccos" in ex or  "arcsin" in ex or "round" in ex or "abs" in ex):
        print("f2")
        return fn2(ex)
    else:
        return f1(ex)
#fn2("sin(cos(x ^ 3 + 3))")
