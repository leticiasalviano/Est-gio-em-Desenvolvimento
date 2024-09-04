def repeticao_letra_a(texto):
    
    contador = texto.lower().count('a')
    
    if contador > 0:
        print(f"A letra 'a' aparece {contador} vez(es) na string.")
    else:
        print("A letra 'a' não aparece na string.")

texto = input("Digite uma string: ")
repeticao_letra_a(texto)
