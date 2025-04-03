def soma_cumulativa(lista):
    """
    Calcula a soma cumulativa dos elementos de uma lista de inteiros.
    
    :param lista: Lista de números inteiros.
    :return: Lista com a soma cumulativa.
    """
    resultado = []
    soma = 0
    for numero in lista:
        soma += numero
        resultado.append(soma)
    return resultado

def main():
    print("Bem-vindo ao calculador de soma cumulativa!")
    print("Digite os números que deseja somar, separados por espaço.")
    
    while True:
        # Solicita ao usuário que insira uma lista de números
        entrada = input("\nDigite os números (ou 'sair' para encerrar): ")
        
        # Verifica se o usuário quer sair
        if entrada.lower() == "sair":
            print("Encerrando o programa...")
            break
        
        # Converte a entrada em uma lista de números inteiros
        try:
            lista_numeros = list(map(int, entrada.split()))
        except ValueError:
            print("Entrada inválida! Certifique-se de digitar apenas números inteiros.")
            continue
        
        # Calcula a soma cumulativa
        resultado = soma_cumulativa(lista_numeros)
        
        # Exibe o resultado
        print("A soma cumulativa da lista é:", resultado)

# Executa o programa
if __name__ == "__main__":
    main()
