resultats = [14, 17, 11, 5, 19, 18]
print(resultats[3]) #5 le quatrieme element de la liste
print(resultats[-1]) #18 le dernier de la liste
print(resultats[:3]) # les 3 premiers
print(resultats[-2:]) # les 2 derniers
print(resultats[1:4])
print(resultats[::-1]) # inverser la liste

# ajouter dans la liste
resultats.append(12)
print(resultats) # [14, 17, 11, 5, 19, 18, 12]

# retirer un élémnent de la liste
resultats.pop() # retirer le dernier
resultats.pop(1) # retirer l'element à l'indice 1
print(resultats) # [14, 11, 5, 19, 18]
# trier la liste
# resultats.sort()
resultats_tries = sorted(resultats)
print(resultats)
print(resultats_tries)

print(len(resultats))

# resultats += [5,6,4]
nouveaux_resultats = resultats + [5, 6, 4]
print(resultats)
print(nouveaux_resultats)

l = [1,2,3]
l[2] = 42
print(l)

carte = (1, 'Pique')
# carte[1] = 'Coeur' # interdit

print('Couleur', carte[1])
# destructurer un tuple
valeur, couleur = carte
print(valeur)
print(couleur)

livre = ('La nuit des temps', 'Barjavel', 1950)
(titre, _ ,annee) = livre
print(titre, annee)

a = 12
b = 4
#  swap de valeur
a, b = (b, a)
print(a)
print(b)

##### tests de performance #####

from random import randint
from timeit import timeit

l = [randint(0, 1_000_000_000_000) for _ in range(1_000_000)]
s = {randint(0, 1_000_000_000_000) for _ in range(1_000_000)}

print(len(l))
print(len(s))

duree_l = timeit(lambda : 42 in l, number=10)
duree_s = timeit(lambda : 42 in s, number=10)

print(duree_l)
print(duree_s)

print(f'{duree_l/duree_s:.0f} fois plus rapide de chercher dans un set')