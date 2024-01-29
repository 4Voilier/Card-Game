te = []
moy = 0
j1win = 0
j2win = 0
min = 1000000000
max = -(10^10)
partie = int(input("Combien veux tu de partie : "))
for t in range(0,partie) :
    game = []
    game2 = []
    jeu = []
    typedujeu = ['Tile','Heart','Clubs','Spades']
    typedecarte = ['Valet','Queen','King','Ace']
    for i in range (2,11) :
        jeu.append(str(i))
    for y in jeu :
        for x in typedujeu :
            game.append([y,x])
    for z in typedecarte :
        for x in typedujeu :
            game.append([z,x])
    for y in jeu :
            game2.append(y)
    for z in typedecarte :
            game2.append(z)
    import random
    random.shuffle(game)
    j1 = game[:26]
    j2 = game[26:]
    end = 1
    gameturn = 1
    while end == 1 :
        turn = 0
        j1card = j1[0]
        j2card = j2[0]   
        j1index = game2.index(j1card[0])
        j2index = game2.index(j2card[0])
        if j1card[0] == j2card[0]:
            while j1card[0] == j2card[0] :
                if len(j1) <= 4 or len(j2) <= 4 :
                    if len(j1) <= 4 :
                        te.append(gameturn)
                        end = 0
                        j2win += 1
                        if gameturn < min :
                            min = gameturn-1
                        if gameturn > max :
                            max = gameturn-1
                        break
                    if len(j2) <= 4 :
                        te.append(gameturn)
                        end = 0
                        j1win += 1
                        if gameturn < min :
                            min = gameturn-1
                        if gameturn > max :
                            max = gameturn-1
                        break
                    break
                else :
                    j1combat = [j1.pop(0)] + [j1.pop(1)] + [j1.pop(2)]
                    j2combat = [j2.pop(0)] + [j2.pop(1)] + [j2.pop(2)]
                    j1card = j1combat[-1]
                    j2card = j2combat[-1]
                    if game2.index(j2card[0]) < game2.index(j1card[0]):
                        j1.extend(j1combat + j2combat)
                    elif game2.index(j1card[0]) < game2.index(j2card[0]):
                        j2.extend(j1combat + j2combat)
        else:
            if j1index > j2index:
                j1.extend([j2.pop(j2.index(j2card))])
                
            elif j1index < j2index:
                j2.extend( [j1.pop(j1.index(j1card))])
        gameturn += 1
        if len(j1) == 0 or len(j2) == 0 :
            if len(j1) == 0 :
                te.append(gameturn-1)
                j2win += 1
            elif len(j2) == 0 :
                te.append(gameturn-1)
                j1win +=1
            if gameturn < min :
                min = gameturn-1
            if gameturn > max :
                max = gameturn-1
            break
for ine in te :
    moy += ine
moy = moy/len(te)
print(f"Il faut en moyenne {moy} tours pour gagner")
print(f"J1 a gagné {j1win} fois")
print(f"J2 a gagné {j2win} fois")
print(f"Il a fallut au minimum {min} tours pour gagner")
print(f"Il a fallut au maximum {max} tours pour gagner")