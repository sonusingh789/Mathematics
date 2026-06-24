import sympy as sp

x = sp.Symbol('x')
f = x**2
derivative = sp.diff(f,x)
print("Derivative: ",derivative)


x=sp.Symbol('x')
f= sp.sin(x)
derivative2 = sp.diff(f,x)
print(derivative2)

# Partial Derivative and Gradient

x ,y = sp.symbols('x y')
f = x**2  + y**2
gradient_x = sp.diff(f,x)
gradient_y = sp.diff(f,y)
print("Partial Derivatives : ",gradient_x,gradient_y)

# computing gradients

x,y = sp.symbols('x y')
f = x**2 + 3*y**2-4*x*y
