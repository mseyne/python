class Person:
  def __init__(self, first, middle, last, age):
    self.first = first = first;
    self.middle = middle;
    self.last = last;
    self.age = age;
  
  def __str__(self):
    return self.first + ' ' + self.middle + ' ' + self.last + \
           ' ' + str(self.age)

  def initials(self):
    return self.first[0] + self.middle[0] + self.last[0]

  def changeAge(self, amount):
    self.age += amount


aPerson = Person('Jane', 'Q', 'Public', 27)
print(aPerson)
aPerson.changeAge(2)
print(aPerson)
print(aPerson.initials())
