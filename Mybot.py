def do_turn(pw):
    dis = dis1 = 999999
    dest = dest1 = 1

    if len(pw.my_planets()) == 0:
        return

    source = maxShips(pw.my_planets())

    if len(pw.neutral_planets()) >= 1:
        dest,dis = destPlanet(pw,source,pw.neutral_planets())
    if len(pw.enemy_planets()) >= 1:
        dest1,dis1 = destPlanet(pw,source,pw.enemy_planets())


    """pw.debug(dis)
    pw.debug(dis1)"""

    if dis > dis1:
        dest = dest1


    num_ships = source.num_ships() -1

    pw.issue_order(source, dest, num_ships)



def destPlanet(pw, sorce, planets):
    dest = planets[0]
    min = pw.distance(sorce,dest)
    for planet in planets:
        dis = pw.distance(sorce,planet)

        if(dis<min):
            min = dis
            dest = planet
    return dest,min


def maxShips(planets):
    max= 0
    for planet in planets:
        sh = planet.num_ships()
        if sh > max:
            max = sh
            p = planet
        elif sh == max:
            if p.growth_rate()< planet.growth_rate():
                p = planet
    return p
