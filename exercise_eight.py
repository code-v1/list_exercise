foods = ('hotdog', 'pizza', 'burger')

for food in [food for food in foods if 'a' in food]:
    print(food)