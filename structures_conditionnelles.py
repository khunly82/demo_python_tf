age = 6

# if cond:
    # instruction 1
    # instruction 2
    # instruction 3

if age < 18:
    print('Bienvenue 🌽!')
    print('Bienvenue 🌽!')
    print('Bienvenue 🌽!')
elif age < 24:
    print('Bienvenue 🍎!')
else:
    print('Bienvenue 🥩!')

jour = 4
match jour:
    case 1:
        print('lundi')
    case 2:
        print('mardi')
    case 3:
        print('mercredi')
    case _:
        print('J\'ai la flemme')

nom = 'Khun'
# operateur ternaire
metier = 'Prof' if nom == 'Khun' else 'Autre metier'
print(metier)

# coalesce
promotion = None
prix = 50
print(prix - (prix * (promotion or 0) / 100))

a = True
b = True

if a ^ b:
    print('On ne peut pas etre vrai en meme temps')
if a or b:
    print('Un peut etre vrai') 

# Falsy / Truthy
nom = ''
if nom:
    print(nom)

print(not not True)
print(not not 'Khun') # True car 'Khun' est truthy
print(not not '') # False car '' est falsy
print(not not 0) # False
print(not not []) # False
print(not not None) # False

