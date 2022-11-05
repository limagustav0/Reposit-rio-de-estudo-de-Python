def encriptador(texto):
    import random
    import string
    letra = string.ascii_letters.lower() + string.ascii_letters.upper() + '!@#$%¨&*1234567890'
    try:
        liberador = [random.choice(letra) for x in range(0,4)]
        liberador = (''.join(liberador))

        textoCriptografado = [random.choice(letra) for i in range(0,len(texto))]

        textoCriptografado = (''.join(textoCriptografado))

        print(f'A criptografia do texto digitado é {texto} é {textoCriptografado}')

        print("\n\n✊ PIN >>> {}".format(liberador))
        pintest = input("Digite o PIN para liberar o decodificador: ")

        while liberador != pintest:
            print("PIN incorreto. O PIN será redefinido.")
            liberador = [random.choice(letra) for x in range(0, 4)]
            liberador = (''.join(liberador))
            print('\n✊ PIN:', liberador)
            pintest = input("Digite o PIN para liberar o decodificador: ")
        else:
            decriptador = input("\n✋ Decodificador liberado. \nDescriptografe o código com a criptografia gerada: ")
            while decriptador != textoCriptografado:
                decriptador = input("Entrada inválida❗ Escreva a codificação certa! \nDescriptografe o código com a criptografia gerada: ")
            else:
                print('\n✅ Texto descriptografado. O texto digitado é {}.'.format(texto))
    except Exception as e:
        print(e)

if __name__ == '__main__':
    encriptador('1234567')