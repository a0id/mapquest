address = "7 Shelley Lane"
city = "West Harrison"
state = "NY"
start = [address,city, state]

for x in range(len(start)):
    for y in range(len(start[x])):
        if start[x][y] == " ":
            start[x] = start[x][y].replace(" ", "+")
            print(start[x])