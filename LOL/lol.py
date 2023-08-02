import tkinter as tk
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

"""
Un jugador de League of Legends tiene un fin de semana libre y va a jugar partidas hasta que se canse.
Para mejorar su jugabilidad, por cada partida jugada va a registrar:
Modo de juego ("Normal", "Clasificatoria", "ARAM")
Nombre del personaje que usó
La cantidad de asesinatos (No puede ser negativo)
Muertes (No puede ser negativo)
Asistencias. (No puede ser negativo, hasta 40)

De lo registrado, al jugador le interesa lo siguiente:

a) El modo de juego más jugado.
b) El personaje con el cual murió más.
c) El promedio de asistencias.
d) De la partida con mas asesinatos, el nombre del personaje y el modo de juego.

 """
class App(customtkinter.CTk):
    def __init__(self):
            super().__init__()

            self.title("UTN FRA - League of Legends")
            self.minsize(320, 250)

            self.label_title = customtkinter.CTkLabel(master=self, text="League of Legends", font=("Arial", 20, "bold"))
            self.label_title.grid(row=0, column=0, columnspan=2, padx=20, pady=10)
        
            self.top_banner = customtkinter.CTkLabel(master = self, text = 'Banner')
            self.top_banner.grid_configure(row = 1, column = 0, padx = 20, pady = 5, columnspan = 2, rowspan = 1, sticky = 'we')

            self.btn_cargar_datos = customtkinter.CTkButton(master=self, text="Cargar datos de partida", command=self.btn_cargar_datos_on_click)
            self.btn_cargar_datos.grid(row=3, pady=10, columnspan=2, sticky="nsew")
            self.btn_informe_1 = customtkinter.CTkButton(master=self, text="Informe 1", command=self.btn_mostrar_informe_1)
            self.btn_informe_1.grid(row=4, pady=10, columnspan=2, sticky="nsew")
            self.btn_informe_2 = customtkinter.CTkButton(master=self, text="Informe 2", command=self.btn_mostrar_informe_2)
            self.btn_informe_2.grid(row=5, pady=10, columnspan=2, sticky="nsew")
            self.btn_informe_3 = customtkinter.CTkButton(master=self, text="Informe 3", command=self.btn_mostrar_informe_3)
            self.btn_informe_3.grid(row=6, pady=10, columnspan=2, sticky="nsew")

            self.lista_modos_de_juego = []
            self.lista_nombres = []
            self.lista_asesinatos = []
            self.lista_muertes = []
            self.lista_asistencias = []



    def btn_cargar_datos_on_click(self):
        modo_de_juego = prompt("Modo de juego", "Ingrese su modo de juego (Normal, Clasificatoria o ARAM)")
        while modo_de_juego != "Normal" and modo_de_juego != "Clasificatoria" and modo_de_juego != "ARAM":
            modo_de_juego = prompt("Error", "Por favor, ingrese su modo de juego (Normal, Clasificatoria o ARAM)")
        self.lista_modos_de_juego.append(modo_de_juego)

        nombre = prompt("Nombre", "Ingrese el nombre de su personaje")
        while not nombre:
            nombre = prompt("Error", "Por favor, ingrese el nombre de su personaje")
        self.lista_nombres.append(nombre)

        cantidad_asesinatos = prompt("Asesinatos", "Ingrese la cantidad de asesinatos")
        while not cantidad_asesinatos or not cantidad_asesinatos.isdigit():
            cantidad_asesinatos = prompt("Error", "Por favor, ingrese la cantidad de asesinatos")
        cantidad_asesinatos = int(cantidad_asesinatos)
        self.lista_asesinatos.append(cantidad_asesinatos)

        muertes = prompt("Muertes", "Ingrese el numero de muertes")
        while not muertes or not muertes.isdigit():
            muertes = prompt("Error", "Por favor, ingrese la cantidad de muertes")
        muertes = int(muertes)
        self.lista_muertes.append(muertes)

        asistencias = prompt("Asistencias", "Ingrese el número de asistencias (maximo 40)")
        while not asistencias or not asistencias.isdigit() or int(asistencias) > 40:
            asistencias = prompt("Error", "Por favor, ingrese el número de asistencias (maximo 40)")
        asistencias = int(asistencias)
        self.lista_asistencias.append(asistencias)


    def btn_mostrar_informe_1(self):
        # a) El modo de juego más jugado.

        cont_normal = 0
        cont_clasificatoria = 0
        cont_aram = 0
        for modo_juego in self.lista_modos_de_juego:
            if modo_juego == "Normal":
                cont_normal += 1
            elif modo_juego == "Clasificatoria":
                cont_clasificatoria += 1
            else:
                cont_aram += 1
        
        if cont_normal > cont_aram and cont_normal > cont_clasificatoria:
            mayor_modo = "Normal"
        elif cont_clasificatoria > cont_normal and cont_clasificatoria > cont_aram:
            mayor_modo = "Clasificatoria"
        elif cont_aram > cont_clasificatoria and cont_aram > cont_normal:
            mayor_modo = "ARAM"
        else:
            mayor_modo = "Ninguno"

        alert("Mayor modo", f"El modo de juego mas jugado es: {mayor_modo}")








    def btn_mostrar_informe_2(self):
        # b) El personaje con el cual murió más.

        mayor_muerte = 0
        nombre_mayor_muerte = None

        for i, muertes in enumerate(self.lista_muertes):
            if muertes > mayor_muerte:
                mayor_muerte = muertes
                nombre_mayor_muerte = self.lista_nombres[i]
        
        alert("Mayor muerte", f"El personaje que más muertes tuvo es {nombre_mayor_muerte} con {mayor_muerte} muertes")

        




    def btn_mostrar_informe_3(self):
        # c) El promedio de asistencias.
        # d) De la partida con mas asesinatos, el nombre del personaje y el modo de juego.

        acumulador_asistencias = 0
        cont_asistencias = len(self.lista_asistencias)

        for asistencias in self.lista_asistencias:
            acumulador_asistencias += asistencias
        
        promedio_asistencias = acumulador_asistencias / cont_asistencias

        alert("Promedio asistencias", f"El promedio de asistencias es {promedio_asistencias}")

        mayor_asesinatos = 0
        nombre_mayor_asesinatos = None
        modo_juego_mayor_asesinatos = None

        for i, asesinatos in enumerate(self.lista_asesinatos):
            if asesinatos > mayor_asesinatos:
                mayor_asesinatos = asesinatos
                nombre_mayor_asesinatos = self.lista_nombres[i]
                modo_juego_mayor_asesinatos = self.lista_modos_de_juego[i]
        
        alert("Datos finales", f"De la partida con mas asesinatos ({mayor_asesinatos}), el nombre del personaje es {nombre_mayor_asesinatos} y el modo de juego es {modo_juego_mayor_asesinatos}")


        


if __name__ == "__main__":
    app = App()
    app.mainloop()
