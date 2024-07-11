km = int(input())
tank = int(input())
c1 = 1
c2 = 1
oil_km = km/15
oil_km2 = km/15
while True :
    oil_km -= (tank*0.5)
    c1 += 1
    if oil_km < tank  :
        c1 += 1
        break
while True :
    oil_km2 -= (tank*0.9)
    c2 += 1
    if oil_km2 < tank  :
        break
print(c1)
print(c2)
