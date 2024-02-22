#Import das bibliotecas utilizadas
import os 
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Leitura de DataBase
caminho_absluto = os.path.abspath('Defective_Equipment.xlsx')
df = pd.read_excel(caminho_absluto)

#Correlação de Pearson
# Quando fazer análise de correlação?

# Quando você tem uma hipótese de que o aumento ou queda em uma variável estão associados à evolução de outra variável, por exemplo, se aumentar o desconto,
# as vendas também aumentam.

# No r de Pearson, a métrica da linearidade entre variáveis é exposta em um número que vai de -1 a +1. 
# Quanto mais próximo dos extremos (-1 ou 1), maior é a força da correlação. Valores próximos de zero querem dizer a correlação é fraca.

# O valor ser negativo ou positivo indica a direção desta relação. 
# Se positiva, o aumento em uma variável implica no aumento na outra variável. Já os valores negativos indicam que o aumento de uma 
# variável implica no decréscimo de outra

# Exclue valores não númericos dos dados
numeric_df = df.select_dtypes(include=[np.number])

# Cálcula a correlação
correlation_matrix = numeric_df.corr()

# Print da Matrix de correlações
print(correlation_matrix)

# Chama a figura 
plt.figure()
# Chamando o gráfico de heatmap
sns.heatmap(correlation_matrix, annot= True)

# Insere título do gráfico
plt.title ('Correalação de Pearson')

# Chama a figura 
plt.figure()

# Laço for para gerara o Scatter plot de V1 até V8
for column in numeric_df.columns[1:]:
    sns.scatterplot(data=numeric_df, x='V1', y=column, label=column)

#Chama a Legenda do gráfico
plt.legend()

#Insere título do gráfico
plt.title ('Comparação Gráfica')

# A correlação de Spearman descreve a relação entre as variáveis através de uma função monotética.

# Isso significa, de maneira simplificada, que ele está analisando se, quando o valor de uma variável aumenta ou diminui,
# o valor da outra variável
# aumenta ou diminui.

# Para interpretarmos esta relação, o coeficiente da correlação de Spearman gera um número que varia de -1 a +1. Quanto mais próximo 
# dos extremos (-1 ou 1), maior é a força da correlação. Já os valores próximos de 0 implicam em correlações mais fracas ou inexistentes.

# O quão próximo do zero indica o poder da relação, mas também precisamos interpretar o sinal, 
# se é positivo ou negativo, que indica a direção desta relação. 
# Se positiva, o aumento em uma variável implica no aumento na outra variável. 
# Os valores negativos indicam que o aumento de uma variável implica no decréscimo de outra

# Não existe consenso sobre o a interpretação do poder da correlação, mas existem algumas recomendações. 
# Cohen (1992) sugere os seguintes tamanhos de efeito:

# r = 0,10 -> correlação fraca.
# r = 0,30 -> correlação moderada.
# r = 0,50 -> correlação forte.
# (“How to Interpret a Correlation Coefficient r – dummies,” 2019) sugere que:

# r = 0,30 -> correlação fraca
# r = 0,50 -> correlação moderada
# r = 0,70 -> correlação forte

# Esse coeficiente também é chamado de coeficiente de determinação e é considerado o tamanho de efeito da correlação.

# Elevando o valor de rs ao quadrado, percebemos que rs = 0,10, significa que 1% da variação de uma variável pode ser explicada pela outra.
# rs = 0,30 explica 9% da variância total e rs = 0,50 explica 25% da variância total.

# Por isso, interpretar o rs2 pode trazer mais clareza sobre o quanto os construtos encontram-se relacionados.

# É importante atenção, pois na medida em que o coeficiente de correlação vai aumentando, a variância compartilhada cresce exponencialmente.
# Por exemplo, a diferença de variância explicada entre os coeficientes de correlação de 0,10 para 0,20, é de apenas 3%. 
# Entretanto, entre rs = 0,80 e rs = 0,90, a diferença na variância explicada já é de 17%.

# É importante destacar que para a interpretabilidade do tamanho do efeito das correlações,
# você pode se basear nas diretrizes mencionadas, mas é a revisão da literatura que irá, de fato, 
# lhe informar se os seus achados são fracos ou fortes.

# Exclue valores não númericos dos dados
numeric_df1 = df.select_dtypes(include=[np.number])

# Calcula a Correlação 
correlation_matrix1 = numeric_df1.corr('spearman')

# Print da Matrix de correlações
print(correlation_matrix1)

# Chama a figura 
plt.figure()

# Chamando o gráfico de heatmap
sns.heatmap (correlation_matrix1, annot= True)

# Definição de Título do gráfico
plt.title ('Correlação de Spearman')

# Mostra os gráficos
plt.show()

