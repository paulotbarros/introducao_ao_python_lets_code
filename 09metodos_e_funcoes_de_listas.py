# > Métodos de Listas

lista = [1, 3, 12, 8, 2]

# Append --> Adiciona elementos ao final da lista. 

print('Antes do append: ',lista)

lista.append(3)

print('Depois do append: ',lista)

# Insert --> Também faz adicição a lista, porém você escolhe qual elemento adicionar e aonde adicionar.

lista.insert(2, 10)

print('Depois do insert: ',lista)

# Extend --> Ele faz a junção dos elemntos de duas listas, ao final da lista desejada. "Concaternasr duas listas"

lista2 = [1, 2, 3]

lista.extend(lista2)

print('Depois do extend: ',lista)

''' # Pop --> Ele serve para remover o elemento que você especificar da lista, 
ou se você não especificar ele remove o último elemento da lista.'''


# Neste caso o elemento a ser removido será o último da lista.

lista.pop()  

print('Lista após o pop: ', lista)

lista.pop(0)

print('Lista após o pop remover o elemento indice 0', lista)

'''# Remove --> Ele remove qual elemento da lista for especificado. 
Caso tenha mais do mesmo elemento na lista ele irá remover sempre o 
primeiro elemento encontrado.'''

lista.remove(3)

print('Depois do remove: ', lista)

# Count --> Faz a contangem do elemento especificado dentro da lista.

print('Quantidade de 2 na lista: ', lista.count(2))


# Index --> Ele passa qual é o indice de um determinado elemento especificado.

print('Índice do elemnto 12: ', lista.index(12))

# Sort --> Ele serve para ordenar a os elementos da lista de forma crescente.

lista.sort()

print(lista)

# Quando quiser ordenar de forma decrescente é só aplicar lista.sort(reverse=True)

lista.sort(reverse=True)

print(lista)

# Funções para Listas

# Len --> Esta função te passa a quantidade de elementos existente dentro da sua lista.

print(len(lista))

# Sum --> Esta função faz a soma de todos elementos que estão dentro da lista.

print(sum(lista))

# Max --> Esta função te retorna o maior elemento da sua lista.

print('Maior elemento da lista: ', max(lista))

# Min --> Esta função te retorna o menor elemento da sua lista.

print('Menor elemento da lista: ', min(lista))

