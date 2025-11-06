# comentario de un solo reglon
"""
comentario
de 
varios
reglones


#poner un mensaje por consola

print("holaaa profee")

#variable(es un espacio donde guardamos un dato)

nombre ="cerati"  #  string / cadena de caracteres
edad = 55 # int = numero entero (no necesita que se pongan comillas)
e = 2.718281828 # float = numero decimal
datos_logicos = True # datos logicos / boolean (son dos estados "opuestos" por ej: true o false)


#la forma de ver si la variable esta bien (se ve en la consola)

print(nombre) 
print(edad)
print(e)
print(datos_logicos)

#type se usa para ver el tipo de dato que se usa en una variable

print (type(nombre))
print (type(edad))
print (type(e))
print (type(datos_logicos))


#input se usa para mostrar un mensaje al usuario para que guarde una variable
nombre_usuario = input ("ingrese su nombre")
print(nombre_usuario)



#operaciones basicas

suma = 7 + 2 
print(suma)

resta = 12 - 5
print(resta)

multiplicar = 4*6
print(multiplicar)

dividir = 9/3
print(dividir)

#condicionales 

nombre = "juan"

if nombre == "cerati":
    print("sos cerati")
else:
    print("no sos cerati")




#condicional con elif

edad= 43

if edad <= 12:
    print("sos una criatura todavia")
elif edad >= 13 and edad <=17 :
    print("ya sos todo un adolescente")
elif edad >=18 and edad <=30 :
    print("juventud plenaaa")
elif edad >=31 and edad <=50 :
    print("ya estamos bastante grandes con laburo y hasta un par de canas")
else:
    print("ya con nietos y toda la bola")


#desafio de la clase 2

suma = 458 + 529 + 237
print(suma)

resta = 23.53 - 12.49
print(resta)

numero1 =12
numero2 = 34

if numero1 == numero2 :
    print("entonces numero1 y numero2 son iguales")
elif numero1 > numero2 :
    print("entonces numero1 es mayor a numero2")
else :
    print("entonces numero1 es menor a numero2")


#fin del desafio de la clase 2





#listas se usan para almacenar varios datos variables (es una coleccion de datos)

#lista de bandas

nombres_de_bandas = ["soda stereo", "the beatles", "la renga", "nirvana", "joystick"]
print(nombres_de_bandas)

#lista de numeros
lista_de_numeros = [132, 4231, 843, 13, 94]
print(lista_de_numeros)

#lista mixta (pueden almacenar disntos datos juntos)
mixta = ["anakin", 42, False, 4.32]
print(mixta)

print(nombres_de_bandas[1])#sirve para encontrar solo un dato de la lista y se hace contando desde cero


#tuplas son iguales a las listas pero no se pueden editar

artistas =("cerati", "charly garcia", "spinetta") #se usa para guardar datos importantes 




#diccionario permite almacenar datos con key y value

auto = {
    "marca": "toyota",
    "modelo" : "corolla",
    "año" : 2020,
    "funcionando": True
    }


print(auto)

print(auto["año"])


#while (bucles) se usa para ejecutar varias veces un codigo si cumple con una condicion (bucle condicional)

contraseña = "papo"

intentos = 5

while intentos >  0 :
    entrada = input("Ingrese la contraseña")
    if entrada == contraseña :
        print("inicio exitoso")
        intentos=0
    else:
        intentos -= 1
        print("la contraseña es incorrecta. Te quedan", intentos)
    if intentos == 0 and entrada != contraseña:
        print("no te quedan intentos")


#for (otro tipo de bucle contado/secuencial)
import random

secreto = random.randint(1, 10) #genera un numero entero random entre el 1 y el 10
intentos = 5
ganaste = False # indica si adivino o no

print("Adivina el numero en el que estoy pensando! Te doy una pista, esta entre el uno y el diez. Tenes", intentos, "intentos")

for i in range(intentos):
    intento = int(input("Dame tu lectura mental: "))

    if intento == secreto:
        print("¡Adivinaste! Mi número era", secreto)
        ganaste = True
        break  # salís del bucle si gana
    elif intento < secreto:
        print("No adivinaste. El número es más grande!")
    else:
        print("Mi número es más chico!")

if not ganaste:
    print("Perdiste! Mi número era", secreto)


import random
 
def marca_pares():
    numero = random.randint(1, 50) 
    print("Número elegido:", numero)

    for i in range(numero + 1):
        if i % 2 == 0:
            print(i, "par")
        else:
            print(i)

marca_pares()



artistaydiscofav = {}

artista = input("Escribí tu artista favorito: ")
disco = input("Escribí tu disco favorito: ")

artistaydiscofav[artista] = disco

print("Diccionario actual:", artistaydiscofav)

clave = input("Ingresá el nombre de un artista para ver su disco: ")

if clave in artistaydiscofav:
    print("El disco de", clave, "es:", artistaydiscofav[clave])
else:
    print("Ese artista no está en el diccionario.")
"""



import streamlit as st
from groq import Groq

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(page_title="Talento Tech IA", page_icon="🤖", layout="centered")

st.title("🤖 Mi chat de IA - Talento Tech")
st.write("Bienvenido a tu primer chatbot con inteligencia artificial usando Streamlit y Groq 🚀")

# --- API KEY ---
import os
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

if api_key:
    client = Groq(api_key=api_key)

    st.subheader("💬 Escribí tu mensaje:")
    user_input = st.text_area("")

    if st.button("Enviar"):
        if user_input.strip():
            with st.spinner("Pensando..."):
                response = client.chat.completions.create(
                    model="llama-3.1-70b-versatile",
                    messages=[
                        {"role": "system", "content": "Sos una IA llamada Talento Tech IA, amigable, educativa y clara."},
                        {"role": "user", "content": user_input}
                    ]
                )
                st.success("**Respuesta del chatbot:**")
                st.write(response.choices[0].message.content)
        else:
            st.warning("Por favor, escribí algo antes de enviar.")
else:
    st.info("Ingresá tu API Key para activar el chatbot.")









