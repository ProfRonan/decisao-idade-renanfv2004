while True:
    valor = input("Digite um valor: ")

    try:
        valor_inteiro = int(valor)

        if valor_inteiro < 0:
            print("Impossível!")
        elif valor_inteiro < 18:
            print("Não precisa se alistar.")
        elif valor_inteiro < 65:
            print("Não esqueça de votar na próxima eleição.")
        elif valor_inteiro >= 65:
            print("Vá descansar.")
        else:
            print("Eita!")
        
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")
