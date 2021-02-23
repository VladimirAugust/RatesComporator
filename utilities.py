

def extendByOnlyUniqueValues(listTo, listFrom):
    for i in listFrom:
        if i not in listTo:
            listTo.append(i)