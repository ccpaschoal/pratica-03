# 3- Conversor de Temperatura
def conversor_temperatura():
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
conversor_temperatura()