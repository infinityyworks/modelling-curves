# Modelling curves using logarithms
A script to model the relationship between bivariate data. Currently approximates exponential relationships in the form y = kb<sup>x</sup>, and polynomial relationships in the form y = ax<sup>n</sup>.
## Entering data
1. Enter the names of the indepdendent and dependent variable, separated with a space between them.
2. Enter the dataset for the independent variable, separating each number by a space.
3. Enter the dataset for the dependent variable, again separating each data item using a space.
## Output
The program will propose two possible relationships in the forms y = kb<sup>x</sup> and y = ax<sup>n</sup>. For each one, it will show the Pearson's correlation coefficient for:
- The linear regression line between the logarithm of the dependent dataset against the independent dataset (exponential relationship)
- The linear regression line between the logarithms of each dataset against each other (polynomial relationship)
<br>
This allows you to easily compare the accuracy of each model.
<br>
The equations themselves will be given in terms of the independent and dependent variable names, with the constants rounded to 2 decimal places, and the correlation coefficient rounded to 4 decimal places.
