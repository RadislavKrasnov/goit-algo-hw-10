import pulp

# Initialize model
model = pulp.LpProblem('Maximize products quantity', pulp.LpMaximize)

# Create variables
x = pulp.LpVariable('X', lowBound=0, cat='Integer') # Limonade
y = pulp.LpVariable('Y', lowBound=0, cat='cat') # Friut Juice

# Objective function (Maximizing products quantity)
model += x + y

# Constraints
model += 2 * x + y <= 100 # Water
model += x <= 50 # Sugar
model += x <= 30 # Lemon juice
model += 2 * y <= 40 # Fruit puree

# Solve the model
model.solve()

# Output of results
print(f'Status: {pulp.LpStatus[model.status]}')
print(f'Limonade quantity: {x.varValue}') # 30.0
print(f'Fruit Juice: {y.varValue}') # 20.0
print(f'Total optimal quantity of Limonade and Fruit Juice: {pulp.value(model.objective)}') # 50.0
