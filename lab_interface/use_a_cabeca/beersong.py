word = 'garrafas'
for beer_num in range(99,0,-1):
    print(beer_num, word, "de cerveja na parede")
    print(beer_num, word, "de cerveja")
    print("Derruba mais uma")
    print("Passe adiante")
    
    if beer_num == 1:
        print('sem mais garrafa de cerveja na parede')
    else:
        new_num = beer_num -1
        if new_num == 1:
            word = 'garrafa'
        print(new_num, word, 'de cerveja na parede')
    print()

