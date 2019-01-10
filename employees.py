class Company(object):
    """This represents a company in which people work"""

    def __init__(self, company_name, date_founded):
        self.company_name = company_name
        self.date_founded = date_founded
        self.employees = []

    def get_company_name(self):
        """Returns the name of the company"""

        return self.company_name

    def create_employee(self, employee_name, job_title, start_date):
        """Adds a new employee to the list of employee dictionaries with their name, title and start date"""

        self.employees.append({
          "employee_name": employee_name,
          "job_title": job_title,
          "start_date": start_date
        })

    def get_employee_title(self, employee_name):
      """Looks up an employee in the employee list by name and returns their title"""

      for employee in self.employees:
        if employee["employee_name"] == employee_name:
          return employee["job_title"]

    def get_employee_start_date(self, employee_name):
      """Looks up an employee in the employee list by name and returns their start date"""

      for employee in self.employees:
        if employee["employee_name"] == employee_name:
          return employee["start_date"]

    def __str__(self):
      return f"Company name {self.company_name}, date founded {self.date_founded}. They employee the following people {self.employees}"



nss = Company("NSS", "2012")

nss.create_employee("jessica", "student", "10-01-2018")
# print(nss)

print(nss.get_employee_title("jessica"))
print(nss.get_employee_start_date("jessica"))

