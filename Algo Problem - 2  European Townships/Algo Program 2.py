with open('input.txt', 'r') as fp:
    fileInput = fp.readlines()

with open('output.txt', 'w') as fp:
    pass

townShips = int(fileInput[0])
allHouses = fileInput[1:]

for townShip in range(townShips):
    houseNo = eval(allHouses[0])

    accentQty = 0
    regularQty = 0
    totalHours = 0
    walls = 0

    houses = allHouses[1:houseNo + 1]
    for house in houses:
        bedRooms, roofBeds, standardRooms, halls = eval(f'[{house.strip()}]')
        walls += (halls * 6) + (standardRooms * 4) + (roofBeds * 3)

    accentWalls = walls * 1 / 3
    regularWalls = walls - accentWalls
    
    totalHours = f'{round((accentWalls * 2.5) + (regularWalls * 3.25), 2):.2f}'
    accentQty = f'{round(accentWalls * 1.5, 2):.2f}'
    regularQty = f'{round(regularWalls * 2.25, 2):.2f}'
    
    with open('output.txt', 'a') as fp:
        fp.write(f'Case #{townShip + 1}: {totalHours}, {accentQty}, {regularQty}\n')
    allHouses = allHouses[houseNo + 1:]