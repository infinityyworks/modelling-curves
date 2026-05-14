import numpy as np
from scipy.stats import linregress
from math import exp

independentVar, dependentVar = input('Independent and dependent variable names: ').split()
independent = np.array(list(map(float, input(f'Dataset for {independentVar}: ').split())))
dependent = np.array(list(map(float, input(f'Dataset for {dependentVar}: ').split())))

ln_independent = np.log(independent)
ln_dependent = np.log(dependent)

# for linear relationship in form y = m*x + c
linear = linregress(independent, dependent)
m = linear.slope
c = linear.intercept
print(f'\nFor a linear relationship in the form {dependentVar} = m*{independentVar} + c:')
print(f'Pearson correlation coefficient: {linear.rvalue:.4f}')
print(f'Equation: {dependentVar} = {m:.2f} * {independentVar} + {c:.2f}')

# for exponential relationship in form y = k*b^x
exponential = linregress(independent, ln_dependent)
k = exp(exponential.intercept)
b = exp(exponential.slope)
print(f'\nFor a exponential relationship in the form {dependentVar} = k*b^{independentVar}:')
print(f'Pearson correlation coefficient: {exponential.rvalue:.4f}')
print(f'Equation: {dependentVar} = {k:.2f} * {b:.2f}^{independentVar}')

# for power relationship in form y = a*x^n
power = linregress(ln_independent, ln_dependent)
a = exp(power.intercept)
n = power.slope
print(f'\nFor a power relationship in the form {dependentVar} = a*{independentVar}^n:')
print(f'Pearson correlation coefficient: {power.rvalue:.4f}')
print(f'Equation: {dependentVar} = {a:.2f} * {independentVar}^{n:.2f}')
