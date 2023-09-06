import tkinter as tk
from client.gui_app import App

def main():
    ventana = tk.Tk()
    ventana.geometry("1200x1200")
    App(ventana).pack(side="top", fill="both", expand=True)
    ventana.mainloop()


if __name__=='__main__':
   
    main()