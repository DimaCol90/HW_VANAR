class English:
    #properties
    
    alphabet='latin'
    total_words=170_000
    geography='globally'

    def sayHi():
        print("Hello")

    def sayBye():
        print("Bye")

    def lovePython():
        print("I love Python programming language")


class Romanian:
    alphabet='latin'
    total_words=70_000
    geography='South-Eastern Europe'

    def sayHi():
        print("Salut")

    def sayBye():
        print("Pa")
    
    def lovePython():
        print("Imi place limbajul de programare Piton")

class French:
    alphabet='latin'
    total_words=120_000
    geography='Western coast, Europe'

    def sayHi():
        print("Salut")

    def sayBye():
        print("Au revoir")
    
    def lovePython():
        print("J'aime le langage de programmation Python")

print('En has', English.total_words,'words')

English.sayHi()
English.sayBye()
print(f"English is practiced {English.geography}")
Romanian.sayHi() 
Romanian.sayBye()           

French.sayHi
French.sayBye
print(f"French is practiced in {French.geography}")

#HW1: add another property for each language
#HW2: add another class for a language
