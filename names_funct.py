def hi(lang,name):
    if lang =="en":
        print(f"Hello, {name}")
    elif lang=="ro":
        print(f"salut, {name}")
    elif lang=="ru":
        print(f"Привет, {name}")

hi("en","John")
hi("ro","Ion")
hi("ru","Леонид")
