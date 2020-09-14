#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math


def average(a: float, b: float, c: float) -> float:
    return (a + b + c) / 3


def to_radians(angle_degs: float, angle_mins: float, angle_secs: float) -> float:
    return 0.0


def to_degrees(angle_rads: float) -> tuple:
    degree = math.degrees(angle_rads) # change the radian angle to degree first
    whole_number ,decimal_number = divmod((degree),1) # whole_number represents the degrees (la partie entiere)
    minutes, decimal_sec = divmod((decimal_number * 60), 1) # min = la partie decimale de 'degree' * 60
    seconds, decimal = divmod((decimal_sec * 60) , 1)  # sec = la partie decimale des 'minutes' * 60
    return whole_number, minutes, seconds


def to_celsius(temperature: float) -> float:
    try :
        if temperature < -459.67 :
            raise ValueError("Cette tempertaure en Celsius est inferieure au minimum '-459.67' qui se trouve sur l'echelle.\n")
    except ValueError : 
        print("Valeur ")
    return 0.0


def to_farenheit(temperature: float) -> float:
    try :
        if temperature < -273.15 :
            raise ValueError("Cette tempertaure en Celsius est inferieure au minimum '-273.15' qui se trouve sur l'echelle.\n")
    except ValueError :
        print("Valeur invalide.\n")
        return 1
    fahrenheit = 1.8 * temperature + 32
    return fahrenheit


def main() -> None:
    print(f"Moyenne des nombres 2, 4, 6: {average(2.1, 4.3, 6.5)}")

    print(f"Conversion de 100 degres, 2 minutes et 45 secondes en radians: {to_radians(180, 2, 45)}")
    
    degrees, minutes, seconds = to_degrees(1.0)
    print(f"Conversion de 1 radian en degres: {degrees} degres, {minutes} minutes et {seconds} secondes")

    print(f"Conversion de 100 Celsius en Farenheit: {to_farenheit(100.0)}")
    print(f"Conversion de 451 Farenheit en Celsius: {to_celsius(451.0)}")


if __name__ == '__main__':
    main()
