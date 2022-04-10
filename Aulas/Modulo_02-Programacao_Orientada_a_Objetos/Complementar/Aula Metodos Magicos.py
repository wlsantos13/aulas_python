# Métodos Mágicos (Métodos dunder) - Métodos especiais


x = 2

y = 3

print(x.__add__(y))


# __repr__ : método de representação (eu quero algo esqpecífico no print)

# Classe de cadastro : me retornar na tela o nome e o e-mail de um usuário(persolinalizada)

class Cadastro:

    def __init__(self, nome, email):

        self.nome = nome
        self.email = email

    def __repr__(self):

        return f'O usuario {self.nome} tem email : {self.email}'

usuario1 = Cadastro('Matheus','matheus@email.com')

#print(usuario1)


# __len__: vai retornar a quantidade total



class BancoDeDados:

    def __init__ (self, nome, email):
        self.nome = nome
        self.email = email

    def __repr__(self):
        return f'O usuario {self.nome} tem email : {self.email}'

class ListaDoBanco:

    def __init__(self):
        self.usuarios = []

    def mostrar_usuario(self):

        for usuario in self.usuarios:
            print(usuario)

    def __len__(self):

        return len(self.usuarios)

    def __add__(self, usuario):

        self.usuarios.append(usuario)

        return self

    def __getitem__(self, index):

        return self.usuarios[index]

usuarios = ListaDoBanco()

user1 = BancoDeDados('Paulo', 'paulo@paulo.com')
user2 = BancoDeDados('Matheus','matheus@matheus.com')

usuarios = usuarios + user1
usuarios = usuarios + user2

print(len(usuarios))
print(list(usuarios))
usuarios.mostrar_usuario()


