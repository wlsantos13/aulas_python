'''
Faça um programa que peça a temperatura em graus Fahrenheit (F), transforme e mostre a temperatura em graus Celsius (°C).

°C = (5 * (F-32) / 9)

℉ =℃ * 1.8000+ 32.00

Obs: Tente também fazer um programa que faça o inverso: peça a temperatura em graus Celsius e a transforme em graus Fahrenheit.

'''


tempF = float(input('Digite a temperatura em (F) que deseja converter para (C):'))

TempC = round((5 * (tempF - 32 ) / 9),2)

print('A temperatura em F° informada corresponde em C° a', TempC, 'graus.'  )

tempC = float(input('Digite a temperatura em (C) que deseja converter para (F):'))


TempF = tempC * 1.8000 + 32.00

print('A temperatura em C° informada corresponde em F° a', TempF, 'graus.'  )
