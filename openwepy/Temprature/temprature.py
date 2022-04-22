class temprature:
    def celcius_to_fahrenheit(celcius):
        formula = (celcius * 9/5) + 32
        return formula

    def fahrenheit_to_celcius(fahrenheit):
        formula = (fahrenheit - 32) * 5/9
        return formula

    def kelvin_to_fahrenheit(kelvin):
        formula = ((kelvin - 273.15) * 9/5) + 32
        return formula

    def kelvin_to_celcius(kelvin):
        fahrenheit = temprature.kelvin_to_fahrenheit(kelvin)
        formula = temprature.fahrenheit_to_celcius(fahrenheit)
        return formula