class cliente:

    def __init__(self,nome,idade,sexo,email,telefone,endereco):
        self.nome = nome.title()
        self.idade = idade
        self.sexo = sexo
        self.email = email
        self.telefone = telefone
        self.endereco = endereco.title()

    def __str__(self):
        return (f"nome: {self.nome}\n")
        f"idade: {self.idade}\n"  
        f"sexo: {self.sexo}\n"
        f"E-mail: {self.email}\n"
        f"telefone": {self.telefone}
        f"endereco: {self.endereco}"

    def cadastrar_cliente (nome,idade,sexo,email,telefone,endereco):
        cliente = cliente (nome,idade,sexo,email,telefone,endereco)

        print(cliente)
        print ("\nCadastro efetuado com sucesso!")


        ##exemplo de cadatro de um cliente

    cadastrar_cliente()

    nome = "maria heloisa",
    idade = 35 
    sexo = "masculino"
    email = "maria.imples@gmail.com"
    telefone = "(011) 128945581"
    endereco = "rua das flores,123,São Paulo - SP"


