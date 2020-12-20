light = input("Jakie jest swiatlo?(green , red , yellow)")

if str(light).startswith("r"):#red
    print("Czekaj!")
elif light == 'yellow':
    print("przygotuj sie")
elif light == 'green':
    print("jedz!")
else:
    print("niewłaściwa wartość")
