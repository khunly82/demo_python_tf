prenoms = ['Khun', 'Pierre', 'Robin']
noms = ['LY', 'JUIF', 'PECHEUR']
notes = [4, 12, 6]

for nom, prenom, note in zip(noms, prenoms, notes):
    print(nom, prenom, note, sep=' - ')


# comprehension
scores = [4, 3.5, 5, 1 , 2.5]
scores_100 = [score * 20 for score in scores if score > 3]
# for s in scores:
#     scores_100.append(s * 20)
print(scores_100)