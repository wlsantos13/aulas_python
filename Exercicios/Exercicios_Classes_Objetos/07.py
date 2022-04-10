'''
Crie uma modelagem de classes para uma agenda capaz de armazenar contatos.
 Através dessa agenda é possível incluir, remover, buscar e listar contatos já cadastrados.
'''

class Contato:

    def __init__(self, nome, email, telefone):
        self.nome = nome
        self.email = email
        self.telefone = telefone

class Agenda:

    def __init__(self):
        self.Contatos = []

    def adicionarContato(self, Contato):
        self.Contatos.append({
            'Nome': Contato.nome,
            'Email': Contato.email,
            'Telefone': Contato.telefone
        })

    def removeContatos(self, nome):
        for contato in self.Contatos:
            if contato['Nome'] == nome:
                self.Contatos.remove(contato)

    def buscarContatos(self, nome):
        for contato in self.Contatos:
            if contato['Nome'] == nome:
                print(contato)
            else:
                print('Contato informado nao existe na Agenda')

    def listarContatos(self):
        for contato in self.Contatos:
            print(contato)


contato1 =Contato('wangles', 'teste@teste.com', '32323224')
contato2 = Contato('Luan', 'luan@teste.com', '55553333')
contato3 = Contato('Lucia', 'Lucia@email.com', '45527777')

agenda1 = Agenda()

agenda1.adicionarContato(contato1)

print(agenda1.Contatos)

agenda1.adicionarContato(contato2)

print(agenda1.Contatos)

agenda1.removeContatos('Luan')

print(agenda1.Contatos)

agenda1.buscarContatos('wangles')

agenda1.adicionarContato(contato3)

agenda1.listarContatos()



