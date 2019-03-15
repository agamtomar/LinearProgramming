

import cvxpy as cvx
import numpy as np

# ECE 236A Class Notes Programs

########################################################################################################################
########################################### Page 3 #####################################################################
########################################################################################################################

X = cvx.Variable(shape=(2,1))
c = np.array([10, -1]).reshape(-1, 1)

# Objective = cvx.Maximize(10*X[0] - X[1])
Objective = cvx.Maximize(c.T*X)

Constraints = [X[0] >= 100,
               X[0] <= 400,
               X[1] >= 100,
               X[1] <= 300,
               X[0] + X[1] >= 250,
               X[0] >= 0, X[1] >= 0]

Problem = cvx.Problem(objective=Objective, constraints=Constraints)

result = Problem.solve()
print(X.value)

########################################################################################################################
########################################### Page 52 ####################################################################
########################################################################################################################

x = cvx.Variable(shape=(1))
y = cvx.Variable(shape=(1))

Objective = cvx.Maximize(3*x+y)

Constraints = [x+y <= 4,
               x+2*y <= 6,
               x>=0, y>=0]

Problem = cvx.Problem(objective=Objective, constraints=Constraints)

result = Problem.solve()

print(x.value, y.value)


########################################################################################################################
########################################### Integer Programming ########################################################
########################################################################################################################

# Usual Approach
X = cvx.Variable(shape=(4, 1))
A = np.array([8, 11, 6, 4])
c = np.array([5, 7, 4, 3])

Objective = cvx.Maximize(A*X)

Constraints = [c*X <= 14, X >=0, X <= 1]

Problem = cvx.Problem(Objective, Constraints)

result = Problem.solve()

print(result, X.value)

# To get Integral Answers
X = cvx.Variable(shape=(4, 1), boolean=True)
A = np.array([8, 11, 6, 4])
c = np.array([5, 7, 4, 3])

Objective = cvx.Maximize(A*X)

Constraints = [c*X <= 14]

Problem = cvx.Problem(Objective, Constraints)

result = Problem.solve()

print(result, X.value)
