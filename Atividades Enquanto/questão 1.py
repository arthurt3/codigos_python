def cadastrar_usuario(usuario_existente=None):
    
    while True:
        login = input("Digite o login desejado: ")
        
        if usuario_existente and login == usuario_existente:
            print("Esse login já foi utilizado. Escolha outro.")
            continue
        
        senha = input("Digite a senha desejada: ")
        
        while senha == login:
            print("A senha não pode ser igual ao login. Tente novamente.")
            senha = input("Digite a senha desejada: ")
        
        return login, senha

# Cadastro do primeiro usuário
print("Cadastro do Primeiro Usuário")
login1, senha1 = cadastrar_usuario()

# Cadastro do segundo usuário, garantindo que o login não seja igual ao do primeiro usuário
print("Cadastro do Segundo Usuário")
login2, senha2 = cadastrar_usuario(usuario_existente=login1)

print("\nUsuários cadastrados com sucesso!")
print(f"Usuário 1 - Login: {login1}, Senha: {senha1}")
print(f"Usuário 2 - Login: {login2}, Senha: {senha2}")