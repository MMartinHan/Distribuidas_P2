import tkinter as tk
import pickle
import nomina_methods as nm
import contabilidad_methods as cm
import seleccion_methods as sm
from tkinter import ttk
from tkinter import messagebox
from funciones_ventanas import abrir_ventana, cerrar_ventana
import socket
import datetime

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
        self.geometry("1000x500")
        self.candidatos = []
        self.create_widgets()
        self.rellenar_tabla()

    def create_widgets(self):
        self.label_cedula = tk.Label(self.master, text="Cédula del candidato:")
        self.label_cedula.pack()
        self.entry_cedula = tk.Entry(self.master)
        self.entry_cedula.pack()

        self.label_nombre = tk.Label(self.master, text="Nombre del candidato:")
        self.label_nombre.pack()
        self.entry_nombre = tk.Entry(self.master)
        self.entry_nombre.pack()

        self.label_apellido = tk.Label(self.master, text="Apellido del candidato:")
        self.label_apellido.pack()
        self.entry_apellido = tk.Entry(self.master)
        self.entry_apellido.pack()

        self.label_fecha_nacimiento = tk.Label(self.master, text="Fecha de Nacimiento del candidato:")
        self.label_fecha_nacimiento.pack()
        self.entry_fecha_nacimiento = tk.Entry(self.master)
        self.entry_fecha_nacimiento.pack()

        self.btn_guardar_candidato = tk.Button(self.master, text="Guardar", command=self.guardar_candidato)
        self.btn_guardar_candidato.pack()

        self.label_candidatos_guardados = tk.Label(self.master, text="Candidatos Guardados:")
        self.label_candidatos_guardados.pack()

        self.treeview_candidatos = ttk.Treeview(self.master, columns=("cedula", "nombre", "apellido", "fechaNacimiento"), show="headings")
        self.treeview_candidatos.heading("cedula", text="Cedula")
        self.treeview_candidatos.heading("nombre", text="Nombre")
        self.treeview_candidatos.heading("apellido", text="Apellido")
        self.treeview_candidatos.heading("fechaNacimiento", text="Fecha nacimiento")
        self.treeview_candidatos.column("cedula", anchor=tk.CENTER)
        self.treeview_candidatos.column("nombre", anchor=tk.CENTER)
        self.treeview_candidatos.column("apellido", anchor=tk.CENTER)
        self.treeview_candidatos.column("fechaNacimiento", anchor=tk.CENTER)
        self.treeview_candidatos.pack()

        self.btn_modificar = tk.Button(self.master, text="Modificar", state=tk.DISABLED, command=self.modificar_candidato)
        self.btn_modificar.pack(side=tk.LEFT)

        self.btn_eliminar = tk.Button(self.master, text="Eliminar", state=tk.DISABLED, command=self.eliminar_candidato)
        self.btn_eliminar.pack(side=tk.LEFT)

        self.treeview_candidatos.bind("<<TreeviewSelect>>", self.actualizar_botones)

        self.btn_regresar = tk.Button(self.master, text="Regresar", command=self.mover_inicio)
        self.btn_regresar.pack(side=tk.RIGHT)

    def rellenar_tabla(self):
        mi_socket = crear_socket()
        consultaCandidatos = "CONSULTAR_CAN|CANDIDATO|*"
        mi_socket.send(consultaCandidatos.encode("utf-8"))
        self.treeview_candidatos.delete(*self.treeview_candidatos.get_children())
        data = b''
        data += mi_socket.recv(1024)
        print(data)
        data_decoded = pickle.loads(data)
        for candidato in data_decoded:
            self.treeview_candidatos.insert('', 'end', values=candidato)
        mi_socket.close()
        
    def mover_inicio(self):
        cerrar_ventana(self)
        abrir_ventana(VentanaSeleccion) 

    def guardar_candidato(self):
        cedula_candidato = self.entry_cedula.get()
        nombre_candidato = self.entry_nombre.get()
        apellido_candidato = self.entry_apellido.get()
        fechaNacimiento_candidato = self.entry_fecha_nacimiento.get()
        ingresoCandidato = "INGRESAR|CANDIDATO|(CEDULA_CAN,NOMBRE_CAN,APELLIDO_CAN,FECHANACIMIENTO_CAN)|"+str(cedula_candidato)+","+str(nombre_candidato)+","+str(apellido_candidato)+","+str(fechaNacimiento_candidato)
        mi_socket = crear_socket()
        mi_socket.send(ingresoCandidato.encode("utf-8"))
        respuesta = mi_socket.recv(1024)
        respuesta = respuesta.decode("utf-8")
        print(respuesta)
        mi_socket.close()
        
        self.entry_cedula.delete(0, 'end')  # Borrar contenido del campo de entrada
        self.entry_nombre.delete(0, 'end')
        self.entry_apellido.delete(0, 'end')
        self.entry_fecha_nacimiento.delete(0, 'end')
        self.rellenar_tabla()
        
        
    def modificar_candidato(self):
        seleccion = self.treeview_candidatos.selection()
        if seleccion:
            # Obtener los valores actuales del motivo seleccionado
            item = self.treeview_candidatos.item(seleccion)
            cedula_actual = item['values'][0]
            nuevo_nombre = self.entry_nombre.get()
            nuevo_apellido = self.entry_apellido.get()
            nuevo_fechaNacimiento = self.entry_fecha_nacimiento.get()
            modificarCandidato = "MODIFICAR_CAN|CANDIDATO|"+nuevo_nombre+"|"+nuevo_apellido+"|"+nuevo_fechaNacimiento+"|"+str(cedula_actual)
            mi_socket = crear_socket()
            mi_socket.send(modificarCandidato.encode("utf-8"))
            respuesta = mi_socket.recv(1024)
            respuesta = respuesta.decode("utf-8")    
            mi_socket.close()
            self.entry_cedula.delete(0, 'end')  # Borrar contenido del campo de entrada
            self.entry_nombre.delete(0, 'end')
            self.entry_apellido.delete(0, 'end')
            self.entry_fecha_nacimiento.delete(0, 'end')
            self.rellenar_tabla()

    def eliminar_candidato(self):
        seleccion = self.treeview_candidatos.selection()
        if seleccion:
            item = self.treeview_candidatos.item(seleccion)
            cedula_actual = item['values'][0]
            cedula_actual = str(cedula_actual)
            eliminarCandidato = "ELIMINAR_CAN|CANDIDATO|"+cedula_actual
            mi_socket = crear_socket()
            mi_socket.send(eliminarCandidato.encode("utf-8"))
            respuesta = mi_socket.recv(1024)
            respuesta = respuesta.decode("utf-8")    
            mi_socket.close()
            
            self.entry_cedula.delete(0, 'end')  # Borrar contenido del campo de entrada
            self.entry_nombre.delete(0, 'end')
            self.entry_apellido.delete(0, 'end')
            self.entry_fecha_nacimiento.delete(0, 'end')
            self.rellenar_tabla()
            
    def actualizar_botones(self, event):
        seleccion = self.treeview_candidatos.selection()

        if seleccion:
            self.btn_modificar.config(state=tk.NORMAL)
            self.btn_eliminar.config(state=tk.NORMAL)
            indice = seleccion[0]
            candidato = self.treeview_candidatos.item(indice)['values']
            print(candidato)
            self.entry_cedula.delete(0, tk.END)
            self.entry_cedula.insert(tk.END, candidato[0])
            self.entry_nombre.delete(0, tk.END)
            self.entry_nombre.insert(tk.END, candidato[1])
            self.entry_apellido.delete(0, tk.END)
            self.entry_apellido.insert(tk.END, candidato[2])
            self.entry_fecha_nacimiento.delete(0, tk.END)
            self.entry_fecha_nacimiento.insert(tk.END, candidato[3])
        else:
            self.btn_modificar.config(state=tk.DISABLED)
            self.btn_eliminar.config(state=tk.DISABLED) 

class VentanaAgregarParametro(tk.Tk):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.geometry("900x500")
        self.parametros = []
        self.create_widgets()
        self.rellenar_tabla()

    def create_widgets(self):
        self.label_candidato = tk.Label(self.master, text="Escoja al candidato")
        self.label_candidato.pack()
        op = self.rellenar_combobox()
        opcion_seleccionada = tk.StringVar()
        self.combo_candidato = ttk.Combobox(self.master, textvariable=opcion_seleccionada, values=op, state="readonly")
        self.combo_candidato.pack()
        
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

        self.treeview_parametros = ttk.Treeview(self.master, columns=("candidato", "codigo", "nombre", "puntaje"), show="headings")
        self.treeview_parametros.heading("candidato", text="Candidato")
        self.treeview_parametros.heading("codigo", text="Código")
        self.treeview_parametros.heading("nombre", text="Nombre")
        self.treeview_parametros.heading("puntaje", text="Puntaje")
        self.treeview_parametros.column("candidato", anchor=tk.CENTER)
        self.treeview_parametros.column("codigo", anchor=tk.CENTER)
        self.treeview_parametros.column("nombre", anchor=tk.CENTER)
        self.treeview_parametros.column("puntaje", anchor=tk.CENTER)
        self.treeview_parametros.pack()

        self.btn_modificar = tk.Button(self.master, text="Modificar", state=tk.DISABLED, command=self.modificar_parametro)
        self.btn_modificar.pack(side=tk.LEFT)

        self.btn_eliminar = tk.Button(self.master, text="Eliminar", state=tk.DISABLED, command=self.eliminar_parametro)
        self.btn_eliminar.pack(side=tk.LEFT)

        self.treeview_parametros.bind("<<TreeviewSelect>>", self.actualizar_botones)

        self.btn_regresar = tk.Button(self.master, text="Regresar", command=self.mover_inicio)
        self.btn_regresar.pack()

    def rellenar_combobox(self):
        opciones = sm.consultar_candidatos()
        return opciones
    
    def mover_inicio(self):
        cerrar_ventana(self)
        abrir_ventana(VentanaSeleccion)
    
    def rellenar_tabla(self):
        mi_socket = crear_socket()
        consultaParametros = "CONSULTAR_PARAMETRO|PARAMETROEVALUACION|*"
        mi_socket.send(consultaParametros.encode("utf-8"))
        self.treeview_parametros.delete(*self.treeview_parametros.get_children())
        data = b''
        data += mi_socket.recv(1024)
        print(data)
        data_decoded = pickle.loads(data)
        for motivo in data_decoded:
            self.treeview_parametros.insert('', 'end', values=motivo)
        mi_socket.close()

    def guardar_parametro(self):
        candidato = self.combo_candidato.get()
        nombre_parametro = self.entry_nombre_parametro.get()
        puntaje_maximo = self.entry_puntaje_maximo.get()
        id = sm.generar_id_parametroEvaluacion()
        ingresoParametro = "INGRESAR|PARAMETROEVALUACION|(CEDULA_CAN,CODIGO_PEV,NOMBRE_PEV,PUNTAJEMAXIMO_PEV)|"+ str(candidato) + ", " + id + ", "+ str(nombre_parametro) +", " + str(puntaje_maximo)
        print(ingresoParametro)
        mi_socket = crear_socket()
        mi_socket.send(ingresoParametro.encode("utf-8"))
        respuesta = mi_socket.recv(1024)
        respuesta = respuesta.decode("utf-8")
        print(respuesta)
        mi_socket.close()
        
        self.combo_candidato.set('')  # Borrar contenido del campo de entrada
        self.entry_nombre_parametro.delete(0, 'end')  
        self.entry_puntaje_maximo.delete(0, 'end')  
        self.rellenar_tabla()
        
        
    def modificar_parametro(self):
        seleccion = self.treeview_parametros.selection()

        if seleccion:
            # Obtener los valores actuales del motivo seleccionado
            item = self.treeview_parametros.item(seleccion)
            codigo_actual = item['values'][1]
            candidato_nuevo = self.combo_candidato.get()
            nombre_nuevo = self.entry_nombre_parametro.get()
            puntaje_nuevo = self.entry_puntaje_maximo.get()
            modificarParametro = "MODIFICAR_PARAMETRO|PARAMETROEVALUACION|"+str(candidato_nuevo)+"|"+nombre_nuevo+"|"+str(puntaje_nuevo)+"|"+str(codigo_actual)
            print(modificarParametro)
            mi_socket = crear_socket()
            mi_socket.send(modificarParametro.encode("utf-8"))
            respuesta = mi_socket.recv(1024)
            respuesta = respuesta.decode("utf-8")    
            mi_socket.close()
            self.combo_candidato.set('')  # Borrar contenido del campo de entrada
            self.entry_nombre_parametro.delete(0, 'end')  
            self.entry_puntaje_maximo.delete(0, 'end') 
            self.rellenar_tabla()
    
    def eliminar_parametro(self):
        seleccion = self.treeview_parametros.selection()
        if seleccion:
            item = self.treeview_parametros.item(seleccion)
            codigo_actual = item['values'][1]
            codigo_actual = str(codigo_actual)
            eliminarMotivo = "ELIMINAR|PARAMETROEVALUACION|CODIGO_PEV|"+codigo_actual
            mi_socket = crear_socket()
            mi_socket.send(eliminarMotivo.encode("utf-8"))
            respuesta = mi_socket.recv(1024)
            respuesta = respuesta.decode("utf-8")    
            mi_socket.close()
            self.combo_candidato.set('')  # Borrar contenido del campo de entrada
            self.entry_nombre_parametro.delete(0, 'end')  
            self.entry_puntaje_maximo.delete(0, 'end') 
            self.rellenar_tabla()
              
    def actualizar_botones(self, event):
        seleccion = self.treeview_parametros.selection()

        if seleccion:
            self.btn_modificar.config(state=tk.NORMAL)
            self.btn_eliminar.config(state=tk.NORMAL)
            indice = seleccion[0]
            parametro = self.treeview_parametros.item(indice)['values']
            print(parametro)
            self.combo_candidato.set('')
            self.combo_candidato.set(parametro[0])
            self.entry_nombre_parametro.delete(0, tk.END)
            self.entry_nombre_parametro.insert(tk.END, parametro[2])
            self.entry_puntaje_maximo.delete(0, tk.END)
            self.entry_puntaje_maximo.insert(tk.END, parametro[3])
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
        
        self.boton_opcion_8 = tk.Button(self.frame_contenedor, text="Detalle de nomina", command=self.verDetalleNomina)
        self.boton_opcion_8.pack(side="left", padx=10)
        self.boton_opcion_9 = tk.Button(self.frame_contenedor, text="Opciones de nomina", command=self.verOpcionesNomina)
        self.boton_opcion_9.pack(side="left", padx=10)
        
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
        
    def verDetalleNomina(self):
        cerrar_ventana(self)
        abrir_ventana(VentanaDetalleNomina)
        
    def verOpcionesNomina(self):
        cerrar_ventana(self)
        abrir_ventana(VentanaOpcionesNomina)
        
class VentanaDetalleNomina(tk.Tk):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.geometry("620x430")
        self.create_widgets()
        
    def create_widgets(self):
        self.label_codigo_nomina = tk.Label(self.master, text="Código de la nómina:")
        self.label_codigo_nomina.pack()
        self.label_id = tk.StringVar()
        self.entry_codigo_nomina = tk.Label(self.master,justify=tk.CENTER,textvariable=self.label_id)
        self.label_id.set(nm.generar_id_detalle())
        self.entry_codigo_nomina.pack()
        self.label_codigo_nomina.place(x=10, y=10)
        self.entry_codigo_nomina.place(x=130, y=10)
        
        self.label_fecha_nomina = tk.Label(self.master, text="Fecha del reporte:")
        self.label_fecha_nomina.pack()
        fecha_actual = datetime.date.today()
        fecha_actual_str = fecha_actual.strftime("%Y-%m-%d")
        self.label_fecha = tk.StringVar()
        self.entry_fecha_nomina = tk.Label(self.master, justify=tk.CENTER, textvariable=self.label_fecha)
        self.label_fecha.set(fecha_actual_str)
        self.entry_fecha_nomina.pack()
        self.label_fecha_nomina.place(x=10, y=40)
        self.entry_fecha_nomina.place(x=130, y=40)
        
        op = self.rellenar_combobox()
        opcion_seleccionada = tk.StringVar()
        self.label_combo = tk.Label(self.master, text="Seleccione el empleado:")
        self.combo_empleado = ttk.Combobox(self.master,textvariable=opcion_seleccionada, values=op, state="readonly")
        self.combo_empleado.pack()
        self.label_combo.pack()
        self.label_combo.place(x=10, y=70)
        self.combo_empleado.place(x=150, y=70)
        
        self.boton_buscar = tk.Button(self.master, text="Buscar", command=self.buscar_join)
        self.boton_buscar.pack()
        self.boton_buscar.place(x=350, y=70)
        
        self.label_datos = tk.Label(self.master, text="Datos del empleado:")
        self.entry_datos = tk.Label(self.master, text=' ')
        self.label_datos.pack()
        self.entry_datos.pack()
        self.label_datos.place(x=10, y=100)
        self.entry_datos.place(x=150, y=100)
        
        
        self.treeview_detalle = ttk.Treeview(self.master, columns=("motivo", "sueldo","observacion"), show="headings")
        self.treeview_detalle.heading("motivo", text="Motivo")
        self.treeview_detalle.heading("sueldo", text="Sueldo")
        self.treeview_detalle.heading("observacion", text="Observaciones")
        self.treeview_detalle.column("motivo", anchor=tk.CENTER)
        self.treeview_detalle.column("sueldo", anchor=tk.CENTER)
        self.treeview_detalle.column("observacion", anchor=tk.CENTER)
        self.treeview_detalle.pack()
        self.treeview_detalle.place(x=10, y=130)
        
        self.boton_guardar = tk.Button(self.master, text="Modificar reporte")
        self.boton_regresar = tk.Button(self.master, text="Regresar",command=self.regresar)
        self.boton_guardar.pack()
        self.boton_regresar.pack()
        self.boton_guardar.place(x=10, y=400)
        self.boton_regresar.place(x=560, y=400)
        
    def rellenar_combobox(self):
        opciones = nm.consultar_empleados()
        return opciones
    
    def regresar(self):
        cerrar_ventana(self)
        abrir_ventana(VentanaNomina)
    
    def buscar_join(self):
        mi_socket = crear_socket()
        constultaJoin = "JOIN|MOTIVO|EMPLEADO"
        mi_socket.send(constultaJoin.encode("utf-8"))
        self.treeview_detalle.delete(*self.treeview_detalle.get_children())
        data = b''
        data += mi_socket.recv(1024)
        print(data)
        data_decoded = pickle.loads(data)
        combo = self.combo_empleado.get()
        print(combo)
        print(combo[0])
        nuevo = combo.split(" ")
        print(nuevo[0])
        for i in range(len(data_decoded)):
            if nuevo[0] == str(data_decoded[i][2]):
                print("entro")
                self.entry_datos.config(text="Cedula: "+str(nuevo[0])+", Nombre: "+str(nuevo[1])+", Apellido: "+str(nuevo[2]))
                self.treeview_detalle.insert("", tk.END, values=(data_decoded[i][1], data_decoded[i][6], "Operacion realizada el: "+str(data_decoded[i][5])))
                self.combo_empleado.set("")
                item = self.treeview_detalle.get_children()
                for j in item:
                    print(self.treeview_detalle.item(j)["values"])
                    x = self.treeview_detalle.item(j)["values"]
                    print(data_decoded[i][0])
                    print(str(nuevo[0]))
                    print(str(self.label_id.get()))
                    print(x[2])
                    print(data_decoded[i][6])
                    ingresoReporte = "INGRESAR|NOMINA|(CODIGO_MOT,CEDULA_EMP,CODIGO_NOM,FECHA_NOM,DETALLE_NOM,SUELDO_EMP_NOM)|"+str(data_decoded[i][0])+","+str(nuevo[0])+","+str(self.label_id.get())+","+str(self.label_fecha.get())+","+str(x[2])+","+str(data_decoded[i][6])
                    print(ingresoReporte)
                    mi_socket = crear_socket()
                    mi_socket.send(ingresoReporte.encode("utf-8"))
                    respuesta = mi_socket.recv(1024)
                    respuesta = respuesta.decode("utf-8")
                    self.label_id.set("")
                    self.label_id.set(nm.generar_id_detalle())
                    print(respuesta)
                    mi_socket.close()
        
            
class VentanaOpcionesNomina(tk.Tk):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.geometry("1230x500")
        self.create_widgets() 
        self.rellenar_tabla()
        
    def create_widgets(self):
        self.label_motivo = tk.Label(self.master, text="Codigo del motivo:")  
        self.label_motivo.pack()
        self.label_motivo.place(x=10, y=10)
        
        self.text_motivo = tk.StringVar()
        self.label_motivo_2 = tk.Label(self.master, textvariable=self.text_motivo)
        self.label_motivo_2.pack()
        self.label_motivo_2.place(x=150, y=10)             
        
        self.label_cedula = tk.Label(self.master, text="Cedula del empleado:")  
        self.label_cedula.pack()
        self.label_cedula.place(x=10, y=40)
        
        self.text_cedula = tk.StringVar()
        self.label_cedula_2 = tk.Label(self.master, textvariable=self.text_cedula)
        self.label_cedula_2.pack()
        self.label_cedula_2.place(x=150, y=40)
        
        self.label_nomina = tk.Label(self.master, text="Codigo de la nomina:")  
        self.label_nomina.pack()
        self.label_nomina.place(x=10, y=70)
        
        self.text_nomina = tk.StringVar()
        self.label_nomina_2 = tk.Label(self.master, textvariable=self.text_nomina)
        self.label_nomina_2.pack()
        self.label_nomina_2.place(x=150, y=70)
        
        self.label_fecha = tk.Label(self.master, text="Fecha del reporte:")  
        self.label_fecha.pack()
        self.label_fecha.place(x=10, y=100)
        
        self.entry_fecha = tk.Entry(self.master,state=tk.DISABLED)
        self.entry_fecha.pack()
        self.entry_fecha.place(x=150, y=100)
        
        self.label_detalle = tk.Label(self.master, text="Detalle del reporte:")  
        self.label_detalle.pack()
        self.label_detalle.place(x=10, y=130)
        
        self.entry_detalle = tk.Entry(self.master,width=50,state=tk.DISABLED)
        self.entry_detalle.pack()
        self.entry_detalle.place(x=150, y=130)
        
        self.label_valor = tk.Label(self.master, text="Valor en USD:")  
        self.label_valor.pack()
        self.label_valor.place(x=10, y=160)
        
        self.entry_valor = tk.Entry(self.master,state=tk.DISABLED)
        self.entry_valor.pack()
        self.entry_valor.place(x=150, y=160)
        
        self.treeview_reporte = ttk.Treeview(self.master, columns=("codigo", "cedula", "nomina", "fecha", "detalle", "valor"), show="headings")
        self.treeview_reporte.heading("codigo", text="Codigo del Motivo")
        self.treeview_reporte.heading("cedula", text="Cedula del Empleado")
        self.treeview_reporte.heading("nomina", text="Codigo del reporte de Nomina")
        self.treeview_reporte.heading("fecha", text="Fecha del reporte")
        self.treeview_reporte.heading("detalle", text="Detalle del reporte")
        self.treeview_reporte.heading("valor", text="Valor en USD")
        self.treeview_reporte.column("codigo",anchor=tk.CENTER)
        self.treeview_reporte.column("cedula",anchor=tk.CENTER)
        self.treeview_reporte.column("nomina",anchor=tk.CENTER)
        self.treeview_reporte.column("fecha",anchor=tk.CENTER)
        self.treeview_reporte.column("detalle",anchor=tk.CENTER)
        self.treeview_reporte.column("valor",anchor=tk.CENTER)
        self.treeview_reporte.pack()
        self.treeview_reporte.bind("<<TreeviewSelect>>", self.actualizar_botones)
        self.treeview_reporte.place(x=10, y=190)
        
        self.boton_modificar = tk.Button(self.master, text="Modificar", state=tk.DISABLED, command=self.modificar_reporte)
        self.boton_modificar.pack()
        self.boton_modificar.place(x=10, y=450)
        
        self.boton_eliminar = tk.Button(self.master, text="Eliminar", state=tk.DISABLED, command=self.eliminar_reporte)
        self.boton_eliminar.pack()
        self.boton_eliminar.place(x=100, y=450)
        
        self.boton_regresar = tk.Button(self.master, text="Regresar", command=self.regresar)
        self.boton_regresar.pack()
        self.boton_regresar.place(x=190, y=450)
        
    def regresar(self):
        cerrar_ventana(self)
        abrir_ventana(VentanaNomina)
        
    def rellenar_tabla(self):
        mi_socket = crear_socket()
        datosReporte = "CONSULTA_REPORTE|NOMINA"
        mi_socket.send(datosReporte.encode("utf-8"))
        self.treeview_reporte.delete(*self.treeview_reporte.get_children())
        data = b''
        data += mi_socket.recv(1024)
        print(data)
        data_decoded = pickle.loads(data)
        for motivo in data_decoded:
            self.treeview_reporte.insert('', 'end', values=motivo)
        mi_socket.close()
         
    def actualizar_botones(self, event):
        seleccion = self.treeview_reporte.selection()

        if seleccion:
            self.boton_modificar.config(state=tk.NORMAL)
            self.boton_eliminar.config(state=tk.NORMAL)
            indice = seleccion[0]
            reportes = self.treeview_reporte.item(indice)['values']  
            self.text_motivo.set(reportes[0]) 
            self.text_cedula.set(reportes[1])
            self.text_nomina.set(reportes[2])
            self.entry_fecha.delete(0, tk.END)
            self.entry_fecha.config(state=tk.NORMAL)
            self.entry_fecha.insert(0, reportes[3])
            self.entry_detalle.delete(0, tk.END)
            self.entry_detalle.config(state=tk.NORMAL)
            self.entry_detalle.insert(0, reportes[4])
            self.entry_valor.delete(0, tk.END)
            self.entry_valor.config(state=tk.NORMAL)
            self.entry_valor.insert(0, reportes[5]) 
        else:
            self.boton_modificar.config(state=tk.DISABLED)
            self.boton_eliminar.config(state=tk.DISABLED)

    def modificar_reporte(self):
        seleccion = self.treeview_reporte.selection()
        if seleccion:
            # Obtener los valores actuales del motivo seleccionado
            item = self.treeview_reporte.item(seleccion)
            codigo_nom_actual = item['values'][2]
            fecha_nueva = self.entry_fecha.get()
            detalle_nuevo = self.entry_detalle.get()
            valor_nuevo = self.entry_valor.get()
            modificarReporte = "MODIFICAR_REPORTE|NOMINA|"+str(fecha_nueva)+"|"+str(detalle_nuevo)+"|"+str(valor_nuevo)+"|"+str(codigo_nom_actual)
            print(modificarReporte)
            mi_socket = crear_socket()
            mi_socket.send(modificarReporte.encode("utf-8"))
            respuesta = mi_socket.recv(1024)
            respuesta = respuesta.decode("utf-8")    
            mi_socket.close()
            self.text_motivo.set("")
            self.text_cedula.set("")
            self.text_nomina.set("")
            self.entry_fecha.delete(0, tk.END)
            self.entry_fecha.config(state=tk.DISABLED)
            self.entry_detalle.delete(0, tk.END)
            self.entry_detalle.config(state=tk.DISABLED)
            self.entry_valor.delete(0, tk.END)
            self.entry_valor.config(state=tk.DISABLED)
            self.rellenar_tabla()
            
    def eliminar_reporte(self):
        seleccion = self.treeview_reporte.selection()
        if seleccion:
            # Obtener los valores actuales del motivo seleccionado
            item = self.treeview_reporte.item(seleccion)
            codigo_nom_actual = item['values'][2]
            fecha_nueva = self.entry_fecha.get()
            detalle_nuevo = self.entry_detalle.get()
            valor_nuevo = self.entry_valor.get()
            modificarReporte = "ELIMINAR|NOMINA|CODIGO_NOM|"+str(codigo_nom_actual)
            print(modificarReporte)
            mi_socket = crear_socket()
            mi_socket.send(modificarReporte.encode("utf-8"))
            respuesta = mi_socket.recv(1024)
            respuesta = respuesta.decode("utf-8")    
            mi_socket.close()
            self.text_motivo.set("")
            self.text_cedula.set("")
            self.text_nomina.set("")
            self.entry_fecha.delete(0, tk.END)
            self.entry_fecha.config(state=tk.DISABLED)
            self.entry_detalle.delete(0, tk.END)
            self.entry_detalle.config(state=tk.DISABLED)
            self.entry_valor.delete(0, tk.END)
            self.entry_valor.config(state=tk.DISABLED)
            self.rellenar_tabla()
            
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
        self.treeview_motivos.column("codigo", anchor=tk.CENTER)
        self.treeview_motivos.column("nombre", anchor=tk.CENTER)
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
            codigo_actual = str(codigo_actual)
            nuevo_nombre = self.entry_nombre_motivo.get()
            modificarMotivo = "MODIFICAR|MOTIVO|"+nuevo_nombre+"|"+codigo_actual
            mi_socket = crear_socket()
            mi_socket.send(modificarMotivo.encode("utf-8"))
            respuesta = mi_socket.recv(1024)
            respuesta = respuesta.decode("utf-8")    
            mi_socket.close()
            self.entry_nombre_motivo.delete(0, 'end')
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
            self.entry_nombre_motivo.delete(0, 'end')
            self.rellenar_tabla()

    def actualizar_botones(self, event):
        seleccion = self.treeview_motivos.selection()

        if seleccion:
            self.btn_modificar.config(state=tk.NORMAL)
            self.btn_eliminar.config(state=tk.NORMAL)
            self.entry_nombre_motivo.delete(0, 'end')  # Borrar contenido del campo de entrada
            self.entry_nombre_motivo.insert(0, self.treeview_motivos.item(seleccion)['values'][1])
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
        
        self.label_motivo = tk.Label(self.master, text="Escoja el motivo")
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
        ingresarEmpleado = "INGRESAR|EMPLEADO|(CODIGO_MOT, CEDULA_EMP, NOMBRE_EMP, APELLIDO_EMP, FECHA_ING_EMP, SUELDO_EMP)|"+ str(codico_mot[0]) + "," + str(cedula) + "," + str(nombre)+ ","+ str(apellido) + "," + str(fecha) + "," + str(sueldo)
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
        if nombre_cuenta and tipo_cuenta:
            self.cuentas.append((nombre_cuenta, tipo_cuenta))
            cuenta_text = f"{nombre_cuenta} - {tipo_cuenta}"
            self.treeview_cuentas.insert("", tk.END, values=(nombre_cuenta, tipo_cuenta))
            self.entry_nombre_cuenta.delete(0, tk.END)
            messagebox.showinfo("Información", "Cuenta guardada exitosamente.")
        else:
            messagebox.showwarning("Advertencia", "Ingrese un nombre de cuenta y seleccione un tipo de cuenta.")

    def modificar_cuenta(self):
        seleccion = self.treeview_cuentas.selection()

        if seleccion:
            item = self.treeview_cuentas.item(seleccion)
            codigo_tipo_cuenta = item["values"][0]
            codigo_cuenta = item["values"][1]
            nombre_cuenta = item["values"][2]

            self.entry_nombre_cuenta.delete(0, tk.END)
            self.entry_nombre_cuenta.insert(tk.END, nombre_cuenta)

            # Seleccionar el tipo de cuenta correspondiente en el combobox
            for index, opcion in enumerate(self.combobox_tipo_cuenta["values"]):
                if opcion.startswith(codigo_tipo_cuenta):
                    self.combobox_tipo_cuenta.current(index)
                    break

            self.btn_modificar.config(state=tk.NORMAL)
            self.btn_eliminar.config(state=tk.NORMAL)
        else:
            self.entry_nombre_cuenta.delete(0, tk.END)
            self.combobox_tipo_cuenta.current(0)
            self.btn_modificar.config(state=tk.DISABLED)
            self.btn_eliminar.config(state=tk.DISABLED)
    
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
        seleccion = self.treeview_cuentas.selection()

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