print ("BIENVENIDO A EMPAREJANDO.COM")
print("\nNecesitamos conocer algunos datos sobre ti para encontrar tu pareja ideal.")

name = input("Tu nombre:")
year = int(input("Año de nacimiento:"))
tab = input("¿Te gusta Taburete? [Si/No] ")

age = 2020-year

print("Hola "+name+". Si no me equivoco tienes", age,"años.")

if (tab=="Si" or tab=="Sí"  or tab=="si"):
    print("OK boomer, lo tuyo va a ser un caso difícil.")
else:
    print("Bueno, al menos es un comienzo. Veremos qué se puede hacer contigo.")
#Comienzo practica cuatro
usuario={"nombre":name,"edad":age,"taburete":tab}
for dato in usuario.values():
    print(dato)
