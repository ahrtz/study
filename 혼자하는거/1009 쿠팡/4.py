def find_route(depar,dest,road_dict):
    cnt=0
    start_point=[depar]
    while start_point:
        sp=start_point.pop(0)
        if sp in road_dict:
            for i in road_dict[sp]:
                if i == dest:
                    cnt+=1
                else:
                    start_point.append(i)
    return cnt
def sol(depar,hub,dest,roads):
    road_dict=dict()
    for i in roads:
        if i[0] in road_dict:
            road_dict[i[0]].append(i[1])
        else:
            road_dict[i[0]] = [i[1]]
    print(road_dict)
    depar_to_hub = find_route(depar,hub,road_dict)
    print(depar_to_hub)
    if depar_to_hub==0:
        return 0
    hub_to_depar= find_route(hub,dest,road_dict)

    return depar_to_hub*hub_to_depar

depar = "ULSAN"
hub = "SEOUL"
dest= "BUSAN"

roads = [["SEOUL","DAEJEON"],["ULSAN","BUSAN"],["DAEJEON","ULSAN"],["DAEJEON","GWANGJU"],["SEOUL","ULSAN"],["DAEJEON","BUSAN"],["GWANGJU","BUSAN"]]

print(sol(depar,hub,dest,roads))