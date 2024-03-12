def removeSpace(name):
    name_=name.strip()
    return name_

def fixCase(name):
    name_=name.capitalize()
    return name_

name_rem=removeSpace("   DOrIn      ")   

name_rem=fixCase(name_rem)

print(f"|{name_rem}|")

