import numpy as np
import pandas as pd
from tabulate import tabulate
from sympy import *
from sympy import Symbol, Eq, solve

x = Symbol('x')
original_expr = input("Please enter an equation: ")

first_expr = str(factor(diff(original_expr)))
second_expr = str(factor(diff(first_expr)))
print(f"dy/dx = {first_expr}.")
print(f"d^2y/dx^2 = {second_expr}.")


def get_roots(equation):
    roots = solve(equation, dict=false)
    roots.sort()
    return roots


def get_stationery_points(equation, roots):
    for i in range(0, len(roots)):
        print(f"It has stationery points at ({roots[i]},{eval(equation).subs(x, roots[i])}).")
    print("\n")


def make_slopes_table(first_derivative, roots):
    x_values = [i for i in range(int(roots[0]) - 1, int(roots[-1]) + 2)]
    corresponding = [eval(first_derivative).subs(x,x_values[i]) for i in range(0,len(x_values))]
    slope = []
    for i in range(0, len(corresponding)):
        if corresponding[i] > 0:
            slope.append("/")
        elif corresponding[i] == 0:
            slope.append("-")
        elif corresponding[i] < 0:
            slope.append("\\")

    data = {"x-value": x_values,
            "f'(x)": corresponding,
            "slope": slope
            }
    df = pd.DataFrame(data)
    print(df)


def make_concavity_table(second_derivative, roots):
    x_values = [i for i in range(int(roots[0]) - 1, int(roots[-1]) + 2)]
    corresponding = [eval(second_derivative).subs(x,x_values[i]) for i in range(0,len(x_values))]
    concavity = []
    for i in range(0, len(corresponding)):
        if corresponding[i] > 0:
            concavity.append("∪")
        elif corresponding[i] == 0:
            concavity.append("•")
        elif corresponding[i] < 0:
            concavity.append("∩")

    data = {"x-value": x_values,
            "f\"(x)": corresponding,
            "concavity": concavity,

            }
    df = pd.DataFrame(data)
    print(df)


get_stationery_points(original_expr, get_roots(original_expr))
make_slopes_table(first_expr, get_roots(original_expr))
make_concavity_table(second_expr, get_roots(original_expr))
