import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import tkinter as tk

"""
Se deben pedir los siguientes datos de un tour  de vacaciones a un destino en particular:


1 -nombre , edad y género de una persona, mostrar el mensaje , "usted es  xxxx tiene xx de edad y su género es xxx"

2 -pedir la altura de la persona e informar si es bajo: menor a 140 cm,  
medio entre 140 y 170 cm , alto hasta 190 cm y muy alto para mayores a esa altura.1


3- validar todos los datos

4- en las vacaciones se pueden seleccionar distintas excursiones para realizar , 
se pueden hacer desde 0 excursión a 11 excursiones

5- una vez ingresada la cantidad se debe pedir por cada excursión 
el importe y el tipo de excursión(caminata  o vehículo). 
informar cual es el precio más caro el más barato y el promedio

6- informar cual es el tipo de excursión(caminata  o vehículo). 
más seleccionada o si se seleccionó las mismas veces (caminata  o vehículo)

Codigo de: Joaquin Vicente, división E


"""

# class App(customtkinter.CTk):
    
#     def __init__(self):
#         super().__init__()

#         self.title("UTN FRA")
#         self.minsize(320, 250)

#         self.label_title = customtkinter.CTkLabel(master=self, text="Tour", font=("Arial", 20, "bold"))
#         self.label_title.grid(row=0, column=0, columnspan=2, padx=20, pady=10)
#         self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
#         self.btn_mostrar.grid(row=3, pady=20, columnspan=2, sticky="nsew")
#         self.label_nombre = customtkinter.CTkLabel(master=self, text="Nombre")
#         self.label_nombre.grid(row=0, column=0, padx=20, pady=10)
#         self.txt_nombre = customtkinter.CTkEntry(master=self)
#         self.txt_nombre.grid(row=0, column=1)
#         self.label_edad = customtkinter.CTkLabel(master=self, text="Edad")
#         self.label_edad.grid(row=1, column=0, padx=20, pady=10)
#         self.txt_edad = customtkinter.CTkEntry(master=self)
#         self.txt_edad.grid(row=1, column=1)
#         self.label2 = customtkinter.CTkLabel(master=self, text="Tipo")
#         self.label2.grid(row=2, column=0, padx=20, pady=10)
#         self.combobox_genero = customtkinter.CTkComboBox(master=self, values=["Masculino", "Femenino", "Otro"])
#         self.combobox_genero.grid(row=2, column=1, padx=20, pady=10)
   
#     def btn_mostrar_on_click(self):
#         nombre = self.txt_nombre.get()
#         edad =  self.txt_edad.get()
#         genero = self.combobox_genero.get()
#         mensaje = f"Su nombre es {nombre}, tiene {edad} años de edad y su genero es {genero}"

#         alert("Titulo", mensaje)
        

# if __name__ == "__main__":
#     app = App()
#     app.geometry("300x300")
#     app.mainloop()

class App(customtkinter.CTk):
   
    def __init__(self):
        super().__init__()


        self.title("UTN FRA")
        self.minsize(320, 250)


        self.label_title = customtkinter.CTkLabel(master=self, text="Tour", font=("Arial", 20, "bold"))
        self.label_title.grid(row=0, column=0, columnspan=2, padx=20, pady=10)
       
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=4, pady=20, columnspan=2, sticky="nsew")
   
    def btn_mostrar_on_click(self):

        # Puntos 1 y 3
        nombre = prompt("UTN", "Ingrese nombre")
        while not nombre or not nombre.isalpha() or len(nombre) < 3:
            nombre = prompt("UTN", "Error: ingrese nuevamente su nombre")

        edad =  prompt("UTN", "Ingrese edad")
        while not edad or not edad.isdigit():
            edad = prompt("UTN", "Error: ingrese nuevamente su edad")
        edad = int(edad)

        genero = prompt("UTN", 'Ingrese genero: "Masculino" - "Femenino" - "Otro"')
        while not genero or not genero.isalpha() or (genero != "Masculino" and genero != "Femenino" and genero != "Otro"):
            genero = prompt("Error género", 'Ingrese genero: "Masculino" - "Femenino" - "Otro"')


        altura = prompt("UTN", "Ingrese su altura (en centímetros)")
        while not altura or not altura.isdigit():
            altura = prompt("UTN", "Error: ingrese nuevamente su altura")
        altura = int(altura)

        # Punto 2
        if altura < 140:
            mensaje_altura = "bajo"
        elif altura <= 170:
            mensaje_altura = "medio"
        elif altura <= 190:
            mensaje_altura = "alto"
        else:
            mensaje_altura = "muy alto"


        cantidad_exc = prompt("Excursiones", "Ingrese cantidad de excursiones")
        while not cantidad_exc or not cantidad_exc.isdigit() or int(cantidad_exc) < 0 or int(cantidad_exc) > 11:
            cantidad_exc = prompt("Excursiones", "Error: ingrese nuevamente la cantidad de excursiones")

        contador_exc = 0
        precio_caro = None
        tipo_mas_caro = ""
        precio_barato = None
        tipo_mas_barato = ""
        promedio_precios = 0
        suma_precios = 0
        contador_caminatas = 0
        contador_vehiculos = 0

        while contador_exc < cantidad_exc:

            importe =  prompt("UTN", "Ingrese importe")
            while not importe or not importe.isdigit():
                importe = prompt("UTN", "Error: ingrese nuevamente su importe")
            importe = int(importe)

            tipo = prompt("Excursiones", "Ingrese tipo de excursion (caminata o vehículo)")
            while not tipo or not tipo.isalpha() or (tipo!= "caminata" and tipo!= "vehículo"):
                tipo = prompt("Excursiones", "Error: Ingrese tipo de excursion (caminata o vehículo)")

            if not precio_barato or importe < precio_barato:
                precio_barato = importe
                tipo_mas_barato = tipo
            if not precio_caro or importe > precio_caro:
                precio_caro = importe
                tipo_mas_caro = tipo
                
            suma_precios += importe

            contador_exc += 1

            if tipo == "caminata":
                contador_caminatas += 1
            else:
                contador_vehiculos += 1

        
        promedio_precios = suma_precios / cantidad_exc

        informe = f"La excursion mas barata vale ${precio_barato} y es de {tipo_mas_barato}.\n\
            La excursion mas cara vale ${precio_caro} y es de {tipo_mas_caro}.\n\
            El promedio de precios de las excursiones es de ${promedio_precios}"
        alert("Informe", informe)



        excursiones_int = int(cantidad_exc)

        mensaje = f"Usted es {nombre}, tiene {edad} de edad y su genero es {genero} y según su altura es: {mensaje_altura}"

        alert("UTN", mensaje)





if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()

