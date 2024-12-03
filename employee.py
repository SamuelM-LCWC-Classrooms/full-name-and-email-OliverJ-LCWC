class Employee:
    def __init__(self, firstname, lastname) -> None:
        self.__firstname = firstname
        self.__lastname = lastname
        self.__email = f"{firstname}.{lastname}@company.com"
        fullname = f"{firstname} {lastname}"


