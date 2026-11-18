
import hashlib

def gerar_hash(texto):
    resultado = hashlib.sha256(texto.encode())
    return resultado.hexdigest()

def verificar_hash(texto, hash_original):
    hash_atual = gerar_hash(texto)
    return hash_atual == hash_original
