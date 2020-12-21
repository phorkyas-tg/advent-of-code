def CountIngredientsWithoutAllergens(puzzleInput):
    ingredients = {}
    allergens = {}

    for line in puzzleInput.splitlines():
        ingred, allerg = line.split("(")
        allerg = allerg.replace(")", "").replace(",", "")
        allerg = allerg.strip().split()[1:]
        ingred = ingred.strip().split()

        for a in allerg:
            if a not in allergens:
                allergens[a] = ingred.copy()
            else:
                aTemp = []
                for i in ingred:
                    if i in allergens[a]:
                        aTemp.append(i)
                allergens[a] = aTemp.copy()

        for i in ingred:
            ingredients.setdefault(i, 0)
            ingredients[i] += 1

    # remove allergen containing ingredients
    for ing in allergens.values():
        for i in ing:
            if i in ingredients:
                ingredients.pop(i)

    return sum(ingredients.values())


def GetDangerousIngredient(puzzleInput):
    allergens = {}

    for line in puzzleInput.splitlines():
        ingred, allerg = line.split("(")
        allerg = allerg.replace(")", "").replace(",", "")
        allerg = allerg.strip().split()[1:]
        ingred = ingred.strip().split()

        for a in allerg:
            if a not in allergens:
                allergens[a] = ingred.copy()
            else:
                aTemp = []
                for i in ingred:
                    if i in allergens[a]:
                        aTemp.append(i)
                allergens[a] = aTemp.copy()

    dangerDict = {}
    while len(allergens) > 0:
        for key, aList in allergens.items():
            if len(aList) == 1:
                dangerIng = aList[0]
                dangerDict.setdefault(key, dangerIng)
                for a in allergens.values():
                    try:
                        a.remove(dangerIng)
                    except ValueError:
                        pass
                allergens.pop(key)
                break

    allergens = list(dangerDict.keys())
    allergens.sort()
    dangerList = [dangerDict[d] for d in allergens]

    return ",".join(dangerList)
