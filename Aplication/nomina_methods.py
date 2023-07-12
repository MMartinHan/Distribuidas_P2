import tkinter as tk
import nomina_methods as nm
import contabilidad_methods as cm
import seleccion_methods as sm
from tkinter import ttk
from tkinter import messagebox
from funciones_ventanas import abrir_ventana, cerrar_ventana
import socket

def crear_socket():
    mi_socket = socket.socket()
    mi_socket.connect(('localhost', 8000))
    return mi_socket

class VentanaLogin(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Pantalla de inicio de sesión")
        self.geometry("500x300")
        
        self.etiqueta_usuario = tk.Label(self, text="Usuario:")
        self.etiqueta_usuario.pack()
        self.entrada_usuario = tk.Entry(self)
        self.entrada_usuario.pack()

        self.etiqueta_contrasena = tk.Label(self, text="Contraseña:")
        self.etiqueta_contrasena.pack()
        self.entrada_contrasena = tk.Entry(self, show="*")
        self.entrada_contrasena.pack()
        
        self.espacio_blanco = tk.Label(self, text="")
        self.espacio_blanco.pack()
        
        self.boton_iniciar_sesion = tk.Button(self, text="Iniciar sesión", command=self.login)
        self.boton_iniciar_sesion.pack()

    def login(self):
        usuario = self.entrada_usuario.get()
        contrasena = self.entrada_contrasena.get()
        if usuario == "admin" and contrasena == "admin":
            self.entrada_usuario.delete(0, 'end')
            self.entrada_contrasena.delete(0, 'end')
            cerrar_ventana(self)
            abrir_ventana(VentanaOpciones)
        else:
            self.espacio_blanco.config(text="Usuario o contraseña incorrectos")
        