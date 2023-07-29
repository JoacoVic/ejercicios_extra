import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import tkinter as tk
import math

'''
Alumno = Joaquín Vicente
División = E

La juguetería El MUNDO DE OCTAVIO nos encarga un programa para conocer qué cantidad de materiales se necesita para la fabricación de distintos juguetes.

COMETA: 

AB = Diámetro mayor (se debe calcular)
DC = diámetro menor (se ingresa por prompt)
BD y BC = lados menores (se ingresa por prompt)
AD y AC = lados mayores (se ingresa por prompt)

Debemos tener en cuenta que la estructura del cometa estará dada por un perímetro de varillas de plástico y los correspondientes entrecruces (DC y AB) del mismo material para mantener la forma del cometa.
El cometa estará construido con papel de alta resistencia.
La cola del mismo se construirá con el mismo papel que el cuerpo y representará un 10% adicional del necesario para el cuerpo.
Necesitamos saber cuántos Mts de varillas de plástico y cuántos de papel son necesarios para la construcción en masa de 10 cometas. Tener en cuenta que los valores de entrada están expresados en Cms.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        self.minsize(320, 250)

        self.label_title = customtkinter.CTkLabel(master=self, text="El Cometa", font=("Arial", 20, "bold"))
        self.label_title.grid(row=0, column=0, columnspan=2, padx=20, pady=10)
        
        self.label_diametro_menor = customtkinter.CTkLabel(master=self, text="Diametro Menor DC")
        self.label_diametro_menor.grid(row=1, column=0, padx=20, pady=10)

        self.txt_diametro_menor= customtkinter.CTkEntry(master=self)
        self.txt_diametro_menor.grid(row=1, column=1)
        
        self.label_lados_menores = customtkinter.CTkLabel(master=self, text="Lados Menores BD y BC")
        self.label_lados_menores.grid(row=2, column=0, padx=20, pady=10)

        self.txt_lados_menores = customtkinter.CTkEntry(master=self)
        self.txt_lados_menores.grid(row=2, column=1)

        self.label_lados_mayores = customtkinter.CTkLabel(master=self, text="Lados Mayores AD y AC")
        self.label_lados_mayores.grid(row=3, column=0, padx=20, pady=10)

        self.txt_lados_mayores = customtkinter.CTkEntry(master=self)
        self.txt_lados_mayores.grid(row=3, column=1)
                
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=4, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        diametro_menor_texto = self.txt_diametro_menor.get()
        diametro_menor_numero = float(diametro_menor_texto)
        lados_menores_texto = self.txt_lados_menores.get()
        lados_menores_numero = float(lados_menores_texto)
        lados_mayores_texto = self.txt_lados_mayores.get()
        lados_mayores_numero = float(lados_mayores_texto) 

        diametro_menor_numero_mitad = (diametro_menor_numero / 2)**2

        diametro_mayor1 = math.sqrt(lados_menores_numero**2 - diametro_menor_numero_mitad)

        diametro_mayor2 = math.sqrt(lados_mayores_numero**2 - diametro_menor_numero_mitad)

        diametro_mayor = diametro_mayor1 + diametro_mayor2 

        medida_de_varillas = (lados_mayores_numero * 2 + lados_menores_numero * 2 + diametro_mayor + diametro_menor_numero) / 100

        cantidad_papel = (diametro_mayor * diametro_menor_numero) / 2

        cantidad_papel_total = (cantidad_papel * 1.1) / 100

        varillas_para_10 = medida_de_varillas * 10 
        papel_para_10 = cantidad_papel_total * 10

        mensaje = f"La medida de las varillas es {medida_de_varillas:.2f} m" 
        mensaje += f", La cantidad de papel es de {cantidad_papel_total:.2f} m2" 
        mensaje += f", La medida de las varillas para 10 es {varillas_para_10:.2f}"
        mensaje += f", La cantidad de papel para 10 es {papel_para_10:.2f}" 
        alert("" , message= mensaje)  

    
if __name__ == "__main__": 
    app = App()
    app.mainloop()