
def abrir_ventana(ventna_cls):
    ventana = ventna_cls()
    ventana.mainloop()
    
def cerrar_ventana(ventana):
    ventana.destroy()