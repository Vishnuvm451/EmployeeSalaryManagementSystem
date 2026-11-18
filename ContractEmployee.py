from Employee import Employee


class ContractEmployee(Employee):

    def calculate_salary(self,interest):
        interest_amt = self.salary + self.salary * (interest/100)
        print(f'Salary with allowance {interest} % : {interest_amt}')