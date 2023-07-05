from tkinter import *
from funciones_ventanas import abrir_ventana, cerrar_ventana




class VentanaMotivo(Tk):
    def __init__(self):
        super().__init__()
        self.title("Pantalla de motivo")
        self.geometry("500x300")
        
        self.etiqueta_opciones = Label(self, text="Opciones")
        self.etiqueta_opciones.pack()
        
        self.frame_contenedor = Frame(self)
        self.frame_contenedor.pack(pady=20)

        self.boton_opcion_1 = Button(self.frame_contenedor, text="Ingresar motivo")
        self.boton_opcion_1.pack(side="left", padx=10)
        self.boton_opcion_2 = Button(self.frame_contenedor, text="Modificar motivo")
        self.boton_opcion_2.pack(side="left", padx=10)
        self.boton_opcion_3 = Button(self.frame_contenedor, text="Eliminar motivo")
        self.boton_opcion_3.pack(side="left", padx=10)
        self.boton_opcion_4 = Button(self.frame_contenedor, text="Consultar motivo")
        self.boton_opcion_4.pack(side="left", padx=10)
        
        self.boton_regresar = Button(self, text="Regresar", command=self.mover_inicio)
        self.boton_regresar.pack()
        
    def mover_inicio(self):
        cerrar_ventana(self)
        from frames import VentanaOpciones
        abrir_ventana(VentanaOpciones)
    

        
        