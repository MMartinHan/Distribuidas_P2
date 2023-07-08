import tkinter as tk
from tkinter import ttk
from funciones_ventanas import abrir_ventana, cerrar_ventana

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
        
class VentanaOpciones(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Pantalla de opciones")
        self.geometry("500x300")
        
        self.etiqueta_opciones = tk.Label(self, text="Opciones")
        self.etiqueta_opciones.pack()

        self.frame_contenedor = tk.Frame(self)
        self.frame_contenedor.pack(pady=20)

        self.boton_opcion_1 = tk.Button(self.frame_contenedor, text="SELECCION")
        self.boton_opcion_1.pack(side="left", padx=10)
        self.boton_opcion_2 = tk.Button(self.frame_contenedor, text="NOMINA", command=self.abrir_ventana_motivo)
        self.boton_opcion_2.pack(side="left", padx=10)
        self.boton_opcion_3 = tk.Button(self.frame_contenedor, text="CONTABILIDAD")
        self.boton_opcion_3.pack(side="left", padx=10)
        
    def abrir_ventana_motivo(self):
        cerrar_ventana(self)
        abrir_ventana(VentanaNomina)
        
class VentanaNomina(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Pantalla de motivo")
        self.geometry("600x400")
        
        self.etiqueta_opciones = tk.Label(self, text="Opciones de Motivo")
        self.etiqueta_opciones.pack()
        
        self.frame_contenedor = tk.Frame(self)
        self.frame_contenedor.pack(pady=20)

        self.boton_opcion_1 = tk.Button(self.frame_contenedor, text="Ingresar motivo", command=self.agregar)
        self.boton_opcion_1.pack(side="left", padx=10)
        self.boton_opcion_2 = tk.Button(self.frame_contenedor, text="Modificar motivo")
        self.boton_opcion_2.pack(side="left", padx=10)
        self.boton_opcion_3 = tk.Button(self.frame_contenedor, text="Eliminar motivo")
        self.boton_opcion_3.pack(side="left", padx=10)
        self.boton_opcion_4 = tk.Button(self.frame_contenedor, text="Consultar motivo")
        self.boton_opcion_4.pack(side="left", padx=10)
        
        self.etiqueta_opciones = tk.Label(self, text="Opciones de Empleado")
        self.etiqueta_opciones.pack()
        
        self.frame_contenedor = tk.Frame(self)
        self.frame_contenedor.pack(pady=20)

        self.boton_opcion_5 = tk.Button(self.frame_contenedor, text="Ingresar empleado")
        self.boton_opcion_5.pack(side="left", padx=10)
        self.boton_opcion_6 = tk.Button(self.frame_contenedor, text="Modificar empleado")
        self.boton_opcion_6.pack(side="left", padx=10)
        self.boton_opcion_7 = tk.Button(self.frame_contenedor, text="Eliminar empleado")
        self.boton_opcion_7.pack(side="left", padx=10)
        self.boton_opcion_7 = tk.Button(self.frame_contenedor, text="Consultar empleado")
        self.boton_opcion_7.pack(side="left", padx=10)
        
        self.etiqueta_opciones = tk.Label(self, text="Opciones de Nomina")
        self.etiqueta_opciones.pack()
        
        self.frame_contenedor = tk.Frame(self)
        self.frame_contenedor.pack(pady=20)
        
        self.boton_opcion_8 = tk.Button(self.frame_contenedor, text="Ingresar nomina")
        self.boton_opcion_8.pack(side="left", padx=10)
        self.boton_opcion_9 = tk.Button(self.frame_contenedor, text="Modificar nomina")
        self.boton_opcion_9.pack(side="left", padx=10)
        self.boton_opcion_10 = tk.Button(self.frame_contenedor, text="Eliminar nomina")
        self.boton_opcion_10.pack(side="left", padx=10)
        self.boton_opcion_11 = tk.Button(self.frame_contenedor, text="Consultar nomina")
        self.boton_opcion_11.pack(side="left", padx=10)
        
        self.etiqueta_opciones = tk.Label(self, text="Opciones de Reportes")
        self.etiqueta_opciones.pack()
        
        self.frame_contenedor = tk.Frame(self)
        self.frame_contenedor.pack(pady=10)
        
        self.boton_opcion_12 = tk.Button(self.frame_contenedor, text="Valores a pagar")
        self.boton_opcion_12.pack(side="left", padx=5)
        self.boton_opcion_13 = tk.Button(self.frame_contenedor, text="Reporte cruzado")
        self.boton_opcion_13.pack(side="left", padx=5)
        
        self.boton_regresar = tk.Button(self, text="Regresar", command=self.mover_inicio)
        self.boton_regresar.pack()
        
    def mover_inicio(self):
        cerrar_ventana(self)
        abrir_ventana(VentanaOpciones)
        
    def agregar(self):
        cerrar_ventana(self)
        abrir_ventana(VentanaAgregarMotivo)
        
class VentanaAgregarMotivo(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Agregar motivo")
        self.geometry("600x400")

        self.etiqueta_entrada = tk.Label(self, text='Ingresar nuevo motivo: ')
        self.etiqueta_entrada.pack()
        self.campo_motivo = tk.Entry(self)
        self.campo_motivo.pack()
        
        # Crear estilo para la tabla
        estilo = ttk.Style()
        estilo.configure("Tabla.Treeview", borderwidth=1, relief="solid")
        estilo.configure("Tabla.Treeview.Heading", background="lightgray", foreground="black", font=('Helvetica', 10, 'bold'))
        estilo.map("Tabla.Treeview", background=[("selected", "#0078D7")])
        estilo.map("Tabla.Treeview.Heading", background=[("active", "#0078D7")])

        self.etiqueta_tabla = tk.Label(self, text=" ")
        self.etiqueta_tabla.pack()
        self.etiqueta_tabla = tk.Label(self, text="Registros encontrados")
        self.etiqueta_tabla.pack()

        self.tabla = ttk.Treeview(self, columns=('ID', 'Motivo'), show='headings', style="Tabla.Treeview")
        self.tabla.heading('ID', text='ID')
        self.tabla.heading('Motivo', text='Motivo')
        self.tabla.column('ID', width=50)
        self.tabla.column('Motivo', width=300)
        self.dibujar_bordes()
        self.tabla.pack()

        self.tabla.bind('<Double-1>', self.modificar_motivo)

        self.boton_agregar = tk.Button(self, text='Agregar', command=self.agregar_motivo)
        self.boton_agregar.pack()

        self.cargar_registros()  # Cargar los registros existentes

    def dibujar_bordes(self):
        # Obtener el ancho y alto de la tabla
        tabla_width = self.tabla.winfo_width()
        tabla_height = self.tabla.winfo_height()

        # Dibujar bordes de colores para cada fila
        for row_id in self.tabla.get_children():
            rect = self.tabla.bbox(row_id, column="#all")
            self.tabla.item(row_id, tags=(row_id,))
            self.tabla.tag_configure(row_id, background="black")
            self.tabla.place(rect, bordermode="outside", anchor="nw")

        # Dibujar bordes de colores para cada columna
        for col_id in self.tabla.get_children():
            rect = self.tabla.bbox(col_id, column="#all")
            self.tabla.item(col_id, tags=(col_id,))
            self.tabla.tag_configure(col_id, background="black")
            self.tabla.place(rect, bordermode="outside", anchor="nw")
    
    def cargar_registros(self):
        # Obtener los registros de la base de datos
        # Aquí debes agregar la lógica para obtener los registros de la base de datos

        # Ejemplo de registros obtenidos de la base de datos
        registros = [
            {'id': 1, 'motivo': 'Motivo 1'},
            {'id': 2, 'motivo': 'Motivo 2'},
            {'id': 3, 'motivo': 'Motivo 3'}
        ]

        for i, registro in enumerate(registros, start=1):
            id_registro = registro['id']
            motivo_registro = registro['motivo']
            self.tabla.insert('', 'end', values=(i, id_registro, motivo_registro))

    def agregar_motivo(self):
        motivo = self.campo_motivo.get()
        self.tabla.insert('', tk.END, values=('', motivo))
        self.campo_motivo.delete(0, 'end')

    def modificar_motivo(self, event):
        seleccion = self.tabla.focus()
        if seleccion:
            valores = self.tabla.item(seleccion)['values']
            id_seleccionado = valores[1]
            motivo_seleccionado = valores[2]
            self.destroy()
            ventana_modificar = VentanaModificacion()
            ventana_modificar.mainloop()

class VentanaModificacion(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ventana de Modificación")

        motivo =""
        self.motivo_seleccionado = motivo

        self.etiqueta_motivo = tk.Label(self, text=f"Motivo seleccionado: {self.motivo_seleccionado}")
        self.etiqueta_motivo.pack()

        self.boton_guardar = tk.Button(self, text="Guardar", command=self.guardar_motivo)
        self.boton_guardar.pack()

    def guardar_motivo(self):
        # Lógica para guardar el motivo modificado
        self.destroy()     

# Crear una instancia de la clase VentanaLogin y ejecutar el bucle principal
ventana = VentanaLogin()
ventana.mainloop()
