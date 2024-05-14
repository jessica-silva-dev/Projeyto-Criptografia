from hashlib import sha256

mensagem = input("Digite a senha que vai ser criptografada: ")
senha_de_acesso = input("Cadastre uma senha para acessar a mensagem criptografada: ")
print(" ")

mensagem_cript = sha256(mensagem.encode()).digest()
print("Mensagem Criptografada")
print(mensagem_cript)
print(" ")

validar = ""
while (validar != senha_de_acesso):
    validar = input("Digite a senha para ter acesso: ")
    print(" ")
    if (validar == senha_de_acesso):
        print("Acesso liberado!")
        print("Mensagem descriptografada é:")
        print(mensagem)
        break
    else:
        print("Acesso Bloqueado!")
