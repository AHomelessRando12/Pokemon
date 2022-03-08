import pygame
import random

pygame.init()

surface = pygame.display.set_mode((200, 150))
pygame.display.set_caption("Pokemon Showdown!")

white = (255, 255, 255)
black = (0, 0, 0)

pokemonId = input("Enter the id of the pokemon you want to use: ")
pokemonLevel = int(input("Enter the level of the pokemon: "))
pokeList = []
with open("pokemondata.txt", "r") as file:
    line = True
    lineList = []
    while line != "":
        line = file.readline()
        if line != "":
            split = line.split(",")
            lineList.append(split)
    for i in range(len(lineList)):
        if lineList[i][0] == pokemonId:
            for j in range(len(lineList[i])):
                pokeList.append(lineList[i][j])
pokeList.append(pokemonLevel)

randomEnemy = str(random.randint(1, 9))

pokeList2 = []
with open("pokemondata.txt", "r") as file:
    line = True
    lineList = []
    while line != "":
        line = file.readline()
        if line != "":
            split = line.split(",")
            lineList.append(split)
        for i in range(len(lineList)):
            if lineList[i][0] == randomEnemy:
                print("Hello")
                for j in range(len(lineList[i])):
                    pokeList2.append(lineList[i][j])
                    print(pokeList2)


class Move:
    def __init__(self, name, type, contact, pp, power, accuracy, status, effect, stat, level, attack, defense,
                 pokeType, allyList, enemyList):
        self.name = name
        self.type = type
        self.contact = contact
        self.pp = pp
        self.power = power
        self.accuracy = accuracy
        self.status = status
        self.effect = effect
        self.stat = stat
        self.level = level
        self.attack = attack
        self.defense = defense
        self.pokeType = pokeType
        self.allyList = allyList
        self.enemyList = enemyList

    def allyDamage(self, allyList, enemyList):
        self.allyList = allyList
        self.enemyList = enemyList
        moveList = []
        moveId = input("Enter the id of the move you want to use: ")
        with open("movedata.txt", "r") as file:
            line = True
            lineList = []
            while line != "":
                line = file.readline()
                if line != "":
                    split = line.split(",")
                    lineList.append(split)
                for i in range(len(lineList)):
                    if lineList[i][0] == moveId:
                        print("Hello")
                        for j in range(len(lineList[i])):
                            moveList.append(lineList[i][j])
                            print(moveList)

        types = {"normal": 0,
                 "fire": 1,
                 "water": 2,
                 "electric": 3,
                 "grass": 4,
                 "ice": 5,
                 "fighting": 6,
                 "poison": 7,
                 "ground": 8,
                 "flying": 9,
                 "psychic": 10,
                 "bug": 11,
                 "rock": 12,
                 "ghost": 13,
                 "dragon": 14,
                 "dark": 15,
                 "steel": 16,
                 "fairy": 17,
                 "none": 18
                 }

        type_effectiveness = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0.5, 0, 1, 1, 0.5, 1, 1],
                              [1, 0.5, 0.5, 1, 2, 2, 1, 1, 1, 1, 1, 2, 0.5, 1, 0.5, 1, 2, 1, 1],
                              [1, 2, 0.5, 1, 0.5, 1, 1, 1, 2, 1, 1, 1, 2, 1, 0.5, 1, 1, 1, 1],
                              [1, 1, 2, 0.5, 0.5, 1, 1, 1, 0, 2, 1, 1, 1, 1, 0.5, 1, 1, 1, 1],
                              [1, 0.5, 2, 1, 0.5, 1, 1, 0.5, 2, 0.5, 1, 0.5, 2, 1, 0.5, 1, 0.5, 1, 1],
                              [1, 0.5, 0.5, 1, 2, 0.5, 1, 1, 2, 2, 1, 1, 1, 1, 2, 1, 0.5, 1, 1],
                              [2, 1, 1, 1, 1, 2, 1, 0.5, 1, 0.5, 0.5, 0.5, 2, 0, 1, 2, 2, 0.5, 1],
                              [1, 1, 1, 1, 2, 1, 1, 0.5, 0.5, 1, 1, 1, 0.5, 0.5, 1, 1, 0, 2, 1],
                              [1, 2, 1, 2, 0.5, 1, 1, 2, 1, 0, 1, 0.5, 2, 1, 1, 1, 2, 1, 1],
                              [1, 1, 1, 0.5, 2, 1, 2, 1, 1, 1, 1, 2, 0.5, 1, 1, 1, 0.5, 1, 1],
                              [1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 0.5, 1, 1, 1, 1, 0, 0.5, 1, 1],
                              [1, 0.5, 1, 1, 2, 1, 0.5, 0.5, 1, 0.5, 2, 1, 1, 0.5, 1, 2, 0.5, 0.5, 1],
                              [1, 2, 1, 1, 1, 2, 0.5, 1, 0.5, 2, 1, 2, 1, 1, 1, 1, 0.5, 1, 1],
                              [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 0.5, 1, 1, 1],
                              [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 0.5, 0, 1],
                              [1, 1, 1, 1, 1, 1, 0.5, 1, 1, 1, 2, 1, 1, 2, 1, 0.5, 1, 0.5, 1],
                              [1, 0.5, 0.5, 0.5, 1, 2, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 0.5, 2, 1],
                              [1, 0.5, 1, 1, 1, 1, 2, 0.5, 1, 1, 1, 1, 1, 1, 2, 2, 0.5, 1, 1],
                              [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

        effectiveness = type_effectiveness[types[moveList[2]]][types[pokeList2[2]]] * \
                        type_effectiveness[types[moveList[2]]][types[pokeList2[3]]]

        if moveList[3] == "physical":
            moveDamage = True
            contact = True
            attack = float(allyList[5])
            defense = float(enemyList[6])
        elif moveList[3] == "special":
            moveDamage = True
            contact = False
            attack = float(allyList[7])
            defense = float(enemyList[8])
        critical = random.randint(0, 100)
        if critical < 7:
            checkCritical = True
        else:
            checkCritical = 1
        if allyList[2] or allyList[3] == moveList[2]:
            stab = 1.5
        else:
            stab = 1
        damage = ((((((2 * allyList[13]) / 5) + 2) * float(moveList[5]) * (
                attack / defense)) / 50) + 2) * checkCritical * (
                         random.randint(85, 100) / 100) * stab * effectiveness  # *burn/frostbite


class Ally:
    def __init__(self, surface, name, type1, type2, hitPoints, attack, defense, specialAttack, specialDefense, speed,
                 backSprite):
        self.surface = surface
        self.name = name
        self.type1 = type1
        self.type2 = type2
        self.hitPoints = hitPoints
        self.attack = attack
        self.defense = defense
        self.specialAttack = specialAttack
        self.specialDefense = specialDefense
        self.speed = speed
        self.backSprite = "backSprites/" + backSprite

    def draw(self):
        fainted = False
        image = pygame.image.load(self.backSprite)
        self.surface.blit(image, (0, 50))


class Enemy:
    def __init__(self, surface, name, type1, type2, hitPoints, attack, defense, specialAttack, specialDefense, speed,
                 frontSprite):
        self.surface = surface
        self.name = name
        self.type1 = type1
        self.type2 = type2
        self.hitPoints = hitPoints
        self.attack = attack
        self.defense = defense
        self.specialAttack = specialAttack
        self.specialDefense = specialDefense
        self.speed = speed
        self.frontSprite = "frontSprites/" + frontSprite

    def draw(self):
        fainted = False
        image = pygame.image.load(self.frontSprite)
        self.surface.blit(image, (100, 10))


allyPokemon = Ally(surface, pokeList[1], pokeList[2], pokeList[3], pokeList[4], pokeList[5], pokeList[6], pokeList[7],
                   pokeList[8], pokeList[9], pokeList[10])
enemyPokemon = Enemy(surface, pokeList2[1], pokeList2[2], pokeList2[3], pokeList2[4], pokeList2[5], pokeList2[6],
                     pokeList2[7], pokeList2[8], pokeList2[9], pokeList2[11])

while True:
    surface.fill(white)
    allyPokemon.draw()
    enemyPokemon.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    pygame.display.update()
