"""
Diet problem, solved with Mathematical Optimization 
Project: CROSMO
Team: Filo-Space
"""

#Importing libraries (Pandas to work with data, and PuLP for optimization)
import pandas as pd
from pulp import *

#Reading data. 
#We first read data of nutrients per vegetable, the optimal nutrient intake, the tolerable nutrient intake, and the weight
#of every vegetable we study (cabbage, mustard, lettuce).
nutrients_per_vegetable = pd.read_excel('vitamin_minerals.xlsx',sheet_name='nutrients_per_vegetable',usecols=[1,2,3])
optimal_nutrient_requirement = pd.read_excel('vitamin_minerals.xlsx',sheet_name='optimal_nutrient_requirement',usecols=[1,2,3])
tolerable_nutrient_requirement = pd.read_excel('vitamin_minerals.xlsx',sheet_name='tolerable_nutrient_requirement',usecols=[1,2,3])
weight_per_vegetable = pd.read_excel('vitamin_minerals.xlsx',sheet_name='weight_per_vegetable',usecols=[1])

#Number of crops and number of nutrients that we will consider:
n_rows,n_columns=nutrients_per_vegetable.shape

#We transform the nutrients dataframe to a list. This is done to work with the data
nutrients_per_vegetable=nutrients_per_vegetable.values.tolist()
optimal_nutrient_requirement=optimal_nutrient_requirement.values.tolist()
tolerable_nutrient_requirement=tolerable_nutrient_requirement.values.tolist()
weight_per_vegetable=weight_per_vegetable.values

#We define the Linear Optimization Problem
prob = LpProblem("diet",LpMaximize)

#Next, we define the variable X_i. This represents the weight in grams that a crew member has to eat daily of vegetable i.
#Where i={lettuce, cabbage, mustard}
X = {}
for i in range(n_rows):
	X[i] = LpVariable(f'x_{i}',lowBound=0, cat='Continuous')

#We minimize the total weight of crops
prob += lpSum([-weight_per_vegetable[i]*X[i] for i in range(n_rows)]) , "F.O" 

#The diet should have equal or more nutrients than the optimal
for j in range(n_columns):
	prob += lpSum([nutrients_per_vegetable[i][j]*X[i] for i in range(n_rows)])>=optimal_nutrient_requirement[0][j], "r1_%s"%j

#The diet should not have more nutrients than what is recommended
for j in range(n_columns):
	if tolerable_nutrient_requirement[0][j] != "ND":
		prob += lpSum([nutrients_per_vegetable[i][j]*X[i] for i in range(n_rows)])<=tolerable_nutrient_requirement[0][j], "r2_%s"%j #numero minimo de grupo por dia

#We want the diet to have, at most, 1.5 units of every kind of vegetable per day. We are looking to have a diverse diet.
for i in range(n_rows):
	prob += X[i] <= 1.5*weight_per_vegetable[i][0], "r3_%s"%i #

#We solve the linear problem
prob.solve()

#We show the results
vegetables=["red romaine lettuce","chinese cabbage","mizuna mustard"]
for i in range(n_rows):
    if round(X[i].varValue) >0:
        print("Every crew member should eat {0} grams of {1} per day, which is {2} of a unit".format(X[i].varValue,vegetables[i], X[i].varValue/weight_per_vegetable[i]))

prob.writeLP("Mathematical_model.lp")