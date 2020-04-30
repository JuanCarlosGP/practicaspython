print ("BIENVENIDO A EMPAREJANDO.COM")
print("\nNecesitamos conocer algunos datos sobre ti para encontrar tu pareja ideal.")

name = input("Tu nombre:")
year = int(input("Año de nacimiento:"))
taburete = input("¿Te gusta Taburete? [Si/No] ")
age = 2020-year

print("Hola "+name+". Si no me equivoco tienes", age,"años.")

if (taburete=="Si" or taburete=="Sí"  or taburete=="si"):
    print("OK boomer, lo tuyo va a ser un caso difícil.")
else:
    print("Bueno, al menos es un comienzo. Veremos qué se puede hacer contigo.")

#Comienzo practica dos
for contador in range(1,age):
    print("Que no cumple",contador)
print("\n¡Que sí cumple",age,"!")
#Jesús, no he logrado quitar el espacio que sale antes de la ultima exclamación, hay alguna forma de hacerlo?
