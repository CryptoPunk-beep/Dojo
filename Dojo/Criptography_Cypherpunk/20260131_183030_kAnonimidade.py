# Este código demonstra o conceito de k-anonimidade, onde um conjunto de registros é modificado para garantir que cada registro seja indistinguível de pelo menos k outros registros. 
# Isso é importante para proteger a privacidade dos indivíduos em bases de dados. 
# O código utiliza apenas bibliotecas padrão do Python, portanto, não há necessidade de instalação adicional.

import pandas as pd

# Criando um DataFrame com dados fictícios
data = {
    'Nome': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank'],
    'Idade': [25, 30, 25, 30, 40, 40],
    'Cidade': ['São Paulo', 'São Paulo', 'Rio de Janeiro', 'Rio de Janeiro', 'São Paulo', 'Rio de Janeiro']
}

df = pd.DataFrame(data)

# Aplicando k-anonimidade (k=2) agrupando por idade e cidade
anonimized_df = df.groupby(['Idade', 'Cidade']).size().reset_index(name='Contagem')
anonimized_df = anonimized_df[anonimized_df['Contagem'] >= 2]

# Exibindo os resultados
print("Dados originais:")
print(df)
print("\nDados anonimizados (k-anonimidade):")
print(anonimized_df)