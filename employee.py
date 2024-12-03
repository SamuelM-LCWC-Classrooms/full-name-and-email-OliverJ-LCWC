class Employee:
    def __init__(self, firstname, lastname) -> None:
        self._firstname = firstname
        self.lastname = lastname
        self.email = f"{firstname}.{lastname}@company.com"
        self.fullname = f"{firstname} {lastname}"


