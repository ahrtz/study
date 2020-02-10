def turn(gear,dir):
    if dir == 1:
        a=gear.pop(len(gear)-1)
        gear.insert(0,a)
        return gear
    elif dir == -1:
        a=gear.pop(0)
        gear.append(a)
        return gear

times=[[1,1],[1,-1]]
gear=[[0,1,2,5,4,5],[2,3,5,1,6,4,8]]
print(turn(gear[0],times[0][1]))