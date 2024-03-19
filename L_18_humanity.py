class Humanity:
    people=8_000_000_000
    planets='Earth'
    
    races=["white","asian","negroids","eskimos"]
    using_technology=True
    senses=5
    emotional=True


    def dailyBirth():
        return(400_000)
    def dailyDeath():
        return(380_000)
    
growth=0    

print("Humanity place before 2050:",Humanity.planets)

Humanity.planets = [Humanity.planets,"Moon","Mars"]

print("Humanity place after 2050:",Humanity.planets)

add=input("Do you want to add more planers where humanity lives?(y/n) ")=="y"

while add:
    Humanity.planets.append(input("What other planet? "))

    print("Humanity planets after 2080:")
    for planet in Humanity.planets:
        
        print(planet,end=" ")


    add=input("\nDo you want to add more planets? (y/n) ")=="y"

print(f"Humanity in 2024: {Humanity.people}")

for day in range(365):
    growth+=Humanity.dailyBirth() - Humanity.dailyDeath()

print(f"Humanity growth per year(considering death rate): {growth}")    
