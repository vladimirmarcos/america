import tkinter as tk
from client.gui_app import App
from models.general_dao import actualizar_intereses

def main():
    ventana = tk.Tk()
    ventana.geometry("1200x1200")
    App(ventana).pack(side="top", fill="both", expand=True)
    ventana.mainloop()


if __name__=='__main__':
    actualizar_intereses()
    main()