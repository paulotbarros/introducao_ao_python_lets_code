# > Dicionários

# Criando dicionários

dicionario = {}

dicionario = dict()

dicionario = { 'nome': 'Paulo', 'idade': 26, 'altura': 1.77}

print(dicionario)
print(dicionario['idade'])

# Adicionando elementos em um dicionário

dicionario['programador'] = True
print(dicionario)

dicionario['altura'] = 2
print(dicionario)

# Iterando sobre um dicionario

for chave in dicionario:
    print(chave, dicionario[chave])

# Testando a existência de uma chave

print('Peso' in  dicionario)
print('altura' in dicionario)