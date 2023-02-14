is_alive = True
escaped = False
cabinet_examined = False
snake_survived = False
items = []

print("Felébredsz egy előszobában.\n")
while is_alive and not escaped:
    door_pick = int(input("""3 ajtó áll előtted. Melyiket nyitod ki?
    1: Jobb
    2: Közép
    3: Bal\n"""))

    if door_pick == 1:  # Jobb ajtó
        examine_or_return = 1  # 1: Körülnéz, 2: Visszamegy a hallba
        print("Belépsz a jobb oldali szobába. ")
        while examine_or_return != 2:  # A jobb szobába jövünk vissza egész addig amíg egyszer nem választ 2-t a játékos
            examine_or_return = int(input("""Előtted egy ágy, egy szekrény és egy ablak. 
            1: Körülnézel
            2: Visszatérsz a hallba\n"""))

            if examine_or_return == 1:
                what_to_examine = int(input("""Mit vizsgálnál meg?
                1: Ágy
                2: Szekrény
                3: Ablak\n"""))
                if what_to_examine == 1:
                    print("Ez egy nagyon kényelmes ágy. De most nincs időd aludni.\n")
                elif what_to_examine == 2:
                    if cabinet_examined:
                        print("Itt találtál korábban ellenmérget.\n")
                    else:
                        print("Találtál egy üvegcsét 'ellenméreg' felirattal. Zsebre vágtad.\n")
                        items.append("antivenom")
                        cabinet_examined = True
                elif what_to_examine == 3:
                    print("Az ablakon túl csak vakító sötétséget látsz. Megijedsz, és nem merészkedsz közelebb.\n")

    elif door_pick == 2:  # Középső ajtó
        if "key" in items:
            print("Sikeresen megmenekültél a végzet karmai közül. Generációkon át fogják a balladádat énekelni. Gratulálok!")
            escaped = True
        else:
            print("Az ajtó zárva, ráadásul valami igen böszme kulccsal.\n")

    elif door_pick == 3:  # Bal ajtó
        if snake_survived:
            print("Bekukkantasz a bal szobába, ahol hősiesen megküzdöttél a szörnyeteggel. Büszkeség tölt el, hogy milyen elegánsan kiütötted a fenevadat.\n")
        else:
            sneak_or_return = int(input("""Ahogy belépsz a bal oldali szobába, egy szunnyadó mérgeskígyóval találod szembe magad.\n
                        1: Megpróbálsz elosonni mellette
                        2: Visszatérsz a hallba\n"""))

            if sneak_or_return == 1:
                print("A kígyó észrevesz, és villámgyorsan megmar. Megragadod a szörnyeteget a farkánál fogva, és a falnak vágod. Az ütés erejétől bekábul, és felköhög egy kulcsot.")
                if "antivenom" in items:
                    print("Gyors gondolkodással beadod magadnak az ellenmérget, majd egy óra kínkeserves vergődés után talpraállsz, és a kulcsot felvéve elhagyod a szobát.\n")
                    items.append("key")
                    snake_survived = True
                else:
                    print("Azonban ez nem segít rajtad, ahogy a méreg eltelíti a tested. Mintha égnének a vénáid, kínkeserves vergődés mellett elpatkolsz.")
                    is_alive = False

if escaped:
    print("És boldogan éltél, amíg 2 hét múlva bele nem estél egy hasonlóan ostoba csapdába.")
if not is_alive:
    print("Sajnos elhunytál nemes küldetéseden. De nem baj, mert az emlékezeted mindig velünk marad.")