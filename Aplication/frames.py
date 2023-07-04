from tkinter import *
from nomina import *
from seleccion import *
from contabilidad import *

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
        
        self.boton_iniciar_sesion = Button(self, text="Iniciar sesión", command=self.abrir_ventana_opciones)
        self.boton_iniciar_sesion.pack()

    def abrir_ventana_opciones(self):
        usuario = self.entrada_usuario.get()
        contrasena = self.entrada_contrasena.get()
        
        # Verificar las credenciales y realizar las acciones necesarias
        # Tu código de verificación y acciones aquí
        if usuario == "admin" and contrasena == "admin":
            # Limpiar los campos de entrada después de iniciar sesión
            self.entrada_usuario.delete(0, 'end')
            self.entrada_contrasena.delete(0, 'end')
            
            # Cerrar la ventana actual
            self.destroy()
            
            # Abrir la ventana de opciones
            ventana_opciones = VentanaOpciones()
            ventana_opciones.mainloop()
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
        self.boton_opcion_2 = Button(self.frame_contenedor, text="NOMINA")
        self.boton_opcion_2.pack(side="left", padx=10)
        self.boton_opcion_3 = Button(self.frame_contenedor, text="CONTABILIDAD")
        self.boton_opcion_3.pack(side="left", padx=10)

# Crear una instancia de la clase VentanaLogin y ejecutar el bucle principal
ventana = VentanaLogin()
ventana.mainloop()