import re

def fName(name):
    fname = name[name.find('=') + 1:]
    fname = (fname[:fname.find('+')] if '+' in fname else fname)
    return fname

def lName(name):
    lname = name[name.find('=') + 1:]
    lname = (lname[:lname.find('+')] if '+' in lname else lname)
    return lname

def idName(idName):
    id = idName[idName.find('=') + 1:]
    return int(id)

def addData(name, nomes):
    fname = name[0]
    fname = fName(fname)
    lname = name[1]
    lname = lName(lname)
    nomes.append([fname, lname])
    return nomes

def updateData(name, nomes):
    id = name[0]
    id = idName(id)
    fname = name[1]
    fname = fName(fname)
    lname = name[2]
    lname = lName(lname)
    for i in range(len(nomes)):
        if int(id) == i:
            nomes[i] = [fname, lname]

    return nomes

def removeData(name, nomes):
    id = name[0]
    id = idName(id)
    for i in range(len(nomes)):
        if int(id) == i:
            nomes.pop(i)

    return nomes

def filterDataToArray(data, nomes):
    name = re.split('&', data)

    if 'new' in name[0]:
        return(addData(name, nomes))
    elif 'update' in name[0]:
        return(updateData(name, nomes))
    elif 'delete' in name[0]:
        return(removeData(name, nomes))
