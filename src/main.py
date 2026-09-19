import math
import numpy as np
import matplotlib.pyplot as plt

def funcao_da_onda_1s(r):                          # Define a Função da Onda de 1s;
    return (1 / math.sqrt(math.pi)) * np.exp(-r) # Retorne: 1 sobre raiz quadrada de "pi" vezes "e" elevado a "-r" -> (1/√π) * e^(-r); 

def densidade_de_probabilidade_1s(r):              # Define a Densidade de Probabilidade de 1s;
    psi = funcao_da_onda_1s(r)                     # ψ = Função da Onda de 1s(r);
    return abs(psi) ** 2                           # Retorne: O módulo de ψ ao quadrado -> |ψ|²;

def distribuicao_radial_1s(r):                     # Define a Distribuição Radial de 1s;
    densidade = densidade_de_probabilidade_1s(r)   # Densidade = Densidade de Probabilidades de 1s(r);
    return 4 * math.pi * r ** 2 * densidade        # Retorne: 4 vezes "pi" vezes "r" ao quadrado vezes Densidade -> 4πr²|ψ|²;

r_valores = np.linspace(0, 5, 501)
psi_valores = funcao_da_onda_1s(r_valores)
densidade_valores = densidade_de_probabilidade_1s(r_valores)
radial_valores = distribuicao_radial_1s(r_valores)

# Grafico de ψ(r)
plt.plot(r_valores, psi_valores)
plt.xlabel("r (a₀)")
plt.ylabel("ψ(r)")
plt.title("Função de Onda do Hidrogênio - Estado 1s")
plt.show()

# Grafico de |ψ(r)|²
plt.figure()
plt.plot(r_valores, densidade_valores)
plt.xlabel("r (a₀)")
plt.ylabel("|ψ(r)|²")
plt.title("Densidade de Probabilidade - Estado 1s")
plt.show()

# Grafico de P(r)
plt.figure()
plt.plot(r_valores, radial_valores)
plt.xlabel("r (a₀)")
plt.ylabel("P(r)")
plt.title("Distribuição Radial - Estado 1s")
plt.show()

print()
print("----------NUMPY----------")
print(f"ψ(0) = {psi_valores[0]}")
print(f"ψ(1) = {psi_valores[100]}")
print(f"|ψ(0)|² = {densidade_valores[0]}")
print(f"|ψ(1)|² = {densidade_valores[100]}")
print(f"P(0) = {radial_valores[0]}")
print(f"P(1) = {radial_valores[100]}")
print()
    
print("----------LOOP FOR----------")              # Imprima: "----------LOOP FOR----------";
for r in [0, 0.5, 1, 1.5, 2, 3, 4]:                # Loop: Para cada valor de "r" na lista [0, 1, 2, 3, 4];
    psi = funcao_da_onda_1s(r)                     # ψ = Função da Onda de 1s(r);
    densidade = densidade_de_probabilidade_1s(r)   # Densidade = Densidade de Probabilidades de 1s(r);
    radial = distribuicao_radial_1s(r)             # Radial = Distribuição Radial de 1s(r);

    print()                                        # Imprima uma linha em branco;
    print(f"r = {r} a₀")                           # Imprima: "r = {r} a₀";
    print(f"ψ(r) = {psi}")                         # Imprima: "ψ(r) = {psi}";
    print(f"|ψ(r)|² = {densidade}")                # Imprima: "|ψ(r)|² = {densidade}";
    print(f"P(r) = {radial}")                      # Imprima: "P(r) = {radial}";
    print()                                        # Imprima uma linha em branco;