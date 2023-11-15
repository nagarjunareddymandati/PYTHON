def celsius_to_fahrenheit(c):
    return (c/5) * 9 + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

try:
    while True:
        user_input = input("Enter temperature value with scale (C or F): ")
        user_scale = input("Enter temperature scale (C or F): ").upper()
        user_value = float(user_input)

        if user_scale == 'C':
            print("Temperature in Fahrenheit: ", celsius_to_fahrenheit(user_value))
        elif user_scale == 'F':
            print("Temperature in Celsius: ", fahrenheit_to_celsius(user_value))
        else:
            print("Invalid scale entered. Please enter C or F.")
except ValueError as ve:
 print("Please enter a valid number")
except Exception as e:
    print("An error occurred:", str(e))

