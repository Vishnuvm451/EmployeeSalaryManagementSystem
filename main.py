from Employee import Employee
from PermanentEmployee import PermanentEmployee
from ContractEmployee import ContractEmployee

permanent = PermanentEmployee('Vishnu',20000)
contract = ContractEmployee('Jishnu',30000)


print(' ')
print('--- PermanentEmployee ---\n')

permanent.display_details()
permanent.calculate_salary(20)

print(' ')

print('--- ContractEmployee ---\n')

contract.display_details()
contract.calculate_salary(5)

print(' ')

