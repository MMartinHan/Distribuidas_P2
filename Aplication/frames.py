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
        data = b''
        data += mi_socket.recv(1024)
        print(data)
        data_decoded = pickle.loads(data)
        for motivo in data_decoded:
            self.treeview_motivos.insert('', 'end', values=motivo)
        mi_socket.close()

    def mover_inicio(self):
        cerrar_ventana(self)
        abrir_ventana(VentanaNomina)

    def guardar_motivo(self):
        nombre_motivo = self.entry_nombre_motivo.get()
        id = nm.generar_id()
        ingresoMotivo = "INGRESAR|MOTIVO|(CODIGO_MOT,NOMBRE_MOT)|"+id+","+nombre_motivo
        mi_socket = crear_socket()
        mi_socket.send(ingresoMotivo.encode("utf-8"))
        respuesta = mi_socket.recv(1024)
        respuesta = respuesta.decode("utf-8")
        print(respuesta)
        mi_socket.close()
        self.entry_nombre_motivo.delete(0, 'end')  # Borrar contenido del campo de entrada
        self.rellenar_tabla()
        
    def modificar_motivo(self):
        seleccion = self.treeview_motivos.selection()

        if seleccion:
            # Obtener los valores actuales del motivo seleccionado
            item = self.treeview_motivos.item(seleccion)
            codigo_actual = item['values'][0]
            nombre_actual = item['values'][1]
            print(codigo_actual)
            print(nombre_actual)
            codigo_actual = str(codigo_actual)
            nuevo_nombre = self.entry_nombre_motivo.get()
            modificarMotivo = "MODIFICAR|MOTIVO|"+nuevo_nombre+"|"+codigo_actual
            mi_socket = crear_socket()
            mi_socket.send(modificarMotivo.encode("utf-8"))
            respuesta = mi_socket.recv(1024)
            respuesta = respuesta.decode("utf-8")    
            mi_socket.close()
            self.rellenar_tabla()


    def eliminar_motivo(self):
        seleccion = self.treeview_motivos.selection()
        if seleccion:
            item = self.treeview_motivos.item(seleccion)
            codigo_actual = item['values'][0]
            codigo_actual = str(codigo_actual)
            eliminarMotivo = "ELIMINAR|MOTIVO|CODIGO_MOT|"+codigo_actual
            mi_socket = crear_socket()
            mi_socket.send(eliminarMotivo.encode("utf-8"))
            respuesta = mi_socket.recv(1024)
            respuesta = respuesta.decode("utf-8")    
            mi_socket.close()
            self.rellenar_tabla()

    def actualizar_botones(self, event):
        seleccion = self.treeview_motivos.selection()

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
        self.geometry("1300x600")
        self.empleados = []
        self.create_widgets()
        self.rellenar_tabla()

    def create_widgets(self):
        
        self.label_motivo = tk.Label(self.master, text="Escoga el motivo")
        self.label_motivo.pack()
        op = self.rellenar_combobox()
        opcion_seleccionada = tk.StringVar()
        self.combo_motivo = ttk.Combobox(self.master, textvariable=opcion_seleccionada, values=op, state="readonly")
        self.combo_motivo.pack()
        
        
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

        self.treeview_empleados = ttk.Treeview(self.master, columns=("motivo","cedula", "nombre", "apellido", "fecha_ingreso", "sueldo"), show="headings")
        self.treeview_empleados.heading("motivo", text="Motivo")
        self.treeview_empleados.heading("cedula", text="Cédula")
        self.treeview_empleados.heading("nombre", text="Nombre")
        self.treeview_empleados.heading("apellido", text="Apellido")
        self.treeview_empleados.heading("fecha_ingreso", text="Fecha de ingreso")
        self.treeview_empleados.heading("sueldo", text="Sueldo")
        self.treeview_empleados.column("motivo", anchor=tk.CENTER)
        self.treeview_empleados.column("cedula", anchor=tk.CENTER)
        self.treeview_empleados.column("nombre", anchor=tk.CENTER)
        self.treeview_empleados.column("apellido", anchor=tk.CENTER)
        self.treeview_empleados.column("fecha_ingreso", anchor=tk.CENTER)
        self.treeview_empleados.column("sueldo", anchor=tk.CENTER)
        self.treeview_empleados.pack()

        self.btn_modificar = tk.Button(self.master, text="Modificar", state=tk.DISABLED, command=self.modificar_empleado)
        self.btn_modificar.pack(side=tk.LEFT)

        self.btn_eliminar = tk.Button(self.master, text="Eliminar", state=tk.DISABLED, command=self.eliminar_empleado)
        self.btn_eliminar.pack(side=tk.LEFT)

        self.treeview_empleados.bind("<<TreeviewSelect>>", self.actualizar_botones)

        self.btn_regresar = tk.Button(self.master, text="Regresar", command=self.mover_inicio)
        self.btn_regresar.pack(side=tk.RIGHT)

    def rellenar_combobox(self):
        opciones = nm.consultar_motivos()
        return opciones
    
    def mover_inicio(self):
        self.destroy()
        abrir_ventana(VentanaNomina)
    
    def rellenar_tabla(self):
        mi_socket = crear_socket()
        consultaMotivos = "CONSULTAR_EMPLEADO|EMPLEADO|*"
        mi_socket.send(consultaMotivos.encode("utf-8"))
        self.treeview_empleados.delete(*self.treeview_empleados.get_children())
        data = b''
        data += mi_socket.recv(1024)
        print(data)
        data_decoded = pickle.loads(data)
        for motivo in data_decoded:
            self.treeview_empleados.insert('', 'end', values=motivo)
        mi_socket.close()

    def guardar_empleado(self):
        codico_mot = self.combo_motivo.get()
        cedula = self.entry_cedula.get()
        nombre = self.entry_nombre.get()
        apellido = self.entry_apellido.get()
        fecha = self.entry_fecha.get()
        sueldo = self.entry_sueldo.get()
        ingresarEmpleado = "INGRESAR|EMPLEADO|(CODIGO_MOT, CEDULA_EMP, NOMBRE_EMP, APELLIDO_EMP, FECHA_ING_EMP, SUELDO_EMP)|"+ str(codico_mot[0]) + ", " + str(cedula) + ", " + str(nombre)+ ", "+ str(apellido) + ", " + str(fecha) + ", " + str(sueldo)
        print(ingresarEmpleado)
        mi_socket = crear_socket()
        mi_socket.send(ingresarEmpleado.encode("utf-8"))
        respuesta = mi_socket.recv(1024)
        respuesta = respuesta.decode("utf-8")
        print(respuesta)
        mi_socket.close()
        self.combo_motivo.set('')  # Borrar contenido del campo de entrada
        self.entry_cedula.delete(0, 'end')  
        self.entry_nombre.delete(0, 'end')  
        self.entry_apellido.delete(0, 'end')  
        self.entry_fecha.delete(0, 'end')  
        self.entry_sueldo.delete(0, 'end')  
        self.rellenar_tabla()

    def modificar_empleado(self):
        seleccion = self.treeview_empleados.selection()

        if seleccion:
            # Obtener los valores actuales del motivo seleccionado
            item = self.treeview_empleados.item(seleccion)
            cedula_actual = item['values'][1]
            codico_mot_nuevo = self.combo_motivo.get()
            nombre_nuevo = self.entry_nombre.get()
            apellido_nuevo = self.entry_apellido.get()
            fecha_nuevo = self.entry_fecha.get()
            sueldo_nuevo = self.entry_sueldo.get()
            modificarMotivo = "MODIFICAR_EMPLEADO|EMPLEADO|"+codico_mot_nuevo[0]+"|"+nombre_nuevo+"|"+apellido_nuevo+"|"+fecha_nuevo+"|"+str(sueldo_nuevo)+"|"+str(cedula_actual)
            print(modificarMotivo)
            mi_socket = crear_socket()
            mi_socket.send(modificarMotivo.encode("utf-8"))
            respuesta = mi_socket.recv(1024)
            respuesta = respuesta.decode("utf-8")    
            mi_socket.close()
            self.combo_motivo.set('')
            self.entry_cedula.delete(0, tk.END)
            self.entry_nombre.delete(0, tk.END)
            self.entry_apellido.delete(0, tk.END)
            self.entry_fecha.delete(0, tk.END)
            self.entry_sueldo.delete(0, tk.END)
            self.rellenar_tabla()

    def eliminar_empleado(self):
        seleccion = self.treeview_empleados.selection()
        if seleccion:
            item = self.treeview_empleados.item(seleccion)
            cedula_actual = item['values'][1]
            cedula_actual = str(cedula_actual)
            eliminarMotivo = "ELIMINAR|EMPLEADO|CEDULA_EMP|"+cedula_actual
            mi_socket = crear_socket()
            mi_socket.send(eliminarMotivo.encode("utf-8"))
            respuesta = mi_socket.recv(1024)
            respuesta = respuesta.decode("utf-8")    
            mi_socket.close()
            self.combo_motivo.set('')
            self.entry_cedula.delete(0, tk.END)
            self.entry_nombre.delete(0, tk.END)
            self.entry_apellido.delete(0, tk.END)
            self.entry_fecha.delete(0, tk.END)
            self.entry_sueldo.delete(0, tk.END)
            self.rellenar_tabla()  
            
    def actualizar_botones(self, event):
        seleccion = self.treeview_empleados.selection()

        if seleccion:
            self.btn_modificar.config(state=tk.NORMAL)
            self.btn_eliminar.config(state=tk.NORMAL)
            indice = seleccion[0]
            empleado = self.treeview_empleados.item(indice)['values']
            print(empleado)
            self.combo_motivo.set('')
            self.combo_motivo.set(empleado[0])
            self.entry_cedula.delete(0, tk.END)
            self.entry_cedula.insert(tk.END, empleado[1])
            self.entry_nombre.delete(0, tk.END)
            self.entry_nombre.insert(tk.END, empleado[2])
            self.entry_apellido.delete(0, tk.END)
            self.entry_apellido.insert(tk.END, empleado[3])
            self.entry_fecha.delete(0, tk.END)
            self.entry_fecha.insert(tk.END, empleado[4])
            self.entry_sueldo.delete(0, tk.END)
            self.entry_sueldo.insert(tk.END, empleado[5])
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
        
        self.boton_opcion_8 = tk.Button(self.frame_contenedor, text="Asientos contables", command=self.agregarAsiento)
        self.boton_opcion_8.pack(side="left", padx=10)
        
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
        abrir_ventana(VentanaAsiento)

class VentanaIngresarTipoCuenta(tk.Tk):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.geometry("600x400")
        self.cuentas = []
        self.create_widgets()
        self.rellenar_tabla()

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
        ingresoTC = "INGRESAR|TIPO_CUENTA|(CODIGO_TC,NOMBRE_TC)|"+id+","+nombre_tipo_cuenta
        print(ingresoTC)
        mi_socket = crear_socket()
        mi_socket.send(ingresoTC.encode("utf-8"))
        respuesta = mi_socket.recv(1024).decode("utf-8")
        mi_socket.close()
        
        self.entry_nombre_cuenta.delete(0, 'end')  # Borrar contenido del campo de entrada
        self.rellenar_tabla()
    
    def rellenar_tabla(self):
        mi_socket = crear_socket()
        consultaMotivos = "CONSULTAR|TIPO_CUENTA|*"
        mi_socket.send(consultaMotivos.encode("utf-8"))
        self.treeview_cuentas.delete(*self.treeview_cuentas.get_children())
        data = b''
        data += mi_socket.recv(1024)
        data_decoded = pickle.loads(data)
        for motivo in data_decoded:
            self.treeview_cuentas.insert('', 'end', values=motivo)
        mi_socket.close()

    def modificar_tipo_cuenta(self):
        seleccion = self.treeview_cuentas.selection()

        if seleccion:
            # Obtener los valores actuales del motivo seleccionado
            item = self.treeview_cuentas.item(seleccion)
            codigo_actual = item['values'][0]
            nombre_actual = item['values'][1]
            print(codigo_actual)
            print(nombre_actual)
            codigo_actual = str(codigo_actual)
            nuevo_nombre = self.entry_nombre_cuenta.get()
            modificarMotivo = "MODIFICAR_TC|TIPO_CUENTA|"+nuevo_nombre+"|"+codigo_actual
            mi_socket = crear_socket()
            mi_socket.send(modificarMotivo.encode("utf-8"))
            respuesta = mi_socket.recv(1024)
            respuesta = respuesta.decode("utf-8")    
            mi_socket.close()
            self.rellenar_tabla()


    def eliminar_tipo_cuenta(self):
        seleccion = self.treeview_cuentas.selection()
        if seleccion:
            item = self.treeview_cuentas.item(seleccion)
            codigo_actual = item['values'][0]
            codigo_actual = str(codigo_actual)
            eliminarTC = "ELIMINAR_TC|TIPO_CUENTA|"+codigo_actual
            mi_socket = crear_socket()
            mi_socket.send(eliminarTC.encode("utf-8"))
            respuesta = mi_socket.recv(1024)
            respuesta = respuesta.decode("utf-8")    
            mi_socket.close()
            self.rellenar_tabla()

    def actualizar_botones(self, event):
        seleccion = self.treeview_cuentas.selection()

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
        self.rellenar_tabla()

    def create_widgets(self):
        self.label_nombre_cuenta = tk.Label(self.master, text="Nombre de la Cuenta:")
        self.label_nombre_cuenta.pack()
        self.entry_nombre_cuenta = tk.Entry(self.master)
        self.entry_nombre_cuenta.pack()

        self.label_tipo_cuenta = tk.Label(self.master, text="Tipo de Cuenta:")
        self.label_tipo_cuenta.pack()
        opciones = cm.consultar_tipo_cuenta()
        self.combobox_tipo_cuenta = ttk.Combobox(self.master, values=opciones, state="readonly")
        self.combobox_tipo_cuenta.pack()

        self.btn_guardar_cuenta = tk.Button(self.master, text="Guardar", command=self.guardar_cuenta)
        self.btn_guardar_cuenta.pack()

        self.label_cuentas_guardadas = tk.Label(self.master, text="Cuentas Guardadas:")
        self.label_cuentas_guardadas.pack()

        self.treeview_cuentas = ttk.Treeview(self.master, columns=("codigo_tipo", "codigo_cuenta", "nombre_cuenta"), show="headings")
        self.treeview_cuentas.heading("codigo_tipo", text="CódigoTipoCuenta")
        self.treeview_cuentas.heading("codigo_cuenta", text="CódigoCuenta")
        self.treeview_cuentas.heading("nombre_cuenta", text="NombreCuenta")
        self.treeview_cuentas.pack()

        self.btn_modificar = tk.Button(self.master, text="Modificar", state=tk.DISABLED, command=self.modificar_cuenta)
        self.btn_modificar.pack(side=tk.LEFT, padx=5)

        self.btn_eliminar = tk.Button(self.master, text="Eliminar", state=tk.DISABLED, command=self.eliminar_cuenta)
        self.btn_eliminar.pack(side=tk.LEFT, padx=5)

        self.treeview_cuentas.bind("<<TreeviewSelect>>", self.actualizar_botones)

        self.btn_regresar = tk.Button(self.master, text="Regresar", command=self.mover_atras)
        self.btn_regresar.pack(side=tk.RIGHT)

    def rellenar_tabla(self):
        mi_socket = crear_socket()
        consultaMotivos = "CONSULTAR|CUENTA|*"
        mi_socket.send(consultaMotivos.encode("utf-8"))
        self.treeview_cuentas.delete(*self.treeview_cuentas.get_children())
        data = b''
        data += mi_socket.recv(1024)
        print(data)
        data_decoded = pickle.loads(data)
        for motivo in data_decoded:
            self.treeview_cuentas.insert('', 'end', values=motivo)
        mi_socket.close()

    def mover_atras(self):
        cerrar_ventana(self)
        abrir_ventana(VentanaCuenta)

    def guardar_cuenta(self):
        nombre_cuenta = self.entry_nombre_cuenta.get()
        tipo_cuenta = self.combobox_tipo_cuenta.get()
        tipo_cuenta = tipo_cuenta.split(" ")
        idTipoCuenta = tipo_cuenta[0]
        id = cm.generar_id_cuenta()
        ingresarCuenta = "INGRESAR|CUENTA|(CODIGO_TC,CODIGO_CUE,NOMBRE_CUE)|"+idTipoCuenta+","+id+","+nombre_cuenta
        mi_socket = crear_socket()
        mi_socket.send(ingresarCuenta.encode("utf-8"))
        respuesta = mi_socket.recv(1024).decode("utf-8")
        mi_socket.close()
        print(ingresarCuenta)
        self.rellenar_tabla()
    def modificar_cuenta(self):
        seleccion = self.treeview_cuentas.selection()

        if seleccion:
            # Obtener los valores actuales del motivo seleccionado
            item = self.treeview_cuentas.item(seleccion)
            cuenta_actual = item['values'][1]
            codigo_tc_nuevo = self.combobox_tipo_cuenta.get()
            nombre_cuenta_nuevo = self.entry_nombre_cuenta.get()
            modificarCuenta = "MODIFICAR_CUENTA|CUENTA|"+codigo_tc_nuevo[0]+"|"+str(cuenta_actual)+"|"+nombre_cuenta_nuevo
            print(modificarCuenta)
            mi_socket = crear_socket()
            mi_socket.send(modificarCuenta.encode("utf-8"))
            respuesta = mi_socket.recv(1024)
            respuesta = respuesta.decode("utf-8") 
            print(respuesta)   
            mi_socket.close()
            self.combobox_tipo_cuenta.set('')
            self.entry_nombre_cuenta.delete(0, tk.END)
            self.rellenar_tabla()
    
    def eliminar_cuenta(self):
        seleccion = self.treeview_cuentas.selection()
        if seleccion:
            item = self.treeview_cuentas.item(seleccion)
            cuenta_actual = item['values'][1]
            cuenta_actual = str(cuenta_actual)
            eliminarCuenta = "ELIMINAR|CUENTA|CODIGO_CUE|"+cuenta_actual
            mi_socket = crear_socket()
            mi_socket.send(eliminarCuenta.encode("utf-8"))
            respuesta = mi_socket.recv(1024)
            respuesta = respuesta.decode("utf-8")    
            mi_socket.close()
            self.combobox_tipo_cuenta.set('')
            self.entry_nombre_cuenta.delete(0, tk.END)
            self.rellenar_tabla()

    def actualizar_botones(self, event):
        seleccion = self.treeview_cuentas.selection()

        if seleccion:
            self.btn_modificar.config(state=tk.NORMAL)
            self.btn_eliminar.config(state=tk.NORMAL)
            indice = seleccion[0]
            cuenta = self.treeview_cuentas.item(indice)['values']
            print(cuenta)
            self.combobox_tipo_cuenta.set('')
            self.combobox_tipo_cuenta.set(cuenta[0])
            self.entry_nombre_cuenta.delete(0, tk.END)
            self.entry_nombre_cuenta.insert(tk.END, cuenta[2])
            
        else:
            self.btn_modificar.config(state=tk.DISABLED)
            self.btn_eliminar.config(state=tk.DISABLED)

class VentanaAsiento(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Pantalla de asientos contables")
        self.geometry("1050x400")

        self.boton_ingresar_asiento = tk.Button(self, text="Ingresar asiento", command=self.ingresar_asiento)
        self.boton_ingresar_asiento.pack(side=tk.TOP, pady=10)

        self.label_asientos_contables = tk.Label(self, text="Asientos contables")
        self.label_asientos_contables.pack(side=tk.TOP, pady=10)

        self.treeview_asientos = ttk.Treeview(self.master, columns=("numero", "fecha", "observacion"), show="headings")
        self.treeview_asientos.heading("numero", text="Número")
        self.treeview_asientos.heading("fecha", text="Fecha")
        self.treeview_asientos.heading("observacion", text="Observación")
        self.treeview_asientos.pack()

        self.boton_eliminar_asiento = tk.Button(self, text="Eliminar asiento", state=tk.DISABLED)
        self.boton_eliminar_asiento.pack(side=tk.TOP, pady=10)

        self.boton_regresar = tk.Button(self, text="Regresar", command=self.mover_inicio)
        self.boton_regresar.pack(side=tk.BOTTOM, pady=10)

        self.treeview_asientos.bind("<<TreeviewSelect>>", self.actualizar_botones)  # Agregado evento
        self.treeview_asientos.bind("<<TreeviewDoubleClick>>", self.abrir_asiento)  # Agregado evento

        self.llenar_tabla()

    def abrir_asiento(self, event):  # Agregado parámetro de evento
        seleccion = self.treeview_asientos.selection()
        if seleccion:
            item = self.treeview_asientos.item(seleccion)
            numero_asiento = item['values'][0]
            cerrar_ventana(self)
            abrir_ventana(ventanaModificarAsiento)

    def actualizar_botones(self, event):  # Agregado parámetro de evento
        seleccion = self.treeview_asientos.selection()
        if seleccion:
            self.boton_eliminar_asiento.config(state=tk.NORMAL)
        else:
            self.boton_eliminar_asiento.config(state=tk.DISABLED)

    def ingresar_asiento(self):
        cerrar_ventana(self)
        abrir_ventana(VentanaIngresarAsiento)

    def mover_inicio(self):
        cerrar_ventana(self)
        abrir_ventana(VentanaCuenta)

    def llenar_tabla(self):
        self.treeview_asientos.delete(*self.treeview_asientos.get_children())
        mi_socket = crear_socket()
        consultaAsientos = "OBTENER_ASIENTOS|COMPROBANTE|CODIGO_COM|FECHA_COM|OBSERVACIONES_COM"
        mi_socket.send(consultaAsientos.encode("utf-8"))
        data = b''
        data += mi_socket.recv(1024)
        print(data)
        data_decoded = pickle.loads(data)
        
        codigos_com = set()
        for motivo in data_decoded:
            codigo_com = motivo[1]  # Suponiendo que el código de "CODIGO_COM" está en la posición 1 de cada motivo
            if codigo_com not in codigos_com:
                self.treeview_asientos.insert('', 'end', values=motivo)
                codigos_com.add(codigo_com)
                
        mi_socket.close()


class VentanaIngresarAsiento(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Pantalla de agregar asiento")
        self.geometry("900x450")

        self.label_cabecera_asiento = tk.Label(self, text="Cabecera del asiento")
        self.label_numero_asiento = tk.Label(self, text="Número de asiento")
        self.entry_numero_asiento = tk.Entry(self, state="normal")
        id_asiento = cm.generar_id_asiento()
        print(id_asiento)
        print(type(id_asiento))
        self.entry_numero_asiento.insert(0, id_asiento)
        self.entry_numero_asiento.config(state="disabled")
        self.label_fecha_asiento = tk.Label(self, text="Fecha de asiento")
        self.entry_fecha_asiento = tk.Entry(self)
        self.label_observacion_asiento = tk.Label(self, text="Observación de asiento")
        self.entry_observacion_asiento = tk.Entry(self)
        self.label_detalle_asiento = tk.Label(self, text="Detalle del asiento")
        self.label_cuenta_asiento = tk.Label(self, text="Cuenta")
        op = self.llenar_combobox_cuenta()
        self.combobox_cuenta_asiento = ttk.Combobox(self, state="readonly", values=op)
        self.label_debe_asiento = tk.Label(self, text="Debe o Haber")
        op2 = ["Debe", "Haber"]
        self.combobox_debe_asiento = ttk.Combobox(self, state="readonly", values=op2)
        self.label_monto_cuenta = tk.Label(self, text="Monto")
        self.entry_monto_cuenta = tk.Entry(self)
        self.boton_agregar_cuenta = tk.Button(self, text="Agregar cuenta", command=self.agregar_cuenta)
        self.treeview_asiento = ttk.Treeview(self.master, columns=("tipoCuenta", "cuenta", "debe", "haber"), show="headings")
        self.treeview_asiento.heading("tipoCuenta", text="Tipo de cuenta")
        self.treeview_asiento.heading("cuenta", text="Cuenta")
        self.treeview_asiento.heading("debe", text="Debe")
        self.treeview_asiento.heading("haber", text="Haber")
        self.boton_modificar_cuenta = tk.Button(self, text="Modificar cuenta", state=tk.DISABLED, command=self.modificar_cuenta)
        self.boton_eliminar_cuenta = tk.Button(self, text="Eliminar cuenta", state=tk.DISABLED, command=self.eliminar_cuenta)
        self.boton_guardar_asiento = tk.Button(self, text="Guardar asiento", command=self.guardar_asiento)
        self.boton_regresar = tk.Button(self, text="Regresar", command=self.mover_inicio)
        self.treeview_asiento.bind("<<TreeviewSelect>>", self.actualizar_botones)

        self.label_cabecera_asiento.grid(row=0, column=0, columnspan=4, pady=10)
        self.label_numero_asiento.grid(row=1, column=0, sticky=tk.E, padx=10)
        self.entry_numero_asiento.grid(row=1, column=1, sticky=tk.W, padx=10)
        self.label_fecha_asiento.grid(row=1, column=2, sticky=tk.E, padx=10)
        self.entry_fecha_asiento.grid(row=1, column=3, sticky=tk.W, padx=10)
        self.label_observacion_asiento.grid(row=2, column=0, sticky=tk.E, padx=10)
        self.entry_observacion_asiento.grid(row=2, column=1, columnspan=3, sticky=tk.W, padx=10)
        self.label_detalle_asiento.grid(row=4, column=0, columnspan=4, pady=10)
        self.label_cuenta_asiento.grid(row=5, column=0, pady=10)
        self.combobox_cuenta_asiento.grid(row=5, column=1, pady=10)
        self.label_debe_asiento.grid(row=5, column=2, pady=10)
        self.combobox_debe_asiento.grid(row=5, column=3, pady=10)
        self.label_monto_cuenta.grid(row=5, column=4, pady=10)
        self.entry_monto_cuenta.grid(row=5, column=5, pady=10)
        self.boton_agregar_cuenta.grid(row=5, column=6, pady=10)
        self.treeview_asiento.grid(row=6, column=0, columnspan=7)
        self.boton_modificar_cuenta.grid(row=7, column=0, columnspan=3, padx=10, pady=10)
        self.boton_eliminar_cuenta.grid(row=7, column=1, columnspan=3, pady=10)
        self.boton_guardar_asiento.grid(row=7, column=3, columnspan=7, pady=10)
        self.boton_regresar.grid(row=7, column=5, columnspan=7, pady=10)

    def mover_inicio(self):
        cerrar_ventana(self)
        abrir_ventana(VentanaAsiento)

    def eliminar_cuenta(self):
        seleccion = self.treeview_asiento.selection()
        if seleccion:
            self.treeview_asiento.delete(seleccion)
            self.boton_modificar_cuenta.config(state=tk.DISABLED)
            self.boton_eliminar_cuenta.config(state=tk.DISABLED)
            self.combobox_cuenta_asiento.set("")
            self.combobox_debe_asiento.set("")
            self.entry_monto_cuenta.delete(0, tk.END)

    def modificar_cuenta(self):
        seleccion = self.treeview_asiento.selection()
        if seleccion:
            self.agregar_cuenta()
            self.eliminar_cuenta()
            self.combobox_cuenta_asiento.set("")
            self.combobox_debe_asiento.set("")
            self.boton_modificar_cuenta.config(state=tk.DISABLED)
            self.boton_eliminar_cuenta.config(state=tk.DISABLED)
            self.combobox_cuenta_asiento.set("")
            self.combobox_debe_asiento.set("")
            self.entry_monto_cuenta.delete(0, tk.END)

    def guardar_asiento(self):
        cantidad_debe = 0
        cantidad_haber = 0
        for i in self.treeview_asiento.get_children():
            if self.treeview_asiento.item(i, "values")[2] != "0":
                cantidad_debe += int(self.treeview_asiento.item(i, "values")[2])
            elif self.treeview_asiento.item(i, "values")[3] != "0":
                cantidad_haber += int(self.treeview_asiento.item(i, "values")[3])
        mi_socket = crear_socket()
        validacion = "VERIFICAR_ASIENTO|"+str(cantidad_debe)+"|"+str(cantidad_haber)
        mi_socket.send(validacion.encode("utf-8"))
        result = mi_socket.recv(1024)
        mi_socket.close()
        result = int.from_bytes(result, 'big')
        result=bool(result)
        if result == True:
            codigo_comprobante = self.entry_numero_asiento.get()
            fecha = self.entry_fecha_asiento.get()
            observacion = self.entry_observacion_asiento.get()
            for i in self.treeview_asiento.get_children():
                mi_socket = crear_socket()
                consultaCuenta = "OBTENER_CODIGO_TC|TIPO_CUENTA|CODIGO_TC|"+self.treeview_asiento.item(i, "values")[0]
                mi_socket.send(consultaCuenta.encode("utf-8"))
                data = b''
                data += mi_socket.recv(1024)
                result = pickle.loads(data)
                print(result)
                print(type(result))
                mi_socket.close()
                result = str(result)
                result = result[3:-4]
                codigo_tc = result
                
                mi_socket = crear_socket()
                consultaCuenta = "OBTENER_CODIGO_CUENTA|CUENTA|CODIGO_CUE|"+self.treeview_asiento.item(i, "values")[1]
                mi_socket.send(consultaCuenta.encode("utf-8"))
                data = b''
                data += mi_socket.recv(1024)
                result = pickle.loads(data)
                print(result)
                print(type(result))
                mi_socket.close()
                result = str(result)
                result = result[3:-4]
                codigo_cuenta = result

                debe = self.treeview_asiento.item(i, "values")[2]
                haber = self.treeview_asiento.item(i, "values")[3]
                ingresoAsiento = "INGRESAR|COMPROBANTE|(CODIGO_TC, CODIGO_CUE, CODIGO_COM, FECHA_COM, OBSERVACIONES_COM, CANTIDAD_DEBE_COM, CANTIDAD_HABER_COM)|"+str(codigo_tc)+","+str(codigo_cuenta)+","+str(codigo_comprobante)+","+str(fecha)+","+str(observacion)+","+str(debe)+","+str(haber)
                mi_socket = crear_socket()
                mi_socket.send(ingresoAsiento.encode("utf-8"))
                result = mi_socket.recv(1024).decode("utf-8")
                print(result)
                print(ingresoAsiento)
        else:
            messagebox.showerror("Error", "El asiento no esta cuadrado")
            return
        print(result)
        print(type(result))
        pass

    def llenar_combobox_cuenta(self):
        opciones = cm.consultar_cuenta()
        return opciones
    
    def actualizar_botones(self, event):
        seleccion = self.treeview_asiento.selection()
        if seleccion:
            if self.treeview_asiento.item(seleccion, "values")[2] == "0":
                self.combobox_debe_asiento.set("Haber")
                self.entry_monto_cuenta.delete(0, tk.END)
                self.entry_monto_cuenta.insert(0, self.treeview_asiento.item(seleccion, "values")[3])
            elif self.treeview_asiento.item(seleccion, "values")[3] == "0":
                self.combobox_debe_asiento.set("Debe")
                self.entry_monto_cuenta.delete(0, tk.END)
                self.entry_monto_cuenta.insert(0, self.treeview_asiento.item(seleccion, "values")[2])
            string_buscado = self.treeview_asiento.item(seleccion, "values")[1]
            opciones = self.llenar_combobox_cuenta()
            for opcion in opciones:
                if string_buscado in opcion:
                    self.combobox_cuenta_asiento.set(opcion)

            self.boton_modificar_cuenta.config(state=tk.NORMAL)
            self.boton_eliminar_cuenta.config(state=tk.NORMAL)
        else:
            self.boton_modificar_cuenta.config(state=tk.DISABLED)
            self.boton_eliminar_cuenta.config(state=tk.DISABLED)
    
    def vaciar_campos(self):
        self.entry_monto_cuenta.delete(0, tk.END)
        self.combobox_cuenta_asiento.set("")
        self.combobox_debe_asiento.set("")

    def agregar_cuenta(self):
        tipo_cuenta = self.combobox_cuenta_asiento.get()
        tipo_cuenta = tipo_cuenta.split(" ")
        tc_id = tipo_cuenta[0]
        id_cuenta = tipo_cuenta[1]
        nombre_cuenta = tipo_cuenta[2]
        mi_socket = crear_socket()
        consultaCuenta = "OBTENER_NOMBRE_TC|TIPO_CUENTA|NOMBRE_TC|"+tc_id
        mi_socket.send(consultaCuenta.encode("utf-8"))
        data = b''
        data += mi_socket.recv(1024)
        result = pickle.loads(data)
        mi_socket.close()
        result = str(result)
        result = result[3:-4]
        if self.combobox_debe_asiento.get() == "Debe":
            self.treeview_asiento.insert("", tk.END, values=(result, nombre_cuenta, self.entry_monto_cuenta.get(), 0))
        elif self.combobox_debe_asiento.get() == "Haber":
            self.treeview_asiento.insert("", tk.END, values=(result, nombre_cuenta, 0, self.entry_monto_cuenta.get()))
        self.vaciar_campos()
        pass

class ventanaModificarAsiento(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Pantalla de agregar asiento")
        self.geometry("900x450")

        self.label_cabecera_asiento = tk.Label(self, text="Cabecera del asiento")
        self.label_numero_asiento = tk.Label(self, text="Número de asiento")
        self.entry_numero_asiento = tk.Entry(self, state="normal")
        id_asiento = cm.generar_id_asiento()
        print(id_asiento)
        print(type(id_asiento))
        self.entry_numero_asiento.insert(0, id_asiento)
        self.entry_numero_asiento.config(state="disabled")
        self.label_fecha_asiento = tk.Label(self, text="Fecha de asiento")
        self.entry_fecha_asiento = tk.Entry(self)
        self.label_observacion_asiento = tk.Label(self, text="Observación de asiento")
        self.entry_observacion_asiento = tk.Entry(self)
        self.label_detalle_asiento = tk.Label(self, text="Detalle del asiento")
        self.label_cuenta_asiento = tk.Label(self, text="Cuenta")
        op = self.llenar_combobox_cuenta()
        self.combobox_cuenta_asiento = ttk.Combobox(self, state="readonly", values=op)
        self.label_debe_asiento = tk.Label(self, text="Debe o Haber")
        op2 = ["Debe", "Haber"]
        self.combobox_debe_asiento = ttk.Combobox(self, state="readonly", values=op2)
        self.label_monto_cuenta = tk.Label(self, text="Monto")
        self.entry_monto_cuenta = tk.Entry(self)
        self.boton_agregar_cuenta = tk.Button(self, text="Agregar cuenta", command=self.agregar_cuenta)
        self.treeview_asiento = ttk.Treeview(self.master, columns=("tipoCuenta", "cuenta", "debe", "haber"), show="headings")
        self.treeview_asiento.heading("tipoCuenta", text="Tipo de cuenta")
        self.treeview_asiento.heading("cuenta", text="Cuenta")
        self.treeview_asiento.heading("debe", text="Debe")
        self.treeview_asiento.heading("haber", text="Haber")
        self.boton_modificar_cuenta = tk.Button(self, text="Modificar cuenta", state=tk.DISABLED, command=self.modificar_cuenta)
        self.boton_eliminar_cuenta = tk.Button(self, text="Eliminar cuenta", state=tk.DISABLED, command=self.eliminar_cuenta)
        self.boton_guardar_asiento = tk.Button(self, text="Guardar asiento", command=self.guardar_asiento)
        self.boton_regresar = tk.Button(self, text="Regresar", command=self.mover_inicio)
        self.treeview_asiento.bind("<<TreeviewSelect>>", self.actualizar_botones)

        self.label_cabecera_asiento.grid(row=0, column=0, columnspan=4, pady=10)
        self.label_numero_asiento.grid(row=1, column=0, sticky=tk.E, padx=10)
        self.entry_numero_asiento.grid(row=1, column=1, sticky=tk.W, padx=10)
        self.label_fecha_asiento.grid(row=1, column=2, sticky=tk.E, padx=10)
        self.entry_fecha_asiento.grid(row=1, column=3, sticky=tk.W, padx=10)
        self.label_observacion_asiento.grid(row=2, column=0, sticky=tk.E, padx=10)
        self.entry_observacion_asiento.grid(row=2, column=1, columnspan=3, sticky=tk.W, padx=10)
        self.label_detalle_asiento.grid(row=4, column=0, columnspan=4, pady=10)
        self.label_cuenta_asiento.grid(row=5, column=0, pady=10)
        self.combobox_cuenta_asiento.grid(row=5, column=1, pady=10)
        self.label_debe_asiento.grid(row=5, column=2, pady=10)
        self.combobox_debe_asiento.grid(row=5, column=3, pady=10)
        self.label_monto_cuenta.grid(row=5, column=4, pady=10)
        self.entry_monto_cuenta.grid(row=5, column=5, pady=10)
        self.boton_agregar_cuenta.grid(row=5, column=6, pady=10)
        self.treeview_asiento.grid(row=6, column=0, columnspan=7)
        self.boton_modificar_cuenta.grid(row=7, column=0, columnspan=3, padx=10, pady=10)
        self.boton_eliminar_cuenta.grid(row=7, column=1, columnspan=3, pady=10)
        self.boton_guardar_asiento.grid(row=7, column=3, columnspan=7, pady=10)
        self.boton_regresar.grid(row=7, column=5, columnspan=7, pady=10)

# Crear una instancia de la clase VentanaLogin y ejecutar el bucle principal
ventana = VentanaLogin()
ventana.mainloop()