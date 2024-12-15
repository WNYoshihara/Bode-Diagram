#William Noboru Yoshihara - 14612641
#Luana Fialho Franco de Melo - 14755061
#Professor orientador: Marcos Rogério Fernandes

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import TransferFunction, bode

# Função para obter input da função de tranferência G(s) do usuário (utiliza-se lista de mapas para separar a função em numerador e denominador, além do split, que separar os coeficie)
def G():
    print("Digite os coeficientes do numerador e denominador da função de transferência:")
    #Note como o diagrama de bode é montado somente para funções racionais, ou seja, razão entre polinômios
    num = list(map(float, input("Coeficientes do numerador (separados por espaço): ").split()))
    den = list(map(float, input("Coeficientes do denominador (separados por espaço): ").split()))
    return num, den


def Bode(num, den):
    #Criação da função de transferência e atrubuição a variavel sistema
    sistema = TransferFunction(num, den)

    # Obtenção dos dados para o diagrama de Bode usando a funcao bode
    w, mag, phase = bode(sistema)


    #Configuração para a plotagem --------------------------

    # Plot do módulo
    plt.figure(figsize=(10, 6))

    plt.subplot(2, 1, 1)
    plt.semilogx(w, mag)  # Escala logarítmica para a frequência
    plt.title("Diagrama de Bode")
    plt.ylabel("Magnitude (dB)")
    plt.grid(which="both", linestyle="--", linewidth=0.5)

    # Plot da fase
    plt.subplot(2, 1, 2)
    plt.semilogx(w, phase)
    plt.ylabel("Fase (graus)")
    plt.xlabel("Frequência (rad/s)")
    plt.grid(which="both", linestyle="--", linewidth=0.5)

    plt.tight_layout()
    plt.show()
    # -------------------------------------------------

if __name__ == "__main__":
    print("Simulador de Diagrama de Bode para SLIT")
    num, den = G()
    Bode(num, den)
