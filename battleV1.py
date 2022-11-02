import pygame
import random

pygame.init()

surface = pygame.display.set_mode((200, 150))
pygame.display.set_caption("Pokemon Showdown!")

white = (255, 255, 255)
black = (0, 0, 0)

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


file = open("allyTeam.txt", "w")
file.close()
file = open("enemyTeam.txt", "w")
file.close()


for v in range(1):
    pokemonId = input("Enter the id of the pokemon you want to use: ")
    pokemonLevel = int(input("Enter the level of the pokemon: "))
    while pokemonLevel > 100:
        pokemonLevel = int(input("Enter the level of the pokemon: "))
    pokeList = []
    with open("pokemonData.txt", "r") as file:
        lines = file.readlines()[int(pokemonId) - 1: int(pokemonId)][0]
        split = lines.split(",")
        pokeList.extend(split)
        pokeList[-1] = pokeList[-1].strip()
        pokeList.append(pokemonLevel)
    currentMoveList = []
    for i in range(4):
        moveChoiceValidity = False
        while not moveChoiceValidity:
            moveChoice = input("Enter a move you want to put on your pokemon: ")
            with open("pokemonData.txt", "r") as file:
                lines = file.readlines()[int(pokemonId) - 1: int(pokemonId)]
                lines = lines[0].split(",")
                if moveChoice in lines[12: -1]:
                    if moveChoice in currentMoveList[0: -1]:
                        print("Move already learned")
                    else:
                        moveChoiceValidity = True
                        print("Move Learned")
                else:
                    print("This pokemon cannot learn this move")
        currentMoveList.append(moveChoice)
    pokeList.extend(currentMoveList)
    baseHP = float(pokeList[4])
    baseAtk = float(pokeList[5])
    baseDef = float(pokeList[6])
    baseSpAtk = float(pokeList[7])
    baseSpDef = float(pokeList[8])
    baseSpe = float(pokeList[9])
    pokeList[4] = round(((2 * baseHP * pokemonLevel) / 100) + pokemonLevel + 10)
    pokeList[5] = round(((2 * baseAtk * pokemonLevel) / 100) + 5)
    pokeList[6] = round(((2 * baseDef * pokemonLevel) / 100) + 5)
    pokeList[7] = round(((2 * baseSpAtk * pokemonLevel) / 100) + 5)
    pokeList[8] = round(((2 * baseSpDef * pokemonLevel) / 100) + 5)
    pokeList[9] = round(((2 * baseSpe * pokemonLevel) / 100) + 5)

    with open("allyTeam.txt", "a") as file:
        for n in range(12):
            file.write(str(pokeList[n]) + ",")
        file.write(str(pokemonLevel) + ",")
        for r in range(4):
            file.write(currentMoveList[r] + ",")
        file.write("\n")

for q in range(1):
    intRandomEnemy = random.randint(1,493)
    randomEnemy = str(intRandomEnemy)
    enemyLevel = int(input("Enter the level of pokemon you want to fight: "))
    pokeList2 = []
    with open("pokemonData.txt", "r") as file:
        lines = file.readlines()[intRandomEnemy - 1: intRandomEnemy][0]
        split = lines.split(",")
        pokeList2.extend(split)
        pokeList2[-1] = pokeList2[-1].strip()
        pokeList2.append(enemyLevel)
    currentEnemyMoveList = []
    for i in range(4):
        with open("pokemonData.txt", "r") as file:
            lines = file.readlines()[intRandomEnemy - 1: intRandomEnemy]
            split = lines[0].split(",")
            randomEnemyMoveSet = random.randint(12, len(split))
            currentEnemyMoveList.append(split[randomEnemyMoveSet])

    baseHPEnemy = float(pokeList2[4])
    baseAtkEnemy = float(pokeList2[5])
    baseDefEnemy = float(pokeList2[6])
    baseSpAtkEnemy = float(pokeList2[7])
    baseSpDefEnemy = float(pokeList2[8])
    baseSpeEnemy = float(pokeList2[9])
    pokeList2[4] = round(((2 * baseHPEnemy * enemyLevel) / 100) + enemyLevel + 10)
    pokeList2[5] = round(((2 * baseAtkEnemy * enemyLevel) / 100) + 5)
    pokeList2[6] = round(((2 * baseDefEnemy * enemyLevel) / 100) + 5)
    pokeList2[7] = round(((2 * baseSpAtkEnemy * enemyLevel) / 100) + 5)
    pokeList2[8] = round(((2 * baseSpDefEnemy * enemyLevel) / 100) + 5)
    pokeList2[9] = round(((2 * baseSpeEnemy * enemyLevel) / 100) + 5)
    pokeList2[11] = pokeList2[11].strip()

    with open("enemyTeam.txt", "a") as file:
        for n in range(12):
            file.write(str(pokeList2[n]) + ",")
        file.write(str(enemyLevel) + ",")
        for r in range(4):
            file.write(currentEnemyMoveList[r] + ",")
        file.write("\n")


class Move:
    def __init__(self, allyList, enemyList, ally, enemy, pokeSwitch, levelAlly, levelEnemy):
        self.allyList = allyList
        self.enemyList = enemyList
        self.ally = ally
        self.enemy = enemy
        self.pokeSwitch = pokeSwitch
        self.levelAlly = levelAlly
        self.levelEnemy = levelEnemy

    def Damage(self, allyList, enemyList, ally, enemy, levelAlly, levelEnemy):
        self.allyList = allyList
        self.enemyList = enemyList
        self.ally = ally
        self.enemy = enemy
        self.levelAlly = levelAlly
        self.levelEnemy = levelEnemy

        effectiveness = type_effectiveness[types[ally[1]]][types[enemyList[2]]] * \
                        type_effectiveness[types[ally[1]]][types[enemyList[3]]]

        if ally[2] == "physical":
            moveDamage = True
            contact = True
            attack = float(allyList[5])
            defense = float(enemyList[6])
        elif ally[2] == "special":
            moveDamage = True
            contact = False
            attack = float(allyList[7])
            defense = float(enemyList[8])
        elif ally[2] == "status":
            moveDamage = False
            contact = False
        critical = random.randint(0, 100)
        if critical < 7:
            checkCritical = 2
        else:
            checkCritical = 1
        if allyList[2] or allyList[3] == ally[2]:
            stab = 1.5
        else:
            stab = 1
        if moveDamage:
            damage = ((((((2 * float(levelAlly)) / 5) + 2) * float(ally[4]) * (
                    attack / defense)) / 50) + 2) * checkCritical * (
                             random.randint(85, 100) / 100) * stab * effectiveness  # *burn/frostbite
        else:
            damage = 0
        print(allyList[1], " used ", ally[0], "!")
        if checkCritical == 2:
            print("Critical hit!")
        if effectiveness == 2 or effectiveness == 4:
            print("It's super effective!")
        if effectiveness == 0.5 or effectiveness == 0.25:
            print("It's not very effective...")
        return damage

    def moveSelection(self, allyList, enemyList, pokeSwitch, ally, enemy):
        self.allyList = allyList
        self.enemyList = enemyList
        self.pokeSwitch = pokeSwitch
        self.ally = ally
        self.enemy = enemy

        moveList = []
        moveList2 = []

        randomMove = random.randint(12, 15)
        if not pokeSwitch:
            validMove = False
            moveSelection = input("Enter the name of the move you want to use: ")
            while not validMove:
                if moveSelection in ally:
                    with open("moveData.txt","r") as file:
                        for i, selectedMove in enumerate(file):
                            if moveSelection in selectedMove:
                                moveList.extend(selectedMove.split(","))
                                validMove = True
                else:
                    print("That isn't a move you selected")
                    moveSelection =input("Enter the name of the move you want to use: ")
                    validMove = False

        if pokeSwitch:
            moveList = ["0", "switch", "none", "status", "1000000", "0", "100", "10", "0", "None", "0", "0", "0", "0", "0"]

        enemyMove = enemy[randomMove]
        with open("moveData.txt", "r") as file:
            for i, selectedEnemyMove in enumerate(file):
                if enemyMove in selectedEnemyMove:
                    moveList2.extend(selectedEnemyMove.split(","))

        return moveList, moveList2


class Ally:
    def __init__(self, surface, name, type1, type2, hitPoints, attack, defense, specialAttack, specialDefense, speed,
                 backSprite, damage, currentHealth):
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
        self.damage = damage
        self.currentHealth = currentHealth

    def draw(self):
        image = pygame.image.load(self.backSprite)
        self.surface.blit(image, (0, 50))

    def health(self, damage, currentHealth):
        self.damage = damage
        self.currentHealth = currentHealth
        currentHealth = float(currentHealth) - damage
        return currentHealth


class Enemy:
    def __init__(self, surface, name, type1, type2, hitPoints, attack, defense, specialAttack, specialDefense, speed,
                 frontSprite, damage, currentHealth):
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
        self.damage = damage
        self.currentHealth = currentHealth

    def draw(self):
        image = pygame.image.load(self.frontSprite)
        self.surface.blit(image, (100, 10))

    def health(self, damage, currentHealth):
        self.damage = damage
        self.currentHealth = currentHealth
        currentHealth = float(currentHealth) - damage
        return currentHealth


class Infobox:
    def __init__(self, health, name, level, height, width):
        self.health = health
        self.name = name
        self.level = level

    def draw(self, health, name, level, height, width):
        pass
    
        
def setup():
    pokeSwitch = False
    allyDamage = 0
    enemyDamage = 0
    allyFainted = False
    enemyFainted = False
    moveList = []
    moveList2 = []
    currentAllyHealth = float(pokeList[4])
    currentEnemyHealth = float(pokeList2[4])

    allyPokemon = Ally(surface, pokeList[1], pokeList[2], pokeList[3], pokeList[4], pokeList[5], pokeList[6], pokeList[7],
                   pokeList[8], pokeList[9], pokeList[10], allyDamage, currentAllyHealth)
    enemyPokemon = Enemy(surface, pokeList2[1], pokeList2[2], pokeList2[3], pokeList2[4], pokeList2[5], pokeList2[6],
                     pokeList2[7], pokeList2[8], pokeList2[9], pokeList2[11], enemyDamage, currentEnemyHealth)
turnCount = 0
run = True
while run:
    surface.fill(white)
    allyPokemon.draw()
    enemyPokemon.draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()

    turnMove = Move(pokeList, pokeList2, moveList, moveList2, pokeSwitch, pokemonLevel, enemyLevel)
    battleChoice = input("fight or switch: ")
    if battleChoice == "fight":
        pokeSwitch = False
    elif battleChoice == "switch":
        pokeSwitch = True
        print(type(pokeSwitch))
    moveList, moveList2 = turnMove.moveSelection(moveList, moveList2, pokeSwitch, pokeList, pokeList2)
    if moveList[1] == "switch":
        newPokemon = int(input("Enter the number of the line of the pokemon you want to switch to: "))
        with open("allyTeam.txt", "r") as file:
            line = file.readlines()[newPokemon - 1: newPokemon]
            pokeList = line[0].split(",")
        allyPokemon = Ally(surface, pokeList[1], pokeList[2], pokeList[3], pokeList[4], pokeList[5], pokeList[6],
                           pokeList[7],
                           pokeList[8], pokeList[9], pokeList[10], allyDamage, currentAllyHealth)
        print(pokeList)

    if moveList[7] > moveList2[7]:
        print("You moved first")
        pokeDamage = turnMove.Damage(pokeList, pokeList2, moveList, moveList2, pokemonLevel, enemyLevel)
        currentEnemyHealth = enemyPokemon.health(pokeDamage, currentEnemyHealth)
        if currentEnemyHealth < 1:
            print("you win")
            enemyFainted = True
        if not enemyFainted:
            pokeDamage2 = turnMove.Damage(pokeList2, pokeList, moveList2, moveList, enemyLevel, pokemonLevel)
            currentAllyHealth = allyPokemon.health(pokeDamage2, currentAllyHealth)
            if currentAllyHealth < 1:
                print("you lose")
                allyFainted = True
        if enemyFainted:
            pokeDamage2 = 0

    elif moveList2[7] < moveList[7]:
        print("The enemy moved first")
        pokeDamage2 = turnMove.Damage(pokeList2, pokeList, moveList2, moveList, enemyLevel, pokemonLevel)
        currentAllyHealth = allyPokemon.health(pokeDamage2, currentAllyHealth)
        if currentAllyHealth < 1:
            print("you lose")
            allyFainted = True
        if not allyFainted:
            pokeDamage = turnMove.Damage(pokeList, pokeList2, moveList, moveList2, pokemonLevel, enemyLevel)
            currentEnemyHealth = enemyPokemon.health(pokeDamage, currentEnemyHealth)
            if currentEnemyHealth < 1:
                print("you win")
                enemyFainted = True
        if allyFainted:
            pokeDamage = 0

    else:
        if pokeList[9] > pokeList2[9]:
            print("You moved first")
            pokeDamage = turnMove.Damage(pokeList, pokeList2, moveList, moveList2, pokemonLevel, enemyLevel)
            currentEnemyHealth = enemyPokemon.health(pokeDamage, currentEnemyHealth)
            if currentEnemyHealth < 1:
                print("you win")
                enemyFainted = True
            if not enemyFainted:
                pokeDamage2 = turnMove.Damage(pokeList2, pokeList, moveList2, moveList, enemyLevel, pokemonLevel)
                currentAllyHealth = allyPokemon.health(pokeDamage2, currentAllyHealth)
                if currentAllyHealth < 1:
                    print("you lose")
                    allyFainted = True
            if enemyFainted:
                pokeDamage2 = 0

        elif pokeList2[9] > pokeList[9]:
            print("The enemy moved first")
            pokeDamage2 = turnMove.Damage(pokeList2, pokeList, moveList2, moveList, enemyLevel, pokemonLevel)
            currentAllyHealth = allyPokemon.health(pokeDamage2, currentAllyHealth)
            if currentAllyHealth < 1:
                print("you lose")
                allyFainted = True
            if not allyFainted:
                pokeDamage = turnMove.Damage(pokeList, pokeList2, moveList, moveList2, pokemonLevel, enemyLevel)
                currentEnemyHealth = enemyPokemon.health(pokeDamage, currentEnemyHealth)
                if currentEnemyHealth < 1:
                    print("you win")
                    enemyFainted = True
            if allyFainted:
                pokeDamage = 0

        else:
            randomTurn = random.randint(1, 2)
            if randomTurn == 1:
                print("You moved first")
                pokeDamage = turnMove.Damage(pokeList, pokeList2, moveList, moveList2, pokemonLevel, enemyLevel)
                currentEnemyHealth = enemyPokemon.health(pokeDamage, currentEnemyHealth)
                if currentEnemyHealth < 1:
                    print("you win")
                    enemyFainted = True
                if not enemyFainted:
                    pokeDamage2 = turnMove.Damage(pokeList2, pokeList, moveList2, moveList, enemyLevel, pokemonLevel)
                    currentAllyHealth = allyPokemon.health(pokeDamage2, currentAllyHealth)
                    if currentAllyHealth < 1:
                        print("you lose")
                        allyFainted = True
                if enemyFainted:
                    pokeDamage2 = 0

            else:
                print("The enemy moved first")
                pokeDamage2 = turnMove.Damage(pokeList2, pokeList, moveList2, moveList, enemyLevel, pokemonLevel)
                currentAllyHealth = allyPokemon.health(pokeDamage2, currentAllyHealth)
                if currentAllyHealth < 1:
                    print("you lose")
                    allyFainted = True
                if not allyFainted:
                    pokeDamage = turnMove.Damage(pokeList, pokeList2, moveList, moveList2, pokemonLevel, enemyLevel)
                    currentEnemyHealth = enemyPokemon.health(pokeDamage, currentEnemyHealth)
                    if currentEnemyHealth < 1:
                        print("you win")
                        enemyFainted = True
                if allyFainted:
                    pokeDamage = 0
    turnCount += 1

    print("Your Health: ", currentAllyHealth)
    print("Enemy Health: ", currentEnemyHealth)
    print("Your Damage: ", pokeDamage)
    print("Their Damage: ", pokeDamage2)
    print("Turn: ", turnCount)

    if allyFainted or enemyFainted:
        run = False

    if not run:
        pygame.quit()
    pygame.display.update()
