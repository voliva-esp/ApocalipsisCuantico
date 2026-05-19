def cifrar_cesar(texto, desplazamiento):
    resultado = ""

    # Pasamos a mayúsculas para simplificar la explicación en clase
    texto = texto.upper()

    for caracter in texto:
        # Solo ciframos las letras de la A a la Z
        if caracter.isalpha():
            # El código ASCII de la 'A' es 65
            origen_ascii = ord('A')

            # Pasamos el carácter a rango 0-25 (ej: 'A'=0, 'B'=1...)
            posicion_letra = ord(caracter) - origen_ascii

            # Aplicamos el desplazamiento y el módulo 26 (vuelve a empezar tras la Z)
            nueva_posicion = (posicion_letra + desplazamiento) % 26

            # Lo convertimos de vuelta a su código ASCII original
            nuevo_caracter = chr(nueva_posicion + origen_ascii)
            resultado += nuevo_caracter
        else:
            # Si es un espacio, número o signo, lo dejamos igual sin cifrar
            resultado += caracter

    return resultado


def cifrar_vigenere(texto, clave):
    resultado = ""
    for i in range(len(texto)):
        desplazamiento = int(clave[i % len(clave)])
        resultado += cifrar_cesar(texto[i], desplazamiento)
    return resultado


def descifrar_cesar(texto_cifrado, desplazamiento):
    # Descifrar es simplemente desplazar hacia el lado contrario
    return cifrar_cesar(texto_cifrado, -desplazamiento)


def descifrar_vigenere(texto_cifrado, desplazamiento):
    resultado = ""
    for i in range(len(texto_cifrado)):
        desplazamiento = int(clave[i % len(clave)])
        resultado += cifrar_cesar(texto_cifrado[i], -desplazamiento)
    return resultado


# --- Bloque de ejecución principal (Menú interactivo) ---
if __name__ == "__main__":
    print("--- DEMOSTRACIÓN: CIFRADO VIGENERE ---")
    mensaje = input("Introduce el mensaje a cifrar: ")
    clave = input("Introduce el desplazamiento, separado por espacios (ej: 3 4 5): ")
    clave = clave.split(" ")

    # Ciframos
    mensaje_cifrado = cifrar_vigenere(mensaje, clave)
    print(f"\n[+] Mensaje original: {mensaje.upper()}")
    print(f"[+] Mensaje cifrado:  {mensaje_cifrado}")

    # Desciframos para demostrar que funciona en ambos sentidos
    mensaje_descifrado = descifrar_vigenere(mensaje_cifrado, clave)
    print(f"[+] Descifrado final: {mensaje_descifrado}")
