from cryptography.fernet import fernet

def write_key():
    key = fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    with open("key.key", "rb") as key_file:
        key = key_file.read()
    return key

key = load_key()
fer = fernet(key)

chave_mestra = input("Forneça a chave mestra: ")

def ver():
    with open('senhas.txt', 'r') as arquivoSenhas:
        for line in arquivoSenhas.readlines():
            dadosUsuario = line.rstrip("\n")
            user, senha_criptografada = dadosUsuario.split("|")
            try:
                senha_decriptografada = fer.decrypt(senha_criptografada.encode()).decode()
                print(f"Usuário: {user} | Senha: {senha_decriptografada}")
            except:
                print(f"Erro ao decriptografar a senha para o usuário: {user}")

def add():
    nome_conta = input("Nome da conta: ")
    senha_conta = input("Senha a ser salva: ")

    senha_criptografada = fer.encrypt(senha_conta.encode()).decode()

    with open('senhas.txt', 'a') as arquivoSenhas:
        arquivoSenhas.write(nome_conta + "|" + senha_criptografada + "\n")

while True:
    modo = input("Você gostaria de adicionar uma senha ou visualizar sua lista de senhas? (envie 's' caso queira sair.): ").lower()
    if modo == 's':
        break

    if modo == 'visualizar':
        ver()

    elif modo == 'adicionar':
        add()

    else:
        print("Modo inválido.")
