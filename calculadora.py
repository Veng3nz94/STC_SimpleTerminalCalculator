def calculadora():
    print("Bem-vindo à calculadora simples!")
    print("Operações disponíveis:")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("0 - Sair")

    while True:
        try:
            operacao = int(input("Escolha uma operação (1/2/3/4/0): "))

            if operacao == 0:
                print("Saindo da calculadora. Até logo!")
                break
            elif operacao not in [1, 2, 3, 4]:
                print("Opção inválida. Tente novamente.")
                continue

            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            if operacao == 1:
                resultado = num1 + num2
                print(f"Resultado: {num1} + {num2} = {resultado}")
            elif operacao == 2:
                resultado = num1 - num2
                print(f"Resultado: {num1} - {num2} = {resultado}")
            elif operacao == 3:
                resultado = num1 * num2
                print(f"Resultado: {num1} * {num2} = {resultado}")
            elif operacao == 4:
                if num2 == 0:
                    print("Erro: Divisão por zero!")
                else:
                    resultado = num1 / num2
                    print(f"Resultado: {num1} / {num2} = {resultado}")

        except ValueError:
            print("Entrada inválida. Digite um número válido.")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")

# Chame a função para iniciar a calculadora
calculadora()
