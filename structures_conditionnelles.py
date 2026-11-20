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