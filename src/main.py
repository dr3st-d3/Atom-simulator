import math
import numpy as np
import matplotlib.pyplot as plt

def funcao_da_onda_1s(r):                                    # Define a Função da Onda de 1s;
    return (1 / math.sqrt(math.pi)) * np.exp(-r)             # Retorne: 1 sobre raiz quadrada de "pi" vezes "e" elevado a "-r" -> (1/√π) * e^(-r); 

def densidade_de_probabilidade_1s(r):                        # Define a Densidade de Probabilidade de 1s;
    psi = funcao_da_onda_1s(r)                               # ψ = Função da Onda de 1s(r);
    return abs(psi) ** 2                                     # Retorne: O módulo de ψ ao quadrado -> |ψ|²;

def distribuicao_radial_1s(r):                               # Define a Distribuição Radial de 1s;
    densidade = densidade_de_probabilidade_1s(r)             # Densidade = Densidade de Probabilidades de 1s(r);
    return 4 * math.pi * r ** 2 * densidade                  # Retorne: 4 vezes "pi" vezes "r" ao quadrado vezes Densidade -> 4πr²|ψ|²;

r_valores = np.linspace(0, 5, 501)                           # Cria um array com 501 valores igualmente espaçados entre 0 e 5 a₀;
psi_valores = funcao_da_onda_1s(r_valores)                   # Calcula a Função da Onda de 1s para cada valor de r armazenado em r_valores;
densidade_valores = densidade_de_probabilidade_1s(r_valores) # Calcula a Densidade de Probabilidade |ψ|² para cada valor de r armazenado em r_valores;
radial_valores = distribuicao_radial_1s(r_valores)           # Calcula a Distribuição Radial P(r) para cada valor de r armazenado em r_valores;

# Grafico de ψ(r)
plt.plot(r_valores, psi_valores)                             # Valores usados no gráfico: r_valores no eixo x e ψ(r) no eixo y;
plt.xlabel("r (a₀)")                                         # Define o rótulo do eixo x como "r (a₀)";
plt.ylabel("ψ(r)")                                           # Define o rótulo do eixo y como "ψ(r)";
plt.title("Função de Onda do Hidrogênio - Estado 1s")        # Define o título do gráfico como "Função de Onda do Hidrogênio - Estado 1s";
plt.show()                                                   # Exibe o gráfico na tela;

# Grafico de |ψ(r)|²
plt.figure()                                                 # Nova figura;
plt.plot(r_valores, densidade_valores)                       # Valores usados no gráfico: r_valores no eixo x e ψ(r) no eixo y;
plt.xlabel("r (a₀)")                                         # Define o rótulo do eixo x como "r (a₀)";
plt.ylabel("|ψ(r)|²")                                        # Define o rótulo do eixo y como "|ψ(r)|²";
plt.title("Densidade de Probabilidade - Estado 1s")          # Define o título do gráfico como "Densidade de Probabilidade - Estado 1s";
plt.show()                                                   # Exibe o gráfico na tela;

# Grafico de P(r)
plt.figure()                                                 # Nova figura;
plt.plot(r_valores, radial_valores)                          # Valores usados no gráfico: r_valores no eixo x e ψ(r) no eixo y;
plt.xlabel("r (a₀)")                                         # Define o rótulo do eixo x como "r (a₀)";
plt.ylabel("P(r)")                                           # Define o rótulo do eixo y como "P(r)";
plt.title("Distribuição Radial - Estado 1s")                 # Define o título do gráfico como "Distribuição Radial - Estado 1s";
plt.show()                                                   # Exibe o gráfico na tela;

print()                                                      # Imprime uma linha em branco;
print("----------NUMPY----------")                           # Imprime: "----------NUMPY----------";
print(f"ψ(0) = {psi_valores[0]}")                            # Imprime o valor de ψ quando r = 0 a₀; o índice 0 corresponde ao primeiro elemento de r_valores;
print(f"ψ(1) = {psi_valores[100]}")                          # Imprime o valor de ψ quando r = 1 a₀; O índice 100 corresponde a r = 1 porque r_valores possui passo de 0,01;
print(f"|ψ(0)|² = {densidade_valores[0]}")                   # Imprime o valor de |ψ|² quando r = 0 a₀;
print(f"|ψ(1)|² = {densidade_valores[100]}")                 # Imprime o valor de |ψ|² quando r = 1 a₀;
print(f"P(0) = {radial_valores[0]}")                         # Imprime o valor de P(r) quando r = 0 a₀;
print(f"P(1) = {radial_valores[100]}")                       # Imprime o valor de P(r) quando r = 1 a₀;
print()                                                      # Imprime uma linha em branco;

# Parte Antiga    
print("----------LOOP FOR----------")                        # Imprime: "----------LOOP FOR----------";
for r in [0, 0.5, 1, 1.5, 2, 3, 4]:                          # Loop: Para cada valor de "r" na lista [0, 1, 2, 3, 4];
    psi = funcao_da_onda_1s(r)                               # ψ = Função da Onda de 1s(r);
    densidade = densidade_de_probabilidade_1s(r)             # Densidade = Densidade de Probabilidades de 1s(r);
    radial = distribuicao_radial_1s(r)                       # Radial = Distribuição Radial de 1s(r);

    print()                                                  # Imprime uma linha em branco;
    print(f"r = {r} a₀")                                     # Imprime: "r = {r} a₀";
    print(f"ψ(r) = {psi}")                                   # Imprime: "ψ(r) = {psi}";
    print(f"|ψ(r)|² = {densidade}")                          # Imprime: "|ψ(r)|² = {densidade}";
    print(f"P(r) = {radial}")                                # Imprime: "P(r) = {radial}";
    print()                                                  # Imprime uma linha em branco;