# 2- Calculadora de IMC
def calculadora_imc():
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
        return classificacao
    
    except ValueError:
        print("Por favor, insira valores numéricos válidos para peso e altura.")
        
calculadora_imc()