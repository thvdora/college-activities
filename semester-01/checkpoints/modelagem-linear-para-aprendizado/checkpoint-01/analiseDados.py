import pandas as pd

dados_alunos = {
    'Nome': ['Ana', 'Bruno', 'Carla', 'Daniel', 'Eva'],
    'Idade': [20, 22, 21, 23, 20],
    'Nota': [8.5, 7.0, 9.2, 6.8, 7.5]
}

df = pd.DataFrame(dados_alunos)

print(df)

# 1. Informações básicas do DataFrame
df.info()

# 2. Média de idade dos alunos
media_idade = df["Idade"].mean()
print("Média de idade:", media_idade)

# 3. Alunos com nota maior ou igual a 8.0
alunos_aprovados = df[df["Nota"] >= 8.0]

print(alunos_aprovados)
