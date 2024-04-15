#%%
set([1,2,3,1,3,4])  # o set elimina objetos duplicados.

carros = {"gol","celta","palio"}

for carro in carros :
    print(carro)


# %%
#Métodos :
# add(): adiciona um elemento ao conjunto.
my_set = {1, 2, 3}
my_set.add(4)
print(my_set)  # Output: {1, 2, 3, 4}
#remove(): remove um elemento do conjunto.
my_set = {1, 2, 3}
my_set.remove(3)
print(my_set)  # Output: {1, 2}
#discard(): remove e retorna um elemento do conjunto.
my_set = {1, 2, 3}
my_set.discard(2)
print(my_set)  # Output: {1, 3}
#clear(): remove todos os elementos do conjunto.
my_set = {1, 2, 3}
my_set.clear()
print(my_set)  # Output: set()
#pop(): remove e retorna o último elemento adicionado ao conjunto (se houver).
my_set = {1, 2, 3}
my_set.add(4)
my_set.pop()
print(my_set)  # Output: {1, 3}
#update(): atualiza o conjunto com elementos de outro conjunto.
my_set = {1, 2, 3}
my_set.update({4, 5, 6})
print(my_set)  # Output: {1, 2, 3, 4, 5, 6}
#union(): retorna um novo conjunto contendo todos os elementos de ambos os conjuntos.
set1 = {1, 2, 3}
set2 = {4, 5, 6}
union_set = set1.union(set2)
print(union_set) # Output: {1, 2, 3, 4, 5, 6}

#intersection(): retorna um novo conjunto contendo todos os elementos comuns aos dois conjuntos.
set1 = {1, 2, 3}
set2 = {4, 5, 6}
intersection_set = set1.intersection(set2)
print(intersection_set)  # Output: {4, 5}
#difference(): retorna um novo conjunto contendo todos os elementos de um conjunto, mas não do outro.
set1 = {1, 2, 3}
set2 = {4, 5, 6}
difference_set = set1.difference(set2)
print(difference_set) # Output: {1, 2}

#isdisjoint(): retorna True se os conjuntos não tiverem nenhum elemento em comum.
set1 = {1, 2, 3}
set2 = {4, 5, 6}
if set1.isdisjoint(set2):
    print("Os conjuntos não possuem nenhum elemento em comum.")
else:
    print("Os conjuntos possuem elementos em comum.")


# %%
