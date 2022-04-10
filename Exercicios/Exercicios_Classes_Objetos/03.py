'''
Crie uma classe Funcionario cujos atributos são nome e e-mail. Guarde as horas trabalhadas 
em um dicionário cujas chaves são o mês em questão e, em outro dicionário, guarde o salário
por hora relativo ao mês em questão. Crie um método que retorna o salário mensal do funcionário.

'''

class Funcionario:

    def __init__(self, nome, email):

        self.nome = nome
        self.email = email
        self.horas_trabaladas = {}
        self.salario_hora = {}

    def horasTrabalhadas(self, mes, qtd_horas):
        self.horas_trabaladas = {mes:qtd_horas}

    def salarioHora(self, mes, salarioHora):
        self.salario_hora = {mes:salarioHora}

    def salarioMensal(self):
         return self.horas_trabaladas['JAN/21'] * self.salario_hora['JAN/21']



    
func1 = Funcionario('Wangles', 'teste@teste.com')

func1.horasTrabalhadas('JAN/21', 50)

func1.salarioHora('JAN/21', 10)

print(func1.salarioMensal())

