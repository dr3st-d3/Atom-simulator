import math
import numpy as np

def funcao_da_onda_1s(r):                                    # Define a Função da Onda de 1s;
    return (1 / math.sqrt(math.pi)) * np.exp(-r)             # Retorne: 1 sobre raiz quadrada de "pi" vezes "e" elevado a "-r" -> (1/√π) * e^(-r); 

def densidade_de_probabilidade_1s(r):                        # Define a Densidade de Probabilidade de 1s;
    psi = funcao_da_onda_1s(r)                               # ψ = Função da Onda de 1s(r);
    return abs(psi) ** 2                                     # Retorne: O módulo de ψ ao quadrado -> |ψ|²;

def distribuicao_radial_1s(r):                               # Define a Distribuição Radial de 1s;
    densidade = densidade_de_probabilidade_1s(r)             # Densidade = Densidade de Probabilidades de 1s(r);
    return 4 * math.pi * r ** 2 * densidade                  # Retorne: 4 vezes "pi" vezes "r" ao quadrado vezes Densidade -> 4πr²|ψ|²;

quantidade_pontos = 10000

pontos_x = np.random.uniform(-5, 5, quantidade_pontos)
pontos_y = np.random.uniform(-5, 5, quantidade_pontos)
pontos_z = np.random.uniform(-5, 5, quantidade_pontos)

R_pontos = np.sqrt(
    pontos_x**2 +
    pontos_y**2 +
    pontos_z**2
)

densidade_pontos = densidade_de_probabilidade_1s(R_pontos)

print()
print("----------PONTOS ALEATÓRIOS----------")
print(f"Quantidade de Pontos: {quantidade_pontos}")
print(f"Formato dos Pontos X: {pontos_x.shape}")
print(f"Formato dos Pontos Y: {pontos_y.shape}")
print(f"Formato dos Pontos Z: {pontos_z.shape}")
print(f"Formato de densidade_pontos: {densidade_pontos.shape}")
print()
