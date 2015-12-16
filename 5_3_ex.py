# -*- coding:Utf-8 -*-
'''conversion degrés celsius à degrés fahrenheit'''

degrés_celsius = float(input("Degrés Celsius à convertir en degré Fahrenheit?\
\n>>>"))
degrés_fahrenheit = degrés_celsius * 1.8 + 32

print(degrés_celsius, "degrés celsius correspondent à", degrés_fahrenheit,
      "degrés fahrenheit.")

degrés_fahrenheit = float(input("Degrés Fahrenheit à convertir en degré Celsius ?\
\n>>>"))
degrés_celsius = (degrés_fahrenheit - 32) / 1.8

print(degrés_fahrenheit, "degrés fahrenheit correspondent à", round(degrés_celsius,2),
      "degrés celsius.")
