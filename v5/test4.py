import matplotlib.pyplot as plt
import numpy as np
import sympy
from sympy.abc import x



def derivation(stringExpression):
    exp = sympy.sympify(stringExpression)
    print('the expression you entered is: {}'.format(exp))
    dexp = sympy.diff(exp)
    print('the derivative of the expression you entered is: {}'.format(dexp))
    dexpr = [0]*len(a)
    for i in range(0,len(a)-1,1):
        try:
            dexpr[i]=dexp.subs(x,a[i]).evalf()
        except:
            continue
    plt.plot(a,expr)
    plt.plot(a,dexpr)
    plt.show()


def integration(stringExpression):
    exp = sympy.sympify(stringExpression)
    print('the expression you entered is: {}'.format(exp))
    iexp = sympy.integrate(exp,x)
    print('the integration of the expression you entered is: {}'.format(iexp))
    iexpr = [0]*len(a)
    for i in range(0,len(a)-1,1):
        iexpr[i]=iexp.subs(x,a[i]).evalf()
    plt.plot(a,expr)
    plt.plot(a,iexpr)
    plt.show()


sent = input("enter:")
exp = sympy.sympify(sent)
a = np.arange(0,10,0.1)
expr = [0]*len(a)
for i in range(0,len(a)-1,1):
    expr[i]=exp.subs(x,a[i]).evalf()
derivation(sent)
integration(sent)
