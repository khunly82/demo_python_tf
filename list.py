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
