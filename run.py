import information as API

loc = API.Info("9OHwFcxHckgLKLRaCjIkdVr0dXDAqlO9")
data = loc.getInfo()

info = data[0]
traffic = data[1]

for item in info:
    print(item)

for item in traffic:
    print(item)
    