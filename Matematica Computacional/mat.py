import matplotlib.pyplot as plt
import numpy as np

# Dados fictícios
categorias = ['Principal Meio de Aprendizado', 'Auxílio no Aprendizado', 'Não Utilizam a Internet']
quantidades = [400, 450, 150]

# Gráfico de Barras - Distribuição de pessoas por categoria de uso da internet
plt.figure(figsize=(10,6))
plt.bar(categorias, quantidades, color=['#3498db', '#2ecc71', '#e74c3c'])
plt.title('Distribuição de Pessoas por Categoria de Uso da Internet')
plt.xlabel('Categorias')
plt.ylabel('Quantidade de Pessoas')
plt.show()

# Gráfico de Dispersão - Relação entre uso principal e auxílio
# Gerar dados para o gráfico de dispersão com base na regressão
x = np.array([100, 200, 300, 400, 500])  # Quantidade de pessoas utilizando a internet como principal meio
y = 0.9 * x + 50  # Relação da regressão linear com o auxílio no aprendizado

plt.figure(figsize=(10,6))
plt.scatter(x, y, color='#9b59b6')
plt.plot(x, y, color='#8e44ad', linestyle='--', label='y = 0.9x + 50')
plt.title('Relação entre Uso Principal e Auxílio no Aprendizado')
plt.xlabel('Principal Meio de Aprendizado')
plt.ylabel('Auxílio no Aprendizado')
plt.legend()
plt.show()