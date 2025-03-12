# 1- Classificador de Idade
def classificador():
    try:
        idade = int(input("Digite sua idade: "))
        if idade < 0:
            print("Idade inválida!")
        elif idade <= 12:
            print("Categoria: Criança")
        elif idade <= 17:
            print("Categoria: Adolescente")
        elif idade <= 59:
            print("Categoria: Adulto")
        else:
            print("Categoria: Idoso")
    except ValueError:
        print("Por favor, insira um número inteiro válido para a idade.")

# 2- Calculadora de IMC
def imc():
    try:
        peso = float(input("Digite seu peso (em kg): "))
        altura = float(input("Digite sua altura (em metros): "))
        imc = peso / (altura ** 2)
        imc = round(imc, 2)
        if imc < 18.5:
            classificacao = "Abaixo do peso"
        elif imc < 25:
            classificacao = "Peso normal"
        elif imc < 30:
            classificacao = "Sobrepeso"
        else:
            classificacao = "Obeso"
        print(f"Seu IMC é {imc}. Classificação: {classificacao}.")
    except ValueError:
        print("Por favor, insira valores numéricos válidos para peso e altura.")

# 3- Conversor de Temperatura
def temperatura():
    try:
        temperatura = float(input("Digite a temperatura: "))
        unidade_origem = input("Digite a unidade de origem (C, F ou K): ").strip().upper()
        unidade_destino = input("Digite a unidade de destino (C, F ou K): ").strip().upper()

        # Se as unidades forem iguais, não há conversão
        if unidade_origem == unidade_destino:
            resultado = temperatura
        else:
            # Converte a temperatura para Celsius
            if unidade_origem == "C":
                temp_c = temperatura
            elif unidade_origem == "F":
                temp_c = (temperatura - 32) * 5/9
            elif unidade_origem == "K":
                temp_c = temperatura - 273.15
            else:
                print("Unidade de origem inválida!")
                return

            # Converte de Celsius para a unidade de destino
            if unidade_destino == "C":
                resultado = temp_c
            elif unidade_destino == "F":
                resultado = (temp_c * 9/5) + 32
            elif unidade_destino == "K":
                resultado = temp_c + 273.15
            else:
                print("Unidade de destino inválida!")
                return

        resultado = round(resultado, 2)
        print(f"Temperatura convertida: {resultado}°{unidade_destino}")
    except ValueError:
        print("Por favor, insira um valor numérico válido para a temperatura.")

# 4- Verificador de Ano Bissexto
def bissexto():
    try:
        ano = int(input("Digite um ano: "))
        # Um ano é bissexto se for divisível por 4, exceto anos centenários que não são divisíveis por 400.
        if (ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)):
            print(f"O ano {ano} é bissexto.")
        else:
            print(f"O ano {ano} não é bissexto.")
    except ValueError:
        print("Por favor, insira um ano válido (apenas números).")

# Menu de opções para o usuário escolher o programa desejado
def menu():
    print("\nEscolha uma opção:")
    print("1 - Classificador de Idade")
    print("2 - Calculadora de IMC")
    print("3 - Conversor de Temperatura")
    print("4 - Verificador de Ano Bissexto")
    opcao = input("Opção: ")

    if opcao == "1":
        classificador()
    elif opcao == "2":
        imc()
    elif opcao == "3":
        temperatura()
    elif opcao == "4":
        bissexto()
    else:
        print("Opção inválida!")

# Execução do menu principal
if __name__ == "__main__":
    menu()