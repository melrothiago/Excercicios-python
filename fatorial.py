def fatorial(n):
    """Retorna o fatorial de um número n não negativo."""
    if n == 0:  # Caso base
        return 1
    return n * fatorial(n - 1)  # Passo recursivo


# Solicita um número do usuário
try:
    numero = int(input("Digite um número inteiro não negativo: "))
    if numero < 0:
        print("O número deve ser não negativo. Tente novamente.")
    else:
        # Chama a função e imprime o resultado
        print(f"O fatorial de {numero} é {fatorial(numero)}.")
except ValueError:
    print("Por favor, insira um número inteiro válido.")
