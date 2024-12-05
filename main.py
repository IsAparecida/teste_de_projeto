# Função para obter um número válido
def obter_numero(mensagem):
    while True:  # Laço para garantir que o usuário insira um número válido
        try:
            numero = float(input(mensagem))  # Tenta converter a entrada para float
            return numero  # Retorna o número se for válido
        except ValueError:  # Se ocorrer um erro, solicita que insira um número válido
            print("Por favor, insira um número válido.")

# Solicitação de números ao usuário
print("Bem-vindo ao programa de operações matemáticas!")

num1 = obter_numero("Digite o primeiro número: ")  # Obtém o primeiro número
num2 = obter_numero("Digite o segundo número: ")   # Obtém o segundo número

# Realizando algumas operações matemáticas
soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
if num2 != 0:
    divisao = num1 / num2
else:
    divisao = "Indefinido (divisão por zero)"

# Exibindo os resultados
print(f"\nResultado das operações:")
print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}")