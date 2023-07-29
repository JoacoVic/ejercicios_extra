# Copyright (C) 2023 <UTN FRA>
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import tkinter as tk
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
#El profesor OAK de pueblo paleta quiere que construyas un modelo prototipico de pokedex con algunos pokemones de prueba.

A) Para ello deberas programar el boton "Cargar Pokedex" para poder cargar 10 pokemones.
Los datos que deberas pedir para los pokemones son:
    * El nombre del pokemon
    * El tipo de su elemento (Agua, Psiquico, Electrico)
    * Poder de ataque (validar que sea mayor a 50 y menor a 200)
B) Al presionar el boton mostrar se deberan listar los pokemones y su posicion en la lista (por terminal) 
y mostrar los informe del punto C.

Del punto C solo debera realizar 3 informes. Para determinar que informe hacer, tenga en cuenta lo siguiente:
    
    Informe 1- Tome el ultimo numero de su DNI Personal (Ej 4) y realice ese informe (Ej, Realizar informe 4)

    Informe 2- Tome el ultimo numero de su DNI Personal (Ej 4), y restarselo al numero 9 (Ej 9-4 = 5). En caso de que su DNI 
    finalice con el numero 0, debera realizar el informe 9.
    
    Informe 3- Tome la suma de los ultimos dos numeros de su DNI personal, en caso de ser un numero par, tomara el numero par 
    mas chico que su ultimo digito del DNI (en caso de que su ultimo digito sea 2, resolvera el ejercicio 8). En caso contrario, si es impar, 
    tomara el numero impar posterior (en caso de que su ultimo digito sea 9, resolvera el ejercicio 1)
    En caso de que el numero sea el mismo obtenido en el informe 2, realizara el siguiente informe en la lista.
    
    
    Realiza el informe correspondiente al numero obtenido.
    
EL RESTO DE LOS INFORMES LOS PUEDE IGNORAR. 
C) NOMBRE TIPO PODER ATAQUE
    #! 0) - Cantidad de pokemones de tipo Fuego cuyo poder de pelea con un 10% extra supere los 100 puntos.
    #! 1) - Cantidad de pokemones de tipo Electrico cuyo poder de pelea con un 15% menos este entre los 100 y los 150 puntos.
    #! 2) - Nombre y Poder del pokemon de tipo electrico con el poder mas alto.
    #! 3) - Nombre y Poder del pokemon de tipo psiquico con el poder mas bajo.
    #! 4) - Porcentaje de pokemones de tipo agua con mas de 100 puntos de poder (Sobre el total de pokemones ingresados).
    #! 5) - Porcentaje de pokemones de tipo psiquico con poder de pelea inferior o igual a 150 (sobre el total de pokemones ingresados).
    #! 6) - tipo de los pokemones del tipo que mas pokemones posea. 
    #! 7) - tipo de los pokemones del tipo que menos pokemones posea. 
    #! 8) - Listado de todos los pokemones cuyo poder de pelea supere el valor promedio.
    #! 9) - el promedio de poder de todos los pokemones de tipo Electrico.
   
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA - Pokedex")
        self.minsize(320, 250)

        self.label_title = customtkinter.CTkLabel(master=self, text="Pokedex 🎮", font=("Arial", 20, "bold"))
        self.label_title.grid(row=0, column=0, columnspan=2, padx=20, pady=10)
        self.image = tk.PhotoImage(file='Logo_UTN_App.png')
        
        self.top_banner = customtkinter.CTkLabel(master = self, image = self.image, text = 'Banner')
        self.top_banner.grid_configure(row = 1, column = 0, padx = 20, pady = 5, columnspan = 2, rowspan = 1, sticky = 'we')

        self.btn_cargar = customtkinter.CTkButton(master=self, text="Cargar Pokedex", command=self.btn_cargar_pokedex_on_click)
        self.btn_cargar.grid(row=2, pady=10, columnspan=2, sticky="nsew")

        self.btn_informe_1 = customtkinter.CTkButton(master=self, text="Informe 1", command=self.btn_mostrar_informe_1)
        self.btn_informe_1.grid(row=3, pady=10, columnspan=2, sticky="nsew")
        self.btn_informe_2 = customtkinter.CTkButton(master=self, text="Informe 2", command=self.btn_mostrar_informe_2)
        self.btn_informe_2.grid(row=4, pady=10, columnspan=2, sticky="nsew")
        self.btn_informe_3 = customtkinter.CTkButton(master=self, text="Informe 3", command=self.btn_mostrar_informe_3)
        self.btn_informe_3.grid(row=5, pady=10, columnspan=2, sticky="nsew")
        # Cargar aca los pokemones
        self.lista_nombre_pokemones = []
        self.lista_poder_pokemones = []
        self.lista_tipo_pokemones = []


    def btn_mostrar_informe_1(self):
        lista = self.lista_nombre_pokemones
        i = 0

        for pokemon in lista:
            print(f"{i}, {lista[pokemon]}")
            i += 1

    
    def btn_mostrar_informe_2(self):
        alert("2","2")
    
    def btn_mostrar_informe_3(self):
        alert("3","3")
    
    def btn_cargar_pokedex_on_click(self):
    # Validamos datos: El nombre del pokemon, El tipo de su elemento (Agua, Psiquico, Electrico), Poder de ataque(validar que sea mayor a 50 y menor a 200)
        nombre_poder_mas_bajo_psiquico = None
        bandera_nombre_psiquico = True
        bandera_poder_psiquico = True

        for datos_pokemon in range(2):
            nombre_pokemon = prompt("Nombre", "Ingrese el nombre de su pokemon")
            while not nombre_pokemon or not nombre_pokemon.isalpha():
                nombre_pokemon = prompt("Error nombre", "Por favor, ingrese el nombre de su pokemon")
            tipo_pokemon = prompt("Tipo de pokemon", "Elija el tipo de su pokemon (Agua, Psiquico o Electrico)")
            while not tipo_pokemon or (tipo_pokemon != "Agua" and tipo_pokemon != "Psiquico" and tipo_pokemon != "Electrico"):
                tipo_pokemon = prompt("Error en el tipo de pokemon", "Por favor, elija el tipo de su pokemon (Agua, Psiquico o Electrico)")
            poder_ataque_pokemon = prompt("Poder de ataque", "Ingrese el poder de ataque de su pokemon (mayor a 50 y menor a 200)")
            while not poder_ataque_pokemon or not poder_ataque_pokemon.isdigit() or (int(poder_ataque_pokemon) <= 50 and int(poder_ataque_pokemon) >= 200):
                poder_ataque_pokemon = prompt("Error en el poder de ataque", "Por favor, ingrese el poder de ataque de su pokemon (mayor a 50 y menor a 200)")
            poder_ataque_pokemon = int(poder_ataque_pokemon)

            self.lista_nombre_pokemones.append(nombre_pokemon)
            self.lista_tipo_pokemones.append(tipo_pokemon)
            self.lista_poder_pokemones.append(poder_ataque_pokemon)

        #! informe 1: 3) Nombre y Poder del pokemon de tipo psiquico con el poder mas bajo.

        #! informe 2: 6) tipo de los pokemones del tipo que mas pokemones posea.
        mayor_tipo = None
        tipo_agua = 0
        tipo_psiquico = 0
        tipo_electrico = 0
        for tipo in self.lista_tipo_pokemones:
            if tipo == "Agua":
                tipo_agua += 1
            elif tipo == "Psiquico":
                tipo_psiquico += 1
            else:
                tipo_electrico += 1

        if tipo_agua > tipo_psiquico and tipo_agua > tipo_electrico:
            mayor_tipo = "Agua"
        elif tipo_psiquico > tipo_electrico and tipo_psiquico > tipo_agua:
            mayor_tipo = "Psiquico"
        else:
            mayor_tipo = "Electrico"

        print(f"El tipo con mas pokemones es: {mayor_tipo}")

        # Informe 3: 2) - Nombre y Poder del pokemon de tipo electrico con el poder mas alto.

        #ACLARACION: EN TODOS LOS EJERCICIOS QUE NO PUDE HACER FUERON PORQUE NO RECUERDO COMO MOSTRAR DATOS DE DISTINTAS LISTAS, EL RESTO (CREO) QUE ESTÁ BIEN.




    
if __name__ == "__main__":
    app = App()
    app.mainloop()