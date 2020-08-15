#Temperature convertion application

print("Welcome to Temperature Conversion Application")
print()
tempf = float(input("Enter temperture in Fahrenheit : "))
print()
#calculate celsius value
tempc = (tempf - 32 ) * (5 / 9)
#calculating kelvin temp
tempk = ((tempf - 32) * (5 / 9)) + 273.15
print("############################################")
print()
#print Fahrenheit value
print("Fahrenheit temperature : ", round(tempf, 2))
#print celsius value
print("Celsius Temperature : ", round(tempc, 2))
#print kelvin value
print("Kelvin Temperature : ", round(tempk, 2))
print()
print("###########################################")
