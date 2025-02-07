def fahrenheit_to_celsius(fahrenheit):
  return (5/9) * (fahrenheit-32)

temp = float(input("Enter temperature in Fahrenheit: "))
print("Temperature in Celsius: " + str(fahrenheit_to_celsius(temp)))
