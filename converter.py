# converter.py

def fahrenheit_from(celsius):
    """Convert Celsius to Fahrenheit degrees."""
    try:
        fahrenheit = float(celsius) * 9 / 5 + 32
        fahrenheit = round(fahrenheit, 3)
        return str(fahrenheit)
    except ValueError:
        return "invalid input"

if __name__ == "__main__":
    celsius = input("Celsius: ")
    print("Fahrenheit:", fahrenheit_from(celsius))

