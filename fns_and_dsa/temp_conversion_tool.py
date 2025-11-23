FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return fahrenheit * FAHRENHEIT_TO_CELSIUS_FACTOR
def convert_to_fahrenheit(celsius):
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR

temp = int(input("Enter the temperature to convert: "))
unit = chr(input("Is this temperature in Celsius or Fahrenheit? (C/F): ")).upper
if unit == 'F':
    converted_temp = convert_to_celsius(temp)
    print(f"{temp}°F is {converted_temp}°C")
elif unit == 'C':
    converted_temp = convert_to_fahrenheit(temp)
    print(f"{temp}°C is {converted_temp}°F")