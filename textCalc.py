def receber_inputs():
    num1 = float(input("Digite um número real: "))
    num2 = float(input("Digite outro número real: "))
    operador = input("Digite a operação matemática desejada (+, -, *, /): ")
    return num1, num2, operador

def realizar_operacao(num1, num2, operador):
    if operador == "+":
        return num1 + num2
    elif operador == "-":
        return num1 - num2
    elif operador == "*":
        return num1 * num2
    elif operador == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "Erro: Não é possível dividir por zero."
    else:
        return "Erro: Operação inválida."

def main():
    while True:
        num1, num2, operador = receber_inputs()
        resultado = realizar_operacao(num1, num2, operador)
        print("Resultado:", resultado)

        continuar = input("Deseja realizar outra operação? (s/n): ")
        if continuar.lower() != 's':
            break

if __name__ == "__main__":
    main()
