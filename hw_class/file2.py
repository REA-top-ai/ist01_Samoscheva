from abc import ABC, abstractmethod

#
class Employee():
    new_id = 1

    def __init__(self):
        self.id = Employee.new_id
        Employee.new_id += 1

    def say_id(self):
        print(f'My ID is {self.id}')

e1 = Employee()
e2 = Employee()
print(e1.say_id(), e2.say_id())

#
class User:
    def __init__(self, id, role):
        self.id = id
        self.role = role

    def say_user_info(self):
        print(f"User id: {self.id}, role: {self.role}")

#
class Admin(Employee, User):

    def __init__(self):
        Employee.__init__(self)
        User.__init__(self, self.id, "Admin")

    def say_id(self):
        print("I am an Admin")
        super().say_id()
e3 = Admin()
print(e3.say_user_info())

#
class Manager(Admin):

    def say_id(self):
        super().say_id()

e4 = Manager()
print(e4.say_id())

#
meeting = [Employee(), Admin(), Manager()]
for ID in meeting:
    print(ID.say_id())

#
class Meeting:

    def __init__(self):
        self.attendees = []

    def __add__(self, employee):
        self.attendees.append(employee)
        return self

    def __len__(self):
        return len(self.attendees)

e1 = Employee()
e2 = Employee()
e3 = Employee()

m1 = Meeting()
m1 = m1 + e1
m1 = m1 + e2
m1 = m1 + e3

print(len(m1))

#
class AbstractEmployee(ABC):
    new_id = 1

    def __init__(self):
        self.id = AbstractEmployee.new_id
        AbstractEmployee.new_id += 1

    @abstractmethod
    def say_id(self):
        pass

class Employee(AbstractEmployee):
    def say_id(self):
        print(f"My ID is {self.id}")

e1 = Employee()
print(e1.say_id())

#
class Employee:
    def __init__(self):
        self.id = 1
        self._id = 2
        self.__id = 3

e = Employee()
print(dir(e))

#
class Employee:
    def __init__(self):
        self._name = None

    def get_name(self):
        return self._name

    def set_name(self, _name):
        self._name = _name

    def delete_name(self):
        del self._name
        print('name deleted')

e = Employee()
e.set_name("Alice")
print(e.get_name())






