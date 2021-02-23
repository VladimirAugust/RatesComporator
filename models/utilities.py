def appendToMapsList(map, key, data):
    if key in map:
        map[key].append(data)
    else:
        map[key] = [data]