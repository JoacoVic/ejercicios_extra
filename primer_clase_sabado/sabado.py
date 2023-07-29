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
        
        mensaje = f"Usted es {nombre}, tiene {edad} años de edad, su genero es {genero} y según su altura es: {mensaje_altura}"

        alert("UTN", mensaje)


        cantidad_exc = prompt("Excursiones", "Ingrese cantidad de excursiones")
        while not cantidad_exc or not cantidad_exc.isdigit() or int(cantidad_exc) < 0 or int(cantidad_exc) > 11:
            cantidad_exc = prompt("Excursiones", "Error: ingrese nuevamente la cantidad de excursiones")
        cantidad_exc = int(cantidad_exc)

        """
        5- una vez ingresada la cantidad se debe pedir por cada excursión 
        el importe y el tipo de excursión(caminata  o vehículo). 
        informar cual es el precio más caro el más barato y el promedio

        6- informar cual es el tipo de excursión(caminata  o vehículo). 
        más seleccionada o si se seleccionó las mismas veces (caminata  o vehículo)
        """

        importe_caro = 0
        importe_barato = 0
        bandera_caro = True
        bandera_barato = True 
        total_importes = 0
        datos_cada_excursion = 0
        contador_caminata = 0
        contador_vehiculo = 0
        contador_ambos = 0
        while datos_cada_excursion < cantidad_exc:
            datos_cada_excursion += 1
            importe = prompt("Importe", "Ingrese el importe")
            while not importe or not importe.isdigit():
                importe = prompt("Error", "Por favor, ingrese el importe")
            importe = int(importe)
            tipo_excursion = prompt("tipo", "Ingres el tipo de excursion (caminata o vehiculo)")
            while not tipo_excursion or (tipo_excursion != "caminata" and tipo_excursion != "vehiculo"):
                tipo_excursion = prompt("Error", "Por favor, ingrese el tipo de excursion (caminata o vehiculo)")
            if bandera_caro == True or importe_caro < importe:
                bandera_caro = False
                importe_caro = importe

            if bandera_barato == True or importe_barato > importe:
                bandera_barato = False
                importe_barato = importe

            total_importes += importe
            if tipo_excursion == "caminata":
                contador_caminata += 1
            else:
                contador_vehiculo += 1

            contador_ambos += 1
        
        promedio_importe = total_importes / cantidad_exc
        if contador_caminata == contador_vehiculo:
            mensaje = f"La cantidad de excursiones de caminatas y vehículos es la misma ({contador_ambos})"
        elif contador_caminata > contador_vehiculo:
            mensaje = f"El tipo de excursion mas seleccionado es caminata"
        else:
            mensaje = f"El tipo de excursion mas seleccionado es vehiculo"

        alert("Estadisticas", f"El precio mas caro es ${importe_caro} y el mas barato es ${importe_barato}\nEl promedio de los importes es ${promedio_importe}")
        alert("Estadisticas 2", mensaje)







if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()

