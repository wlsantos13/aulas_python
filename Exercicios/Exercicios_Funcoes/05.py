'''
Faça uma função que recebe um nome e um horário e imprime “Bom dia, [nome]”, caso seja antes de 12h, 
“Boa Tarde, [nome]”, caso seja entre 12h e 18h e “Boa noite, [nome]” se for após às 18h.

'''

def cumprimento(horario):
    if horario < 12:
        print('Bom dia')
    elif horario > 12 and horario < 18:
        print('Boa Tarde')
    else:
        print('Boa Noite')


        