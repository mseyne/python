# -*- coding: utf-8 -*-
# Python Hardway, Exercice 28, Boolean Practice
# ex28.py
# This script just do some boolean examples

print("True and True =", True and True) # True
print("False and True =", False and True) # False
print("1 == 1 and 2 == 1 =", 1 == 1 and 2 == 1) # False
print('"test" == "test" =', "test" == "test") # True
print("1 == 1 or 2 != 1 =", 1 == 1 or 2 != 1) # True
print("True and 1 == 1 =", True and 1 == 1) # True
print("False and 0 != 0 =", False and 0 != 0) # False
print("True or 1 == 1 =", True or 1 == 1) # True
print('"test" == "testing" =', "test" == "testing") # False
print("1 != 0 and 2 == 1 =", 1 != 0 and 2 == 1) # False
print('"test" != "testing" =', "test" != "testing") # True
print('"test" == 1 =', "test" == 1) # False
print("not (True and False) =", not (True and False)) # True
print("not (1 == 1 and 0 != 1) =", not (1 == 1 and 0 != 1)) # False
print("not (10 == 1 or 1000 == 1000) =", not (10 == 1 or 1000 == 1000)) # False
print("not (1 != 10 or 3 == 4) =", not (1 != 10 or 3 == 4)) # False
print('not ("testing" == "testing" and "Zed" == "Cool Guy") =',
      not ("testing" == "testing" and "Zed" == "Cool Guy")) # True
print('1 == 1 and not ("testing" == 1 or 1 == 0) =',
      1 == 1 and not ("testing" == 1 or 1 == 0)) # True
print('"chunky" == "bacon" and not (3 == 4 or 3 == 3) =',
      "chunky" == "bacon" and not (3 == 4 or 3 == 3)) # False
print('3 == 3 and not ("testing" == "testing" or "Python" == "Fun") =',
      3 == 3 and not ("testing" == "testing" or "Python" == "Fun")) # False
