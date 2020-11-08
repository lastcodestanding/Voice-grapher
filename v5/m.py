import operator
import numpy as np
import matplotlib.pyplot as plt

def f1(expr):
    x =  np.arange(0,10,0.01)
    a=[]
    out=[]
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
            return p

        p = splitter(str1)

        def eval_binary_expr(op1, oper, op2, get_operator_fn=ops.get):

            if op1.find(" ")<0 and op2.find(" ")<0:
                if op2 != "x" and op2[0]!= "a":
                    op2 = int(op2)
                elif op2=="x":
                    op2 = x
                elif op2[0]== "a":
                    op2 = a[int(op2[1])]

                if op1 != "x" and op1[0] != "a":
                    op1 = int(op1)
                elif op1=="x":
                    op1 = x
                elif op1[0] =="a":
                    op1 = a[int(op1[1])]
                return get_operator_fn(oper)(op1, op2)

            elif op1.find(" ")>=0:
                if op2 != "x" and op2[0]!= "a":
                    op2 = int(op2)
                elif op2=="x":
                    op2 = x
                elif op2[0]== "a":
                    op2 = a[int(op2[1])]

                temp = splitter(op1)
                return get_operator_fn(oper)(eval_binary_expr(splitter(op1)[0],splitter(op1)[1],splitter(op1)[2]), op2)

        y = eval_binary_expr(p[0],p[1],p[2])
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


    out = fn(str2)
    return out

#print(y)
#plt.plot(x,np.power(x,x))
#plt.show()

#print(operator.pow(x,x))
