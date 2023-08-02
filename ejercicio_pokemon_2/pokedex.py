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
    * El tipo de su elemento (Agua, Psiquico, Fuego)
    * Poder de ataque (validar que sea mayor a 50 y menor a 200)
B) Al presionar el boton mostrar se deberan listar los pokemones y su posicion en la lista (por terminal) 

Del punto C solo debera realizar 3 informes. Para determinar que informe hacer, tenga en cuenta lo siguiente:
    
    Informe 1- Tome el ultimo numero de su DNI Personal (Ej 4) y realice ese informe (Ej, Realizar informe 4)
    3
    
    Informe 2- Tome el ultimo numero de su DNI Personal (Ej 4), y restarselo al numero 9 (Ej 9-4 = 5). En caso de que su DNI 
    finalice con el numero 0, debera realizar el informe 9.
    6
    
    
    Informe 3- Tome la suma de los ultimos dos numeros de su DNI personal, en caso de ser un numero par, tomara el numero par 
    mas chico que su ultimo digito del DNI (en caso de que su ultimo digito sea 2, resolvera el ejercicio 8). En caso contrario
    , si es impar, 
    tomara el numero impar posterior (en caso de que su ultimo digito sea 9, resolvera el ejercicio 1)
    En caso de que el numero sea el mismo obtenido en el informe 2, realizara el siguiente informe en la lista.
    
    
    Realizar los informes correspondientes a los numeros obtenidos. EL RESTO DE LOS INFORMES LOS DEBE IGNORAR. 
C) 
    #! 0) - Cantidad de pokemones de tipo Fuego cuyo poder de pelea con un 10% extra supere los 100 puntos.
    #! 1) - Cantidad de pokemones de tipo Psiquico cuyo poder de pelea con un 15% menos este entre los 100 y los 150 puntos.
    #! 2) - Nombre y Poder del pokemon de tipo Agua con el poder mas alto.
    #! 3) - Nombre y Poder del pokemon de tipo Psiquico con el poder mas bajo.
    #! 4) - Porcentaje de pokemones de tipo agua con mas de 100 puntos de poder (Sobre el total de pokemones ingresados).
    #! 5) - Porcentaje de pokemones de tipo psiquico con poder de pelea inferior o igual a 150 (sobre el total de pokemones ingresados).
    #! 6) - tipo de los pokemones del tipo que mas pokemones posea. 
    #! 7) - tipo de los pokemones del tipo que menos pokemones posea. 
    #! 8) - Listado de todos los pokemones cuyo poder de pelea supere el valor promedio.
    #! 9) - el promedio de poder de todos los pokemones de tipo Psiquico.

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA - Pokedex")
        self.minsize(320, 250)

        self.label_title = customtkinter.CTkLabel(master=self, text="Pokedex", font=("Arial", 20, "bold"))
        self.label_title.grid(row=0, column=0, columnspan=2, padx=20, pady=10)
        self.image = tk.PhotoImage(file='Logo_UTN_App.png')
        
        self.top_banner = customtkinter.CTkLabel(master = self, image = self.image, text = 'Banner')
        self.top_banner.grid_configure(row = 1, column = 0, padx = 20, pady = 5, columnspan = 2, rowspan = 1, sticky = 'we')

        self.btn_cargar = customtkinter.CTkButton(master=self, text="Cargar Pokedex", command=self.btn_cargar_pokedex_on_click)
        self.btn_cargar.grid(row=2, pady=10, columnspan=2, sticky="nsew")
        self.btn_mostrar_todos = customtkinter.CTkButton(master=self, text="Mostrar todos", command=self.btn_mostrar_todos_on_click)
        self.btn_mostrar_todos.grid(row=3, pady=10, columnspan=2, sticky="nsew")
        self.btn_informe_1 = customtkinter.CTkButton(master=self, text="Informe 1", command=self.btn_mostrar_informe_1)
        self.btn_informe_1.grid(row=4, pady=10, columnspan=2, sticky="nsew")
        self.btn_informe_2 = customtkinter.CTkButton(master=self, text="Informe 2", command=self.btn_mostrar_informe_2)
        self.btn_informe_2.grid(row=5, pady=10, columnspan=2, sticky="nsew")
        self.btn_informe_3 = customtkinter.CTkButton(master=self, text="Informe 3", command=self.btn_mostrar_informe_3)
        self.btn_informe_3.grid(row=6, pady=10, columnspan=2, sticky="nsew")
        # Cargar aca los pokemones
        self.lista_nombre_pokemones =["Squirtle", "Psyduck", "Cloyster", "Charmander", "Drowzee", "Gyarados", "Squirtle", "Mewtwo", "Charizard", "Magikarp"]
        self.lista_poder_pokemones = [90, 150, 150, 95, 70, 90, 150, 80, 50, 103]
        self.lista_tipo_pokemones = ["agua", "psíquico", "agua", "fuego", "psíquico", "agua", "agua", "psíquico", "fuego", "agua"]

    def btn_mostrar_todos_on_click(self):
        for i, nombre in enumerate(self.lista_nombre_pokemones):
            print(f"{i}, {nombre}")
    
    def btn_mostrar_informe_1(self):
         #! 3) - Nombre y Poder del pokemon de tipo Psiquico con el poder mas bajo.
        nombre_psiquico_mas_debil = None
        poder_psiquico_mas_debil = 0
        indice = 0

        for tipo in self.lista_tipo_pokemones:
            if tipo == "psíquico" and (poder_psiquico_mas_debil == 0 or poder_psiquico_mas_debil > self.lista_poder_pokemones[indice]):
                nombre_psiquico_mas_debil = self.lista_nombre_pokemones[indice]
                poder_psiquico_mas_debil = self.lista_poder_pokemones[indice]
            indice += 1
        if poder_psiquico_mas_debil == 0:
            alert("Error", "No hay pokemones de tipo psíquico")
        else:
            alert("Informe 3", f"El nombre del pokemon tipo psíquico más debil es {nombre_psiquico_mas_debil} y su poder es {poder_psiquico_mas_debil}")

        #! 0) - Cantidad de pokemones de tipo Fuego cuyo poder de pelea con un 10% extra supere los 100 puntos.
        cantidad_fuego_mayor_100 = 0
        indice = 0

        for i, tipo in enumerate(self.lista_tipo_pokemones):
            if tipo == "fuego":
                poder_fuego = self.lista_poder_pokemones[i]
                if (poder_fuego * 1.1) > 100:
                    cantidad_fuego_mayor_100 += 1
            indice += 1
        
        if cantidad_fuego_mayor_100 == 0:
            mensaje = "No existen pokemones de tipo fuego cuyo poder de pelea con un (10%) extra superen los 100 puntos"
        else:
            mensaje = f"La cantidad de pokemones de tipo fuego cuyo poder de pelea con un (10%) extra superen los 100 puntos es {cantidad_fuego_mayor_100}"
        alert("Informe 0", mensaje)

        #! 1) - Cantidad de pokemones de tipo Psiquico cuyo poder de pelea con un 15% menos este entre los 100 y los 150 puntos.
        cant_psiquico_entre_rango_de_poder = 0
        indice = 0
        lista_poder_psiquicos = []
        for i, tipo in enumerate(self.lista_tipo_pokemones):
            if tipo == "psíquico":
                poder_psiquicos = self.lista_poder_pokemones[i]
                lista_poder_psiquicos.append(poder_psiquicos)
                print(poder_psiquicos)
            indice += 1
        
        quince_porciento = (poder_psiquicos * 1.15) / 100

        for poder in lista_poder_psiquicos:
            if ((poder - quince_porciento) >= 100) and ((poder - quince_porciento) <= 150):
                cant_psiquico_entre_rango_de_poder += 1

        if cant_psiquico_entre_rango_de_poder == 0:
            mensaje = "No hay pokemones de tipo psiquico cuyo poder de pelea con un 15% menos este entre los 100 y los 150 puntos"
        else:
            mensaje = f"La cantidad de pokemones de tipo psiquico cuyo poder de pelea con un 15% menos este entre los 100 y los 150 puntos es {cant_psiquico_entre_rango_de_poder}"
        alert("Informe 1", mensaje)

        #! 2) - Nombre y Poder del pokemon de tipo Agua con el poder mas alto.
        nombre_agua_mas_alto = None
        poder_agua_mas_alto = 0
        for i, tipo in enumerate(self.lista_tipo_pokemones):
            if tipo == "agua":
                nombre_agua = self.lista_nombre_pokemones[i]
                poder_agua = self.lista_poder_pokemones[i]
                if poder_agua_mas_alto == 0 or poder_agua > poder_agua_mas_alto:
                    nombre_agua_mas_alto = nombre_agua
                    poder_agua_mas_alto = poder_agua
            indice += 1
        if poder_agua_mas_alto == 0:
            mensaje = "No existen pokemones de tipo agua"
        else:
            mensaje = f"El nombre del pokemon de tipo agua con el poder mas alto es {nombre_agua_mas_alto},y su poder es {poder_agua_mas_alto}"
            
        alert("Informe 2", mensaje)


            

    def btn_mostrar_informe_2(self):
        #! 6) - tipo de los pokemones del tipo que mas pokemones posea.
        cantidad_agua = 0
        cantidad_psíquico = 0
        cantidad_fuego = 0
        
        for tipo in self.lista_tipo_pokemones:
            if tipo == "agua":
                cantidad_agua += 1
            elif tipo == "psíquico":
                cantidad_psíquico += 1
            else:
                cantidad_fuego += 1

        if cantidad_agua > cantidad_fuego and cantidad_agua > cantidad_psíquico:
            mensaje = "agua"
        elif cantidad_fuego > cantidad_agua and cantidad_fuego > cantidad_psíquico:
            mensaje = "fuego"
        else:
            mensaje = "psíquico"
        
        alert("Titulo", f"El tipo con mas pokemones es {mensaje}")

        #! 5) - Porcentaje de pokemones de tipo psiquico con poder de pelea inferior o igual a 150 (sobre el total de pokemones ingresados).
        i = 0
        contador_psiquicos_menor_150 = 0
        for tipo in self.lista_tipo_pokemones:
            if tipo == "psíquico" and (self.lista_poder_pokemones[i] <= 150):
                contador_psiquicos_menor_150 += 1
            i += 1
        

    
    def btn_mostrar_informe_3(self):
        #! 4) - Porcentaje de pokemones de tipo agua con mas de 100 puntos de poder (Sobre el total de pokemones ingresados).
        indice = 0
        contador_pokemones_agua_mayor_100 = 0
        for tipo in self.lista_tipo_pokemones:
            if tipo == "agua" and (self.lista_poder_pokemones[indice] < 100):
                contador_pokemones_agua_mayor_100 += 1
            indice += 1
        total_pokemones = len(self.lista_nombre_pokemones)

        if contador_pokemones_agua_mayor_100 == 0:
            alert("Error", "No existen pokemones tipo agua con mas de 100 de poder")
        else:
            porcentaje_pokemones_agua = (100 * contador_pokemones_agua_mayor_100) / total_pokemones
            alert("Total", f"El porcentaje de pokemones tipo agua con poder mayor a 100 es: {porcentaje_pokemones_agua}%")

        #! 7) - tipo de los pokemones del tipo que menos pokemones posea.
        cantidad_agua = 0
        cantidad_psíquico = 0
        cantidad_fuego = 0
        
        for tipo in self.lista_tipo_pokemones:
            if tipo == "agua":
                cantidad_agua += 1
            elif tipo == "psíquico":
                cantidad_psíquico += 1
            else:
                cantidad_fuego += 1

        if cantidad_agua < cantidad_fuego and cantidad_agua < cantidad_psíquico:
            mensaje = "agua"
        elif cantidad_fuego < cantidad_agua and cantidad_fuego < cantidad_psíquico:
            mensaje = "fuego"
        else:
            mensaje = "psíquico"
        
        alert("Titulo", f"El tipo con menos pokemones es {mensaje}")

        #! 8) - Listado de todos los pokemones cuyo poder de pelea supere el valor promedio.

        contador_poderes = 0
        acumulador_poderes = 0
        for poder in self.lista_poder_pokemones:
            contador_poderes += 1
            acumulador_poderes += poder
            
        promedio_poderes = acumulador_poderes / contador_poderes
        
        for i, poderes in enumerate(self.lista_poder_pokemones):
            if poderes > promedio_poderes:
                print(self.lista_nombre_pokemones[i], self.lista_poder_pokemones[i])
         
                
    def btn_cargar_pokedex_on_click(self):
        pass
        
            
        
        
if __name__ == "__main__":
    app = App()
    app.mainloop() 