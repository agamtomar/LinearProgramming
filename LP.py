

import cvxpy as cvx


# ECE 236A Class Notes Programs

# Page 3

X = cvx.Variable(shape=(2,1))

Objective = cvx.Maximize(10*X[0] - X[1])

Constraints = [X[0] >= 100,
               X[0] <= 400,
               X[1] >= 100,
               X[1] <= 300,
               X[0]+X[1] >= 250,
               X[0] >= 0, X[1] >= 0]

Problem = cvx.Problem(objective=Objective, constraints=Constraints)

result = Problem.solve()
