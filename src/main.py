import math
import numpy as np
import pyvista as pv

def funcao_da_onda_1s(r):                                    # Define a Função da Onda de 1s;
    return (1 / math.sqrt(math.pi)) * np.exp(-r)             # Retorne: 1 sobre raiz quadrada de "pi" vezes "e" elevado a "-r" -> (1/√π) * e^(-r); 

def densidade_de_probabilidade_1s(r):                        # Define a Densidade de Probabilidade de 1s;
    psi = funcao_da_onda_1s(r)                               # ψ = Função da Onda de 1s(r);
    return abs(psi) ** 2                                     # Retorne: O módulo de ψ ao quadrado -> |ψ|²;

def distribuicao_radial_1s(r):                               # Define a Distribuição Radial de 1s;
    densidade = densidade_de_probabilidade_1s(r)             # Densidade = Densidade de Probabilidades de 1s(r);
    return 4 * math.pi * r ** 2 * densidade                  # Retorne: 4 vezes "pi" vezes "r" ao quadrado vezes Densidade -> 4πr²|ψ|²;

quantidade_pontos = 10000

raios = np.random.gamma(
    shape=3,
    scale=0.5,
    size=quantidade_pontos
)

cos_theta = np.random.uniform(
    -1,
    1,
    quantidade_pontos
)

phi = np.random.uniform(
    0,
    2 * math.pi,
    quantidade_pontos
)

sin_theta = np.sqrt(1 - cos_theta**2)

pontos_x = raios * sin_theta * np.cos(phi)
pontos_y = raios * sin_theta * np.sin(phi)
pontos_z = raios * cos_theta

pontos = np.column_stack((
    pontos_x,
    pontos_y,
    pontos_z
))

nuvem = pv.PolyData(pontos)

plotter = pv.Plotter()

plotter.add_points(
    nuvem,
    point_size=5,
    render_points_as_spheres=True
)

print()
print("----------AMOSTRAGEM RADIAL----------")
print(f"Quantidade de pontos: {quantidade_pontos}")
print(f"Menor raio: {raios.min():.4f}")
print(f"Maior raio: {raios.max():.4f}")
print(f"Raio médio: {raios.mean():.4f}")
print()

plotter.show()