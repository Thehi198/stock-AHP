# initialize variables and lists to store data from user input 
numComp = int(input('Enter number of companies: '))
numParam = int(input('Enter number of parameters: '))
parameters = []
comparisons = []

for i in range(1, numParam+1):
    parameters.append(input(f'Enter parameter {i}: '))

for i in range(1, numComp+1):
    comparisons.append(input(f'Enter comparison for company {i}: '))

print(parameters)
print(comparisons)
