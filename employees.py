class Company(object):
    """This represents a company in which people work"""

    def __init__(self, company_name, date_founded):
        self.company_name = company_name
        self.date_founded = date_founded
        self.employees = []

    def get_company_name(self):
        """Returns the name of the company"""

        return self.company_name

    # def create_employee(self, employee_name, job_title, start_date):
    #     """Adds a new employee to the list of employee dictionaries with their name, title and start date"""

    #     self.employees.append({
    #       "employee_name": employee_name,
    #       "job_title": job_title,
    #       "start_date": start_date
    #     })

    def add_employee(self, employee_obj, title, start_date):
      """Adds a new employee to the list of employee dictionaries with their social, firstname and lastname passed in as an object and their title and start date"""

      self.employees.append({
        "social": employee_obj.social,
        "first_name": employee_obj.first_name,
        "last_name": employee_obj.last_name,
        "title": title,
        "start_date": start_date
      })

    # def get_employee_title(self, employee_name):
    #   """Looks up an employee in the employee list by name and returns their title"""

    #   for employee in self.employees:
    #     if employee["employee_name"] == employee_name:
    #       return employee["job_title"]

    # def get_employee_start_date(self, employee_name):
    #   """Looks up an employee in the employee list by name and returns their start date"""

    #   for employee in self.employees:
    #     if employee["employee_name"] == employee_name:
    #       return employee["start_date"]

    def __str__(self):
      return f"These people work at NSS {self.employees}"

# ***********
nss = Company("NSS", "2012")

# ********
class Employee:
  """This represents a worker, unassociated with any particular company"""
  def __init__(self, social, first_name, last_name):
    self.social = social
    self.first_name = first_name
    self.last_name = last_name

  def __str__(self):
    return f"frist name: {self.first_name}, last name: {self.last_name}, social: {self.social}"

jessica = Employee(1111111, "jessica", "barnett")

nss.add_employee(jessica, "student", "10-01-2018")

print(nss.employees)