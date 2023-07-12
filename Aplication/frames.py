import tkinter as tk
import pickle
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
        
class VentanaOpciones(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Pantalla de opciones")
        self.geometry("500x300")
        
        self.etiqueta_opciones = tk.Label(self, text="Opciones")
        self.etiqueta_opciones.pack()

        self.frame_contenedor = tk.Frame(self)
        self.frame_contenedor.pack(pady=20)

        self.boton_opcion_1 = tk.Button(self.frame_contenedor, text="SELECCION", command=self.abrir_ventana_seleccion)
        self.boton_opcion_1.pack(side="left", padx=10)
        self.boton_opcion_2 = tk.Button(self.frame_contenedor, text="NOMINA", command=self.abrir_ventana_motivo)
        self.boton_opcion_2.pack(side="left", padx=10)
        self.boton_opcion_3 = tk.Button(self.frame_contenedor, text="CONTABILIDAD", command=self.abrir_ventana_cuenta)
        self.boton_opcion_3.pack(side="left", padx=10)
        
    def abrir_ventana_seleccion(self):
        cerrar_ventana(self)
        abrir_ventana(VentanaSeleccion)
        
    def abrir_ventana_motivo(self):
        cerrar_ventana(self)
        abrir_ventana(VentanaNomina)
    
    def abrir_ventana_cuenta(self):
        cerrar_ventana(self)
        abrir_ventana(VentanaCuenta)

class VentanaSeleccion(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Pantalla de selección")
        self.geometry("600x400")
        
        self.etiqueta_opciones = tk.Label(self, text="Opciones de Candidato")
        self.etiqueta_opciones.pack()
        
        self.frame_contenedor = tk.Frame(self)
        self.frame_contenedor.pack(pady=20)

        self.boton_opcion_1 = tk.Button(self.frame_contenedor, text="Ingresar candidato", command=self.agregar_candidato)
        self.boton_opcion_1.pack(side="left", padx=10)
        
        self.etiqueta_opciones = tk.Label(self, text="Opciones de Parámetro de Evaluación")
        self.etiqueta_opciones.pack()
        
        self.frame_contenedor = tk.Frame(self)
        self.frame_contenedor.pack(pady=20)

        self.boton_opcion_2 = tk.Button(self.frame_contenedor, text="Ingresar parámetro de evaluación", command=self.agregar_parametro)
        self.boton_opcion_2.pack(side="left", padx=10)
        
        self.etiqueta_opciones = tk.Label(self, text="Opciones de Evaluación")
        self.etiqueta_opciones.pack()
        
        self.frame_contenedor = tk.Frame(self)
        self.frame_contenedor.pack(pady=20)
        
        self.boton_opcion_3 = tk.Button(self.frame_contenedor, text="Ingresar evaluación")
        self.boton_opcion_3.pack(side="left", padx=10)
        self.boton_opcion_4 = tk.Button(self.frame_contenedor, text="Modificar evaluación")
        self.boton_opcion_4.pack(side="left", padx=10)
        self.boton_opcion_5 = tk.Button(self.frame_contenedor, text="Eliminar evaluación")
        self.boton_opcion_5.pack(side="left", padx=10)
        self.boton_opcion_6 = tk.Button(self.frame_contenedor, text="Consultar evaluación")
        self.boton_opcion_6.pack(side="left", padx=10)
        
        self.etiqueta_opciones = tk.Label(self, text="Opciones de Reportes")
        self.etiqueta_opciones.pack()
        
        self.frame_contenedor = tk.Frame(self)
        self.frame_contenedor.pack(pady=10)
        
        self.boton_opcion_7 = tk.Button(self.frame_contenedor, text="Ranking de evaluados")
        self.boton_opcion_7.pack(side="left", padx=5)
        self.boton_opcion_8 = tk.Button(self.frame_contenedor, text="Reporte cruzado")
        self.boton_opcion_8.pack(side="left", padx=5)
        
        self.boton_regresar = tk.Button(self, text="Regresar", command=self.mover_inicio)
        self.boton_regresar.pack()
        
    def mover_inicio(self):
        cerrar_ventana(self)
        abrir_ventana(VentanaOpciones)
        
    def agregar_candidato(self):
        cerrar_ventana(self)
        abrir_ventana(VentanaAgregarCandidato)

    def agregar_parametro(self):
        cerrar_ventana(self)
        abrir_ventana(VentanaAgregarParametro)

class VentanaAgregarCandidato(tk.Tk):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.geometry("600x400")
        self.candidatos = []
        self.create_widgets()

    def create_widgets(self):
        self.label_cedula = tk.Label(self.master, text="Cédula:")
        self.label_cedula.pack()
        self.entry_cedula = tk.Entry(self.master)
        self.entry_cedula.pack()

        self.label_nombre = tk.Label(self.master, text="Nombre:")
        self.label_nombre.pack()
        self.entry_nombre = tk.Entry(self.master)
        self.entry_nombre.pack()

        self.label_apellido = tk.Label(self.master, text="Apellido:")
        self.label_apellido.pack()
        self.entry_apellido = tk.Entry(self.master)
        self.entry_apellido.pack()

        self.label_fecha_nacimiento = tk.Label(self.master, text="Fecha de Nacimiento:")
        self.label_fecha_nacimiento.pack()
        self.entry_fecha_nacimiento = tk.Entry(self.master)
        self.entry_fecha_nacimiento.pack()

        self.btn_guardar_candidato = tk.Button(self.master, text="Guardar", command=self.guardar_candidato)
        self.btn_guardar_candidato.pack()

        self.label_candidatos_guardados = tk.Label(self.master, text="Candidatos Guardados:")
        self.label_candidatos_guardados.pack()

        self.listbox_candidatos = tk.Listbox(self.master)
        self.listbox_candidatos.pack()

        self.btn_modificar = tk.Button(self.master, text="Modificar", state=tk.DISABLED, command=self.modificar_candidato)
        self.btn_modificar.pack(side=tk.LEFT)

        self.btn_eliminar = tk.Button(self.master, text="Eliminar", state=tk.DISABLED, command=self.eliminar_candidato)
        self.btn_eliminar.pack(side=tk.LEFT)

        self.listbox_candidatos.bind("<<ListboxSelect>>", self.actualizar_botones)

        self.btn_regresar = tk.Button(self.master, text="Regresar", command=self.mover_inicio)
        self.btn_regresar.pack()

    def mover_inicio(self):
        cerrar_ventana(self)
        abrir_ventana(VentanaSeleccion)

    def guardar_candidato(self):
        cedula = self.entry_cedula.get()
        nombre = self.entry_nombre.get()
        apellido = self.entry_apellido.get()
        fecha_nacimiento = self.entry_fecha_nacimiento.get()
        id_candidato = sm.generar_id_candidato()
        ingresoCandidato = f"INGRESAR|CANDIDATO|(CEDULA_CAN,NOMBRE_CAN,APELLIDO_CAN,FECHA_NAC_CAN)|({cedula},{nombre},{apellido},{fecha_nacimiento})|"
        id_candidato = sm.generar_id()
        ingresoCandidato = f"INGRESAR|CANDIDATO|(CEDULA_CAN,NOMBRE_CAN,APELLIDO_CAN,FECHA_NAC_CAN)|({cedula},{nombre},{apellido},{fecha_nacimiento})"
        print(ingresoCandidato)
        mi_socket = crear_socket()
        mi_socket.send(ingresoCandidato.encode("utf-8"))
        respuesta = mi_socket.recv(1024)
        print(respuesta)
        mi_socket.close()

        if cedula and nombre and apellido and fecha_nacimiento:
            self.candidatos.append((cedula, nombre, apellido, fecha_nacimiento))
            self.listbox_candidatos.insert(tk.END, f"{cedula} - {nombre} {apellido}")
            self.entry_cedula.delete(0, tk.END)
            self.entry_nombre.delete(0, tk.END)
            self.entry_apellido.delete(0, tk.END)
            self.entry_fecha_nacimiento.delete(0, tk.END)
            messagebox.showinfo("Información", "Candidato guardado exitosamente.")
        else:
            messagebox.showwarning("Advertencia", "Ingrese todos los datos del candidato.")

    def modificar_candidato(self):
        seleccion = self.listbox_candidatos.curselection()

        if seleccion:
            indice = seleccion[0]
            cedula_actual, nombre_actual, apellido_actual, fecha_nacimiento_actual = self.candidatos[indice]
            cedula_modificada = self.entry_cedula.get()
            nombre_modificado = self.entry_nombre.get()
            apellido_modificado = self.entry_apellido.get()
            fecha_nacimiento_modificada = self.entry_fecha_nacimiento.get()

            if cedula_modificada and nombre_modificado and apellido_modificado and fecha_nacimiento_modificada:
                self.candidatos[indice] = (cedula_modificada, nombre_modificado, apellido_modificado, fecha_nacimiento_modificada)
                self.listbox_candidatos.delete(indice)
                self.listbox_candidatos.insert(indice, f"{cedula_modificada} - {nombre_modificado} {apellido_modificado}")
                self.entry_cedula.delete(0, tk.END)
                self.entry_nombre.delete(0, tk.END)
                self.entry_apellido.delete(0, tk.END)
                self.entry_fecha_nacimiento.delete(0, tk.END)
                messagebox.showinfo("Información", "Candidato modificado exitosamente.")
            else:
                messagebox.showwarning("Advertencia", "Ingrese todos los datos del candidato.")
        else:
            messagebox.showwarning("Advertencia", "Seleccione un candidato para modificar.")

    def eliminar_candidato(self):
        seleccion = self.listbox_candidatos.curselection()

        if seleccion:
            indice = seleccion[0]
            cedula, nombre, apellido, fecha_nacimiento = self.candidatos[indice]
            confirmacion = messagebox.askyesno("Confirmación", f"¿Está seguro que desea eliminar el candidato '{cedula} - {nombre} {apellido}'?")

            if confirmacion:
                self.candidatos.pop(indice)
                self.listbox_candidatos.delete(indice)
                messagebox.showinfo("Información", "Candidato eliminado exitosamente.")
        else:
            messagebox.showwarning("Advertencia", "Seleccione un candidato para eliminar.")

    def actualizar_botones(self, event):
        seleccion = self.listbox_candidatos.curselection()

        if seleccion:
            self.btn_modificar.config(state=tk.NORMAL)
            self.btn_eliminar.config(state=tk.NORMAL)
        else:
            self.btn_modificar.config(state=tk.DISABLED)
            self.btn_eliminar.config(state=tk.DISABLED)

class VentanaAgregarParametro(tk.Tk):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.geometry("600x400")
        self.parametros = []
        self.create_widgets()

    def create_widgets(self):
        self.label_nombre_parametro = tk.Label(self.master, text="Nombre del parámetro:")
        self.label_nombre_parametro.pack()
        self.entry_nombre_parametro = tk.Entry(self.master)
        self.entry_nombre_parametro.pack()

        self.label_puntaje_maximo = tk.Label(self.master, text="Puntaje máximo:")
        self.label_puntaje_maximo.pack()
        self.entry_puntaje_maximo = tk.Entry(self.master)
        self.entry_puntaje_maximo.pack()

        self.btn_guardar_parametro = tk.Button(self.master, text="Guardar", command=self.guardar_parametro)
        self.btn_guardar_parametro.pack()

        self.label_parametros_guardados = tk.Label(self.master, text="Parámetros Guardados:")
        self.label_parametros_guardados.pack()

        self.listbox_parametros = tk.Listbox(self.master)
        self.listbox_parametros.pack()

        self.btn_modificar = tk.Button(self.master, text="Modificar", state=tk.DISABLED, command=self.modificar_parametro)
        self.btn_modificar.pack(side=tk.LEFT)

        self.btn_eliminar = tk.Button(self.master, text="Eliminar", state=tk.DISABLED, command=self.eliminar_parametro)
        self.btn_eliminar.pack(side=tk.LEFT)

        self.listbox_parametros.bind("<<ListboxSelect>>", self.actualizar_botones)

        self.btn_regresar = tk.Button(self.master, text="Regresar", command=self.mover_inicio)
        self.btn_regresar.pack()

    def mover_inicio(self):
        self.master.destroy()
        VentanaSeleccion(self.master)

    def guardar_parametro(self):
        nombre_parametro = self.entry_nombre_parametro.get()
        puntaje_maximo = self.entry_puntaje_maximo.get()
        
        if  nombre_parametro and puntaje_maximo:
            id = sm.generar_id_parametroEvaluacion()
            ingresoParametro = f"INGRESAR|PARAMETROEVALUACION|(CODIGO_PEV,NOMBRE_PEV,PUNTAJE_MAX)|({id},{nombre_parametro},{puntaje_maximo})|"
            print(ingresoParametro)
            mi_socket = crear_socket()
            mi_socket.send(ingresoParametro.encode("utf-8"))
            respuesta = mi_socket.recv(1024)
            print(respuesta)
            mi_socket.close()
            self.parametros.append((nombre_parametro, puntaje_maximo))
            self.listbox_parametros.insert(tk.END, f"{nombre_parametro} - {puntaje_maximo}")
            self.entry_nombre_parametro.delete(0, tk.END)
            self.entry_puntaje_maximo.delete(0, tk.END)
            messagebox.showinfo("Información", "Parámetro guardado exitosamente.")
        else:
            messagebox.showwarning("Advertencia", "Por favor, complete todos los campos.")

    def modificar_parametro(self):
        seleccion = self.listbox_parametros.curselection()

        if seleccion:
            indice = seleccion[0]
            parametro_actual = self.parametros[indice]
            nombre_parametro = self.entry_nombre_parametro.get()
            puntaje_maximo = self.entry_puntaje_maximo.get()

            if nombre_parametro and puntaje_maximo:
                self.parametros[indice] = (nombre_parametro, puntaje_maximo)
                self.listbox_parametros.delete(indice)
                self.listbox_parametros.insert(indice, f"{nombre_parametro} - {puntaje_maximo}")
                self.entry_nombre_parametro.delete(0, tk.END)
                self.entry_puntaje_maximo.delete(0, tk.END)
                messagebox.showinfo("Información", "Parámetro modificado exitosamente.")
            else:
                messagebox.showwarning("Advertencia", "Ingrese valores válidos para todos los campos.")
        else:
            messagebox.showwarning("Advertencia", "Seleccione un parámetro para modificar.")

    def eliminar_parametro(self):
        seleccion = self.listbox_parametros.curselection()

        if seleccion:
            indice = seleccion[0]
            parametro = self.parametros[indice]
            confirmacion = messagebox.askyesno("Confirmación", f"¿Está seguro que desea eliminar el parámetro '{parametro[0]}'?")

            if confirmacion:
                self.parametros.pop(indice)
                self.listbox_parametros.delete(indice)
                messagebox.showinfo("Información", "Parámetro eliminado exitosamente.")
        else:
            messagebox.showwarning("Advertencia", "Seleccione un parámetro para eliminar.")

    def actualizar_botones(self, event):
        seleccion = self.listbox_parametros.curselection()

        if seleccion:
            self.btn_modificar.config(state=tk.NORMAL)
            self.btn_eliminar.config(state=tk.NORMAL)
        else:
            self.btn_modificar.config(state=tk.DISABLED)
            self.btn_eliminar.config(state=tk.DISABLED)


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
        
        self.etiqueta_opciones = tk.Label(self, text="Opciones de Empleado")
        self.etiqueta_opciones.pack()
        
        self.frame_contenedor = tk.Frame(self)
        self.frame_contenedor.pack(pady=20)

        self.boton_opcion_5 = tk.Button(self.frame_contenedor, text="Ingresar empleado", command=self.agregarEmpleado)
        self.boton_opcion_5.pack(side="left", padx=10)
        
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

    def agregarEmpleado(self):
        cerrar_ventana(self)
        abrir_ventana(VentanaAgregarEmpleado)
        
class VentanaAgregarMotivo(tk.Tk):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.geometry("600x400")
        self.motivos = []
        self.create_widgets()
        self.rellenar_tabla()

    def create_widgets(self):
        self.label_nombre_motivo = tk.Label(self.master, text="Nombre del motivo:")
        self.label_nombre_motivo.pack()
        self.entry_nombre_motivo = tk.Entry(self.master)
        self.entry_nombre_motivo.pack()

        self.btn_guardar_motivo = tk.Button(self.master, text="Guardar", command=self.guardar_motivo)
        self.btn_guardar_motivo.pack()

        self.label_motivos_guardados = tk.Label(self.master, text="Motivos Guardados:")
        self.label_motivos_guardados.pack()

        self.treeview_motivos = ttk.Treeview(self.master, columns=("codigo", "nombre"), show="headings")
        self.treeview_motivos.heading("codigo", text="Código")
        self.treeview_motivos.heading("nombre", text="Nombre")
        self.treeview_motivos.pack()

        self.btn_modificar = tk.Button(self.master, text="Modificar", state=tk.DISABLED, command=self.modificar_motivo)
        self.btn_modificar.pack(side=tk.LEFT, padx=5)

        self.btn_eliminar = tk.Button(self.master, text="Eliminar", state=tk.DISABLED, command=self.eliminar_motivo)
        self.btn_eliminar.pack(side=tk.LEFT, padx=5)

        self.treeview_motivos.bind("<<TreeviewSelect>>", self.actualizar_botones)

        self.btn_regresar = tk.Button(self.master, text="Regresar", command=self.mover_inicio)
        self.btn_regresar.pack(side=tk.RIGHT)

    def rellenar_tabla(self):
        mi_socket = crear_socket()
        consultaMotivos = "CONSULTAR|MOTIVO|*"
        mi_socket.send(consultaMotivos.encode("utf-8"))
        self.treeview_motivos.delete(*self.treeview_motivos.get_children())
        print("Hasta aqui funciona 1")
        data = b''
        data += mi_socket.recv(1024)
        print(data)
        data_decoded = pickle.loads(data)
        print(data_decoded)
        print(type(data_decoded))
        mi_socket.close()

    def mover_inicio(self):
        cerrar_ventana(self)
        abrir_ventana(VentanaNomina)

    def guardar_motivo(self):
        nombre_motivo = self.entry_nombre_motivo.get()
        id = nm.generar_id()
        ingresoMotivo = "INGRESAR|MOTIVO|(CODIGO_MOT,NOMBRE_MOT)|"+id+","+nombre_motivo
        print(ingresoMotivo)
        mi_socket = crear_socket()
        mi_socket.send(ingresoMotivo.encode("utf-8"))
        respuesta = mi_socket.recv(1024)
        respuesta = respuesta.decode("utf-8")
        print(respuesta)
        mi_socket.close()
        
        

    def modificar_motivo(self):
        seleccion = self.listbox_motivos.curselection()

        if seleccion:
            indice = seleccion[0]
            nombre_motivo_actual = self.listbox_motivos.get(indice)
            nombre_motivo_modificado = self.entry_nombre_motivo.get()

            if nombre_motivo_modificado:
                self.motivos[indice] = nombre_motivo_modificado
                self.listbox_motivos.delete(indice)
                self.listbox_motivos.insert(indice, nombre_motivo_modificado)
                self.entry_nombre_motivo.delete(0, tk.END)
                messagebox.showinfo("Información", "Cuenta modificada exitosamente.")
            else:
                messagebox.showwarning("Advertencia", "Ingrese un nombre de cuenta válido.")
        else:
            messagebox.showwarning("Advertencia", "Seleccione una cuenta para modificar.")

    def eliminar_motivo(self):
        seleccion = self.listbox_motivos.curselection()

        if seleccion:
            indice = seleccion[0]
            nombre_motivo = self.listbox_motivos.get(indice)
            confirmacion = messagebox.askyesno("Confirmación", f"¿Está seguro que desea eliminar la cuenta '{nombre_motivo}'?")

            if confirmacion:
                self.motivos.pop(indice)
                self.listbox_motivos.delete(indice)
                messagebox.showinfo("Información", "Cuenta eliminada exitosamente.")
        else:
            messagebox.showwarning("Advertencia", "Seleccione una cuenta para eliminar.")

    def actualizar_botones(self, event):
        seleccion = self.listbox_motivos.curselection()

        if seleccion:
            self.btn_modificar.config(state=tk.NORMAL)
            self.btn_eliminar.config(state=tk.NORMAL)
        else:
            self.btn_modificar.config(state=tk.DISABLED)
            self.btn_eliminar.config(state=tk.DISABLED) 

class VentanaAgregarEmpleado(tk.Tk):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.geometry("1100x600")
        self.empleados = []
        self.create_widgets()

    def create_widgets(self):
        self.label_cedula = tk.Label(self.master, text="Cédula:")
        self.label_cedula.pack()
        self.entry_cedula = tk.Entry(self.master)
        self.entry_cedula.pack()

        self.label_nombre = tk.Label(self.master, text="Nombre:")
        self.label_nombre.pack()
        self.entry_nombre = tk.Entry(self.master)
        self.entry_nombre.pack()

        self.label_apellido = tk.Label(self.master, text="Apellido:")
        self.label_apellido.pack()
        self.entry_apellido = tk.Entry(self.master)
        self.entry_apellido.pack()

        self.label_fecha = tk.Label(self.master, text="Fecha de ingreso:")
        self.label_fecha.pack()
        self.entry_fecha = tk.Entry(self.master)
        self.entry_fecha.pack()

        self.label_sueldo = tk.Label(self.master, text="Sueldo:")
        self.label_sueldo.pack()
        self.entry_sueldo = tk.Entry(self.master)
        self.entry_sueldo.pack()

        self.btn_guardar = tk.Button(self.master, text="Guardar", command=self.guardar_empleado)
        self.btn_guardar.pack()

        self.label_empleados_guardados = tk.Label(self.master, text="Empleados Guardados:")
        self.label_empleados_guardados.pack()

        self.treeview_empleados = ttk.Treeview(self.master, columns=("cedula", "nombre", "apellido", "fecha_ingreso", "sueldo"), show="headings")
        self.treeview_empleados.heading("cedula", text="Cédula")
        self.treeview_empleados.heading("nombre", text="Nombre")
        self.treeview_empleados.heading("apellido", text="Apellido")
        self.treeview_empleados.heading("fecha_ingreso", text="Fecha de ingreso")
        self.treeview_empleados.heading("sueldo", text="Sueldo")
        self.treeview_empleados.pack()

        self.btn_modificar = tk.Button(self.master, text="Modificar", state=tk.DISABLED, command=self.modificar_empleado)
        self.btn_modificar.pack(side=tk.LEFT)

        self.btn_eliminar = tk.Button(self.master, text="Eliminar", state=tk.DISABLED, command=self.eliminar_empleado)
        self.btn_eliminar.pack(side=tk.LEFT)

        self.treeview_empleados.bind("<<TreeviewSelect>>", self.llenar_campos)

        self.btn_regresar = tk.Button(self.master, text="Regresar", command=self.mover_inicio)
        self.btn_regresar.pack(side=tk.RIGHT)

    def mover_inicio(self):
        self.destroy()
        abrir_ventana(VentanaNomina)

    def guardar_empleado(self):
        cedula = self.entry_cedula.get()
        nombre = self.entry_nombre.get()
        fecha = self.entry_fecha.get()
        sueldo = self.entry_sueldo.get()
        ingresarEmpleado = "INGRESAR|EMPLEADO|(CODIGO_MOT, CEDULA_EMP, NOMBRE_EMP, APELLIDO_EMP, FECHA_ING_EMP, SUELDO_EMP)|(" + ", " + str(cedula) + ", " + str(nombre) + ", " + str(fecha) + ", " + str(sueldo) + ")"
        print(ingresarEmpleado)
        if cedula and nombre and fecha and sueldo:
            empleado = (cedula, nombre, fecha, sueldo)
            self.empleados.append(empleado)
            self.listbox_empleados.insert(tk.END, empleado)
            self.limpiar_campos()
            messagebox.showinfo("Información", "Empleado guardado exitosamente.")
        else:
            messagebox.showwarning("Advertencia", "Ingrese todos los campos requeridos.")

    def modificar_empleado(self):
        seleccion = self.listbox_empleados.curselection()

        if seleccion:
            indice = seleccion[0]
            empleado_actual = self.listbox_empleados.get(indice)
            empleado_modificado = self.get_campos_empleado()

            if empleado_modificado:
                self.empleados[indice] = empleado_modificado
                self.listbox_empleados.delete(indice)
                self.listbox_empleados.insert(indice, empleado_modificado)
                self.limpiar_campos()
                messagebox.showinfo("Información", "Empleado modificado exitosamente.")
            else:
                messagebox.showwarning("Advertencia", "Ingrese todos los campos requeridos.")
        else:
            messagebox.showwarning("Advertencia", "Seleccione un empleado para modificar.")

    def eliminar_empleado(self):
        seleccion = self.listbox_empleados.curselection()

        if seleccion:
            indice = seleccion[0]
            empleado = self.listbox_empleados.get(indice)
            confirmacion = messagebox.askyesno("Confirmación", f"¿Está seguro que desea eliminar al empleado '{empleado}'?")

            if confirmacion:
                self.empleados.pop(indice)
                self.listbox_empleados.delete(indice)
                messagebox.showinfo("Información", "Empleado eliminado exitosamente.")
        else:
            messagebox.showwarning("Advertencia", "Seleccione un empleado para eliminar.")    
            
    def llenar_campos(self, event):
        seleccion = self.listbox_empleados.curselection()

        if seleccion:
            self.btn_modificar.config(state=tk.NORMAL)
            self.btn_eliminar.config(state=tk.NORMAL)
            indice = seleccion[0]
            empleado = self.listbox_empleados.get(indice)
            self.entry_cedula.delete(0, tk.END)
            self.entry_cedula.insert(tk.END, empleado[0])
            self.entry_nombre.delete(0, tk.END)
            self.entry_nombre.insert(tk.END, empleado[1])
            self.entry_fecha.delete(0, tk.END)
            self.entry_fecha.insert(tk.END, empleado[2])
            self.entry_sueldo.delete(0, tk.END)
            self.entry_sueldo.insert(tk.END, empleado[3])
        else:
            self.btn_modificar.config(state=tk.DISABLED)
            self.btn_eliminar.config(state=tk.DISABLED)

    def get_campos_empleado(self):
        cedula = self.entry_cedula.get()
        nombre = self.entry_nombre.get()
        fecha = self.entry_fecha.get()
        sueldo = self.entry_sueldo.get()

        if cedula and nombre and fecha and sueldo:
            return (cedula, nombre, fecha, sueldo)
        else:
            return None

    def limpiar_campos(self):
        self.entry_cedula.delete(0, tk.END)
        self.entry_nombre.delete(0, tk.END)
        self.entry_fecha.delete(0, tk.END)
        self.entry_sueldo.delete(0, tk.END)

class VentanaCuenta(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Pantalla de cuenta")
        self.geometry("600x400")
        
        self.etiqueta_opciones = tk.Label(self, text="Opciones de Tipo de Cuenta")
        self.etiqueta_opciones.pack()
        
        self.frame_contenedor = tk.Frame(self)
        self.frame_contenedor.pack(pady=20)

        self.boton_opcion_1 = tk.Button(self.frame_contenedor, text="Ingresar tipo de cuenta", command=self.ingresar_tipoCuenta)
        self.boton_opcion_1.pack(side="left", padx=10)
        
        self.etiqueta_opciones = tk.Label(self, text="Opciones de Cuenta")
        self.etiqueta_opciones.pack()
        
        self.frame_contenedor = tk.Frame(self)
        self.frame_contenedor.pack(pady=20)

        self.boton_opcion_5 = tk.Button(self.frame_contenedor, text="Ingresar cuenta", command=self.ingresar_cuenta)
        self.boton_opcion_5.pack(side="left", padx=10)
        
        self.etiqueta_opciones = tk.Label(self, text="Opciones de Contabilidad")
        self.etiqueta_opciones.pack()
        
        self.frame_contenedor = tk.Frame(self)
        self.frame_contenedor.pack(pady=20)
        
        self.boton_opcion_8 = tk.Button(self.frame_contenedor, text="Ingresar asiento contable", command=self.agregarAsiento)
        self.boton_opcion_8.pack(side="left", padx=10)
        self.boton_opcion_9 = tk.Button(self.frame_contenedor, text="Modificar asiento contable")
        self.boton_opcion_9.pack(side="left", padx=10)
        self.boton_opcion_10 = tk.Button(self.frame_contenedor, text="Eliminar asiento contable")
        self.boton_opcion_10.pack(side="left", padx=10)
        self.boton_opcion_11 = tk.Button(self.frame_contenedor, text="Consultar asiento contable")
        self.boton_opcion_11.pack(side="left", padx=10)
        
        self.etiqueta_opciones = tk.Label(self, text="Opciones de Reportes")
        self.etiqueta_opciones.pack()
        
        self.frame_contenedor = tk.Frame(self)
        self.frame_contenedor.pack(pady=10)
        
        self.boton_opcion_12 = tk.Button(self.frame_contenedor, text="Balance general")
        self.boton_opcion_12.pack(side="left", padx=5)
        self.boton_opcion_13 = tk.Button(self.frame_contenedor, text="Estado de resultados")
        self.boton_opcion_13.pack(side="left", padx=5)
        
        self.boton_regresar = tk.Button(self, text="Regresar", command=self.mover_inicio)
        self.boton_regresar.pack()
        
    def ingresar_cuenta(self):
        cerrar_ventana(self)
        abrir_ventana(VentanaIngresarCuenta)

    def mover_inicio(self):
        cerrar_ventana(self)
        abrir_ventana(VentanaOpciones)
    
    def ingresar_tipoCuenta(self):
        cerrar_ventana(self)
        abrir_ventana(VentanaIngresarTipoCuenta)

    def agregarAsiento(self):
        cerrar_ventana(self)
        abrir_ventana(VentanaAgregarAsiento)

class VentanaIngresarTipoCuenta(tk.Tk):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.geometry("600x400")
        self.cuentas = []
        self.create_widgets()

    def create_widgets(self):
        self.label_nombre_cuenta = tk.Label(self.master, text="Nombre del tipo de cuenta:")
        self.label_nombre_cuenta.pack()
        self.entry_nombre_cuenta = tk.Entry(self.master)
        self.entry_nombre_cuenta.pack()

        self.btn_guardar_cuenta = tk.Button(self.master, text="Guardar", command=self.guardar_tipo_cuenta)
        self.btn_guardar_cuenta.pack()

        self.label_cuentas_guardadas = tk.Label(self.master, text="Cuentas Guardadas:")
        self.label_cuentas_guardadas.pack()

        self.treeview_cuentas = ttk.Treeview(self.master, columns=("codigo", "nombre"), show="headings")
        self.treeview_cuentas.heading("codigo", text="Código")
        self.treeview_cuentas.heading("nombre", text="Nombre")
        self.treeview_cuentas.pack()

        self.btn_modificar = tk.Button(self.master, text="Modificar", state=tk.DISABLED, command=self.modificar_tipo_cuenta)
        self.btn_modificar.pack(side=tk.LEFT, padx=5)

        self.btn_eliminar = tk.Button(self.master, text="Eliminar", state=tk.DISABLED, command=self.eliminar_tipo_cuenta)
        self.btn_eliminar.pack(side=tk.LEFT, padx=5)

        self.treeview_cuentas.bind("<<TreeviewSelect>>", self.actualizar_botones)

        self.btn_regresar = tk.Button(self.master, text="Regresar", command=self.mover_inicio)
        self.btn_regresar.pack(side=tk.RIGHT)
    
    def mover_inicio(self):
        cerrar_ventana(self)
        abrir_ventana(VentanaCuenta)

    def guardar_tipo_cuenta(self):
        nombre_tipo_cuenta = self.entry_nombre_cuenta.get()
        id = cm.generar_id_tipo_cuenta()
        ingresarTipoCuenta = "INGRESAR|TIPO_CUENTA|(CODIGO_TC,NOMBRE_TC)|("+id+","+nombre_tipo_cuenta+")"
        print(ingresarTipoCuenta)
        if nombre_tipo_cuenta:
            self.cuentas.append(nombre_tipo_cuenta)
            self.listbox_cuentas.insert(tk.END, nombre_tipo_cuenta)
            self.entry_nombre_cuenta.delete(0, tk.END)
            messagebox.showinfo("Información", "Cuenta guardada exitosamente.")
        else:
            messagebox.showwarning("Advertencia", "Ingrese un nombre de cuenta válido.")

    def modificar_tipo_cuenta(self):
        seleccion = self.listbox_cuentas.curselection()

        if seleccion:
            indice = seleccion[0]
            nombre_cuenta_actual = self.listbox_cuentas.get(indice)
            nombre_cuenta_modificado = self.entry_nombre_cuenta.get()

            if nombre_cuenta_modificado:
                self.cuentas[indice] = nombre_cuenta_modificado
                self.listbox_cuentas.delete(indice)
                self.listbox_cuentas.insert(indice, nombre_cuenta_modificado)
                self.entry_nombre_cuenta.delete(0, tk.END)
                messagebox.showinfo("Información", "Cuenta modificada exitosamente.")
            else:
                messagebox.showwarning("Advertencia", "Ingrese un nombre de cuenta válido.")
        else:
            messagebox.showwarning("Advertencia", "Seleccione una cuenta para modificar.")

    def eliminar_tipo_cuenta(self):
        seleccion = self.listbox_cuentas.curselection()

        if seleccion:
            indice = seleccion[0]
            nombre_cuenta = self.listbox_cuentas.get(indice)
            confirmacion = messagebox.askyesno("Confirmación", f"¿Está seguro que desea eliminar la cuenta '{nombre_cuenta}'?")

            if confirmacion:
                self.cuentas.pop(indice)
                self.listbox_cuentas.delete(indice)
                messagebox.showinfo("Información", "Cuenta eliminada exitosamente.")
        else:
            messagebox.showwarning("Advertencia", "Seleccione una cuenta para eliminar.")

    def actualizar_botones(self, event):
        seleccion = self.listbox_cuentas.curselection()

        if seleccion:
            self.btn_modificar.config(state=tk.NORMAL)
            self.btn_eliminar.config(state=tk.NORMAL)
        else:
            self.btn_modificar.config(state=tk.DISABLED)
            self.btn_eliminar.config(state=tk.DISABLED)

class VentanaIngresarCuenta(tk.Tk):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.geometry("600x400")
        self.cuentas = []
        self.tipos_cuenta = []
        self.create_widgets()

    def create_widgets(self):
        self.label_nombre_cuenta = tk.Label(self.master, text="Nombre de la Cuenta:")
        self.label_nombre_cuenta.pack()
        self.entry_nombre_cuenta = tk.Entry(self.master)
        self.entry_nombre_cuenta.pack()

        self.label_tipo_cuenta = tk.Label(self.master, text="Tipo de Cuenta:")
        self.label_tipo_cuenta.pack()
        self.combobox_tipo_cuenta = ttk.Combobox(self.master, values=self.tipos_cuenta)
        self.combobox_tipo_cuenta.pack()

        self.btn_guardar_cuenta = tk.Button(self.master, text="Guardar", command=self.guardar_cuenta)
        self.btn_guardar_cuenta.pack()

        self.label_cuentas_guardadas = tk.Label(self.master, text="Cuentas Guardadas:")
        self.label_cuentas_guardadas.pack()

        self.treeview_cuentas = ttk.Treeview(self.master, columns=("codigo", "nombre"), show="headings")
        self.treeview_cuentas.heading("codigo", text="Código")
        self.treeview_cuentas.heading("nombre", text="Nombre")
        self.treeview_cuentas.pack()

        self.btn_modificar = tk.Button(self.master, text="Modificar", state=tk.DISABLED, command=self.modificar_cuenta)
        self.btn_modificar.pack(side=tk.LEFT, padx=5)

        self.btn_eliminar = tk.Button(self.master, text="Eliminar", state=tk.DISABLED, command=self.eliminar_cuenta)
        self.btn_eliminar.pack(side=tk.LEFT, padx=5)

        self.treeview_cuentas.bind("<<TreeviewSelect>>", self.actualizar_botones)

        self.btn_regresar = tk.Button(self.master, text="Regresar", command=self.mover_atras)
        self.btn_regresar.pack(side=tk.RIGHT)

    def mover_atras(self):
        cerrar_ventana(self)
        abrir_ventana(VentanaCuenta)

    def guardar_cuenta(self):
        nombre_cuenta = self.entry_nombre_cuenta.get()
        tipo_cuenta = self.combobox_tipo_cuenta.get()
        id = cm.generar_id_cuenta()
        ingresarCuenta = "INGRESAR|MOTIVO|(CODIGO_TC,CODIGO_CUE,NOMBRE_CUE)|("+id+","+nombre_cuenta+")"
        print(ingresarCuenta)
        if nombre_cuenta and tipo_cuenta:
            self.cuentas.append((nombre_cuenta, tipo_cuenta))
            cuenta_text = f"{nombre_cuenta} - {tipo_cuenta}"
            self.listbox_cuentas.insert(tk.END, cuenta_text)
            self.entry_nombre_cuenta.delete(0, tk.END)
            messagebox.showinfo("Información", "Cuenta guardada exitosamente.")
        else:
            messagebox.showwarning("Advertencia", "Ingrese un nombre de cuenta y seleccione un tipo de cuenta.")

    def modificar_cuenta(self):
        seleccion = self.listbox_cuentas.curselection()

        if seleccion:
            indice = seleccion[0]
            cuenta_actual = self.listbox_cuentas.get(indice)
            nombre_cuenta_actual, tipo_cuenta_actual = cuenta_actual.split(" - ")
            nombre_cuenta_modificado = self.entry_nombre_cuenta.get()
            tipo_cuenta_modificado = self.combobox_tipo_cuenta.get()

            if nombre_cuenta_modificado and tipo_cuenta_modificado:
                cuenta_modificada = f"{nombre_cuenta_modificado} - {tipo_cuenta_modificado}"
                self.cuentas[indice] = (nombre_cuenta_modificado, tipo_cuenta_modificado)
                self.listbox_cuentas.delete(indice)
                self.listbox_cuentas.insert(indice, cuenta_modificada)
                self.entry_nombre_cuenta.delete(0, tk.END)
                messagebox.showinfo("Información", "Cuenta modificada exitosamente.")
            else:
                messagebox.showwarning("Advertencia", "Ingrese un nombre de cuenta válido y seleccione un tipo de cuenta.")
        else:
            messagebox.showwarning("Advertencia", "Seleccione una cuenta para modificar.")

    def eliminar_cuenta(self):
        seleccion = self.listbox_cuentas.curselection()

        if seleccion:
            indice = seleccion[0]
            cuenta = self.listbox_cuentas.get(indice)
            confirmacion = messagebox.askyesno("Confirmación", f"¿Está seguro que desea eliminar la cuenta '{cuenta}'?")

            if confirmacion:
                self.cuentas.pop(indice)
                self.listbox_cuentas.delete(indice)
                messagebox.showinfo("Información", "Cuenta eliminada exitosamente.")
        else:
            messagebox.showwarning("Advertencia", "Seleccione una cuenta para eliminar.")

    def actualizar_botones(self, event):
        seleccion = self.listbox_cuentas.curselection()

        if seleccion:
            self.btn_modificar.config(state=tk.NORMAL)
            self.btn_eliminar.config(state=tk.NORMAL)
        else:
            self.btn_modificar.config(state=tk.DISABLED)
            self.btn_eliminar.config(state=tk.DISABLED)

class VentanaAgregarAsiento(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Pantalla de agregar asiento")
        self.geometry("600x400")
        
        self.etiqueta_motivo = tk.Label(self, text="Motivo")
        self.etiqueta_motivo.pack()
        
        self.campo_motivo = tk.Entry(self)
        self.campo_motivo.pack()
        
        self.etiqueta_monto = tk.Label(self, text="Monto")
        self.etiqueta_monto.pack()
        
        self.campo_monto = tk.Entry(self)
        self.campo_monto.pack()
        
        self.etiqueta_fecha = tk.Label(self, text="Fecha")
        self.etiqueta_fecha.pack()
        
        self.campo_fecha = tk.Entry(self)
        self.campo_fecha.pack()
        
        self.boton_guardar = tk.Button(self, text="Guardar", command=self.guardar_asiento)
        self.boton_guardar.pack()
        
        self.boton_regresar = tk.Button(self, text="Regresar", command=self.mover_inicio)
        self.boton_regresar.pack()
        
    def guardar_asiento(self):
        # Lógica para guardar el asiento
        self.campo_motivo.delete(0, 'end')
        self.campo_monto.delete(0, 'end')
        self.campo_fecha.delete(0, 'end')

    def mover_inicio(self):
        cerrar_ventana(self)
        abrir_ventana(VentanaCuenta)

# Crear una instancia de la clase VentanaLogin y ejecutar el bucle principal
ventana = VentanaLogin()
ventana.mainloop()