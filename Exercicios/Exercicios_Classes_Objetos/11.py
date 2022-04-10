'''
Crie uma classe Fração cujos atributos são numerador (número de cima) e denominador (número de baixo).

Implemente os métodos de adição, subtração, multiplicação, divisão que retornam objetos do tipo Fração.

Implemente também o método _ repr _.

Implemente métodos para comparação: igualdade (==) e desigualdades (!=, <=, >=, < e >).
'''

class Fracao:

    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    def __repr__(self):
        return f'{self.numerador}/{self.denominador}'

class Calculo:

    def soma(Fracao1, Fracao2):
        resultado = None
        numeradorfinal1 = None
        numeradorfinal2 = None
        denominadorfinal = None
        if Fracao1.denominador == Fracao2.denominador:
            resultado = Fracao((Fracao1.numerador + Fracao2.numerador), Fracao1.denominador)
    
        else: 
            if Calculo.multiplo(Fracao1.denominador, Fracao2.denominador) == True and Fracao1.denominador > Fracao2.denominador:
                denominadorfinal = Fracao1.denominador
            elif Calculo.multiplo(Fracao1.denominador, Fracao2.denominador) == True and Fracao2.denominador < Fracao1.denominador:
                denominadorfinal = Fracao2.denominador
            else:
                denominadorfinal = Fracao1.denominador * Fracao2.denominador
            
            numeradorfinal1 = denominadorfinal / Fracao1.denominador * Fracao1.numerador
            numeradorfinal2 = denominadorfinal / Fracao2.denominador * Fracao2.numerador
            resultado = Fracao(int(numeradorfinal1 + numeradorfinal2),denominadorfinal) 
        return resultado

    def soma2(Fracao1, Fracao2):

        resultado = Fracao((Fracao1.numerador * Fracao2.denominador) + (Fracao1.denominador * Fracao2.numerador), (Fracao1.denominador * Fracao2.denominador))

        return resultado

    def subtracao(Fracao1, Fracao2):
        resultado = None
        numeradorfinal1 = None
        numeradorfinal2 = None
        denominadorfinal = None
        if Fracao1.denominador == Fracao2.denominador:
            resultado = Fracao((Fracao1.numerador + Fracao2.numerador), Fracao1.denominador)
    
        else: 
            if Calculo.multiplo(Fracao1.denominador, Fracao2.denominador) == True and Fracao1.denominador > Fracao2.denominador:
                denominadorfinal = Fracao1.denominador
            elif Calculo.multiplo(Fracao1.denominador, Fracao2.denominador) == True and Fracao2.denominador < Fracao1.denominador:
                denominadorfinal = Fracao2.denominador
            else:
                denominadorfinal = Fracao1.denominador * Fracao2.denominador
            
            numeradorfinal1 = denominadorfinal / Fracao1.denominador * Fracao1.numerador
            numeradorfinal2 = denominadorfinal / Fracao2.denominador * Fracao2.numerador
            resultado = Fracao(int(numeradorfinal1 - numeradorfinal2),denominadorfinal) 
        return resultado

    def multiplicacao(Fracao1, Fracao2):
        numerador = Fracao1.numerador * Fracao2.numerador
        denominador = Fracao1.denominador * Fracao2.denominador
        return Fracao(numerador, denominador)

    def divisao(Fracao1, Fracao2):
        numerador = Fracao1.numerador * Fracao2.denominador
        denominador = Fracao1.denominador * Fracao2.numerador
        return Fracao(numerador, denominador)


    def multiplo(numero, numero2):
        maior = None
        if numero < numero2:
           return (numero2%numero == 0)
        else:
            return (numero%numero2 == 0)

    def igualdade(Fracao1, Fracao2):
        if Fracao1.numerador / Fracao1.denominador == Fracao2.numerador / Fracao2.denominador:
            print('As Frações são iguais')
        elif Fracao1.numerador / Fracao1.denominador < Fracao2.numerador / Fracao2.denominador:
            print('As Fracao2 é maior que a Fracao1')
        else:
            print('As Fracao1 é maior que a Fracao2')





fr1 = Fracao(7,16)
fr2 = Fracao(5,32)
fr3 = Calculo.soma(fr1, fr2)
fr7 = Calculo.soma2(fr1, fr2)
fr4 = Calculo.subtracao(fr1, fr2)
fr5 = Calculo.multiplicacao(fr1, fr2)
fr6 = Calculo.divisao(fr1, fr2)
print(fr3)
print(fr7)
print(fr4)
print(fr5)
print(fr6)
Calculo.igualdade(fr1, fr2)

        
