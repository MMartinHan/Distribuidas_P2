from tkinter import *
from seleccion import *
from contabilidad import *
from funciones_ventanas import abrir_ventana, cerrar_ventana

class VentanaLogin(Tk):
    def __init__(self):
        super().__init__()
        self.title("Pantalla de inicio de sesión")
        self.geometry("500x300")
        
        self.etiqueta_usuario = Label(self, text="Usuario:")
        self.etiqueta_usuario.pack()
        self.entrada_usuario = Entry(self)
        self.entrada_usuario.pack()

        self.etiqueta_contrasena = Label(self, text="Contraseña:")
        self.etiqueta_contrasena.pack()
        self.entrada_contrasena = Entry(self, show="*")
        self.entrada_contrasena.pack()
        
        self.espacio_blanco = Label(self, text="")
        self.espacio_blanco.pack()
        
        self.boton_iniciar_sesion = Button(self, text="Iniciar sesión", command=self.login)
        self.boton_iniciar_sesion.pack()

    def login(self):
        usuario = self.entrada_usuario.get()
        contrasena = self.entrada_contrasena.get()
        if usuario == "admin" and contrasena == "admin":
            # Limpiar los campos de entrada después de iniciar sesión
            self.entrada_usuario.delete(0, 'end')
            self.entrada_contrasena.delete(0, 'end')
            cerrar_ventana(self)
            abrir_ventana(VentanaOpciones)
        else:
            self.espacio_blanco.config(text="Usuario o contraseña incorrectos")
        
        
        
        

class VentanaOpciones(Tk):
    def __init__(self):
        super().__init__()
        self.title("Pantalla de opciones")
        self.geometry("500x300")
        
        self.etiqueta_opciones = Label(self, text="Opciones")
        self.etiqueta_opciones.pack()

        self.frame_contenedor = Frame(self)
        self.frame_contenedor.pack(pady=20)

        self.boton_opcion_1 = Button(self.frame_contenedor, text="SELECCION")
        self.boton_opcion_1.pack(side="left", padx=10)
        self.boton_opcion_2 = Button(self.frame_contenedor, text="NOMINA", command=self.abrir_ventana_motivo)
        self.boton_opcion_2.pack(side="left", padx=10)
        self.boton_opcion_3 = Button(self.frame_contenedor, text="CONTABILIDAD")
        self.boton_opcion_3.pack(side="left", padx=10)
        
    def abrir_ventana_motivo(self):
        cerrar_ventana(self)
        from nomina import VentanaMotivo
        abrir_ventana(VentanaMotivo)
        
        

# Crear una instancia de la clase VentanaLogin y ejecutar el bucle principal
ventana = VentanaLogin()
ventana.mainloop()