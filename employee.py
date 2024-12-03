class Employee:
    def __init__(self, fullname: str, email: str, firstname: str):
        self.__fullname = fullname
        self.__email = email
        self.__firstname = firstname

    def get_fullname(self):
        return self.__fullname
        
    def get_email(self):
        return self.__email
        
    def get_firstname(self):
        return self.__firstname

    def set_fullname(self, new_fullname):
        self.__fullname = new_fullname

    def set_email(self, new_email):
        self.__email = new_email

    def set_firstname(self, new_firstname):
        self.__firstname = new_firstname

emp_1 = Employee("John Smith", "john.smith@company.com", "John")
emp_2 = Employee("Mary Sue", "mary.sue@company.com", "Mary")             
emp_3 = Employee("Antony Walker", "antony.walker@company.com", "Antony")
