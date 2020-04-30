abc = 'abcdefghijklmnopqrstuvwxyz'

print("BIENVENIDO A MI CIFRADOR CÉSAR")

texto_claro=input("Escribe el texto a cifrar:")
clave=int(input("Escribe la clave de cifrado (un número del 1 al 27):"))

def cifracesar(texto_claro,clave):
    texto_cifrado=""

    for letra in texto_claro:
        nueva_posicion = abc.find(letra) + clave
        letra_cifrada = int(nueva_posicion) % len(abc)
        texto_cifrado = texto_cifrado + str(abc[letra_cifrada])
    return texto_cifrado

cifrado=cifracesar(texto_claro,clave)
print("\nEl mensaje descifrado es:",cifrado)
