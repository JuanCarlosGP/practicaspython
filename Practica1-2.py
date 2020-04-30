print ("BIENVENIDO A EMPAREJANDO.COM")
print("\nNecesitamos conocer algunos datos sobre ti para encontrar tu pareja ideal.")

name = input("Tu nombre:")
year = int(input("Año de nacimiento:"))
taburete = input("¿Te gusta Taburete? [Si/No] ")

edad = 2020-year

print("Hola "+name+". Si no me equivoco tienes", edad,"años.")

if (taburete=="Si" or taburete=="Sí"  or taburete=="si"):
    print("OK boomer, lo tuyo va a ser un caso difícil.")
else:
    print("Bueno, al menos es un comienzo. Veremos qué se puede hacer contigo.")
