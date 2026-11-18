
from cryptography.fernet import Fernet

def gerar_chave():
    chave = Fernet.generate_key()
    with open("chave.key", "wb") as arquivo:
        arquivo.write(chave)
    return chave

def carregar_chave():
    try:
        with open("chave.key", "rb") as arquivo:
            return arquivo.read()
    except FileNotFoundError:
        return gerar_chave()

def criptografar(mensagem):
    chave = carregar_chave()
    sistema = Fernet(chave)
    mensagem_criptografada = sistema.encrypt(mensagem.encode())
    return mensagem_criptografada.decode()

def descriptografar(mensagem):
    chave = carregar_chave()
    sistema = Fernet(chave)
    mensagem_original = sistema.decrypt(mensagem.encode())
    return mensagem_original.decode()
