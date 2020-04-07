f = open('desks.txt', "rw+")
map = f.read()
desk_x = []
desk_y = []
desks_num = 0
for i in range(len(map)):
    if(map[i+1] == 'E'):
        break
    if(map[i] == '\n'):
        i += 1
        desk_x.append(ord(map[i]) - 48)
        i += 1
        while map[i] != ',':
            desk_x[desks_num] *= 10
            desk_x[desks_num] += ord(map[i]) - 48
            i += 1
        i += 1
        desk_y.append(ord(map[i]) - 48)
        i += 1
        while map[i] != '\n':
            desk_y[desks_num] *= 10
            desk_y[desks_num] += ord(map[i]) - 48
            i += 1
        i -= 1
        desks_num += 1
