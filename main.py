
from criptografia import criptografar, descriptografar
from hash import gerar_hash, verificar_hash

print("=" * 40)
print(" PROTEÇÃO DE INFORMAÇÕES")
print(" CRIPTOGRAFIA E HASH COM PYTHON")
print(" Maria Eduarda Lopes - 3º A")
print("=" * 40)

while True:
    print("\n1 - Criptografar mensagem")
    print("2 - Descriptografar mensagem")
    print("3 - Gerar Hash SHA-256")
    print("4 - Verificar Hash")
    print("0 - Sair")

    opcao = input("\nEscolha uma opção: ")

    try:
        if opcao == "1":
            mensagem = input("Digite a mensagem: ")
            print("Mensagem criptografada:")
            print(criptografar(mensagem))

        elif opcao == "2":
            mensagem = input("Cole a mensagem criptografada: ")
            print("Mensagem original:")
            print(descriptografar(mensagem))

        elif opcao == "3":
            texto = input("Digite o texto: ")
            print("Hash SHA-256:")
            print(gerar_hash(texto))

        elif opcao == "4":
            texto = input("Digite o texto original: ")
            hash_original = input("Digite o hash para comparar: ")

            if verificar_hash(texto, hash_original):
                print("Hash válido! Os dados correspondem.")
            else:
                print("Hash inválido! Os dados são diferentes.")

        elif opcao == "0":
            print("Programa encerrado.")
            break

        else:
            print("Opção inválida.")

    except Exception:
        print("Erro: verifique os dados informados.")
