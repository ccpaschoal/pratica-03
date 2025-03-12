# 4- Verificador de Ano Bissexto
def verificador_ano_bissexto():
    try:
        ano = int(input("Digite um ano: "))
        # Um ano é bissexto se for divisível por 4, exceto anos centenários que não são divisíveis por 400.
        if (ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)):
            print(f"O ano {ano} é bissexto.")
        else:
            print(f"O ano {ano} não é bissexto.")
    except ValueError:
        print("Por favor, insira um ano válido (apenas números).")

verificador_ano_bissexto()