# Alex tatievsky 317414506

import sympy as sp

def newtonraph(f,ft,a,b):
    """
    newton raphson
    """
    xn = (a+b)/2
    for n in range(0,500):
        fxn = f(xn)
        if abs(fxn) < 0.0001:
            print(n, "Iterations, x=",round(xn, 4))
            return round(xn, 4)
        ftxn = ft(xn)
        if ftxn == 0:
            return None
        xn = xn - fxn/ftxn
    return None

def secant(f,a,b):
    """
    secant
    """
    if f(a) * f(b) >= 0:
        print("Secant method failed.\n")
        return None
    a_n = a
    b_n = b
    for n in range(1, 500):
        m_n = a_n - f(a_n) * (b_n - a_n) / (f(b_n) - f(a_n))
        f_m_n = f(m_n)
        if f(a_n) * f_m_n < 0:
            a_n = a_n
            b_n = m_n
        elif f(b_n) * f_m_n < 0:
            a_n = m_n
            b_n = b_n
        elif f_m_n == 0:
            print(n, "Iterations, x=", round(m_n, 4))
            return round(m_n, 4)
        else:
            return None
    return a_n - f(a_n) * (b_n - a_n) / (f(b_n) - f(a_n))



# main:

"""
Input instruction:
Entering a polynom should be in the format of: " 3*x**2+4*x+5 "
(without the quotation mark)
"""
x =sp.symbols('x')
str_f=input("Enter a polynom: ")
print("Enter a range: ")
a=float(input())
b=float(input())
option=int(input("Choose:\n(0)-Newton Rapson\n(1)-Secant\n")) ##### enter 0 or 1
str_ft=sp.diff(str_f,x)
f=sp.lambdify(x,str_f)  # our function
ft=sp.lambdify(x,str_ft)  # our nigzeret
if option == 0:
    newtonraph(f, ft, a, b)
else:
    if option == 1:
        secant(f, a, b)
    else:
        print("Wrong option input.\n")

