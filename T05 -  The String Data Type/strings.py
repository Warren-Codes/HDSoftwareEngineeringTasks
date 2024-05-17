#The below print(hero) statement will print Superman 
hero = "Superman"
print(hero)

#By manipulating the string with.join allows the character ^ to be inserted after every letter
hero_join = "^".join(hero)
print(hero_join)

#By using the .split string manipulation the output will be ['Superman]
hero_split = hero.split("^")
print(hero_split)