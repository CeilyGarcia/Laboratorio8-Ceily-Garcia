import serial
import time
from matplotlib import image
from tkinter import *

ser = serial.Serial('COM4', 9600, timeout=1)

calor = 25
def imagen():
    root = Tk()
    root.title("¡¡¡¡EMERGENCIA, FUEGO!!!!")
    root.geometry("500x500")
    imagen = PhotoImage(file =r'C:\Users\Ceily\Desktop\UMG\5 semestre\tareas\programacion 3\Laboratorio 8\grito.png' )
    fondo = Label(root,image=imagen).place(x = 0,y = 0)
    Button(root, text="AYUDAAAAAAAAA FUEGOOOOOOOOOOO", command=root.destroy).pack()
    root.mainloop()

    root2 = Tk()
    root2.title("¡¡¡¡EMERGENCIA, FUEGO!!!!")
    root2.geometry("500x500")
    imagen1 = PhotoImage(file =r'C:\Users\Ceily\Desktop\UMG\5 semestre\tareas\programacion 3\Laboratorio 8\alarma2.png' )
    fondo1 = Label(root2,image=imagen1).place(x = 0,y = 0)
    Button(root2, text="Llamar a los bomberos", command=root2.destroy).pack()
    root2.mainloop()

    root3 = Tk()
    root3.title("¡¡¡¡EMERGENCIA, FUEGO!!!!")
    root3.geometry("500x500")
    imagen1 = PhotoImage(file =r'C:\Users\Ceily\Desktop\UMG\5 semestre\tareas\programacion 3\Laboratorio 8\bomberos.png' )
    fondo1 = Label(root3,image=imagen1).place(x = 0,y = 0)
    Button(root3, text="Apagar el fuego", command=root3.destroy).pack()
    root3.mainloop()

    root4 = Tk()
    root4.title("¡¡¡¡EMERGENCIA, FUEGO!!!!")
    root4.geometry("500x500")
    imagen1 = PhotoImage(file =r'C:\Users\Ceily\Desktop\UMG\5 semestre\tareas\programacion 3\Laboratorio 8\final.png' )
    fondo1 = Label(root4,image=imagen1).place(x = 0,y = 0)
    Button(root4, text="Fuego controlado, FIN", command=root4.destroy).pack()
    root4.mainloop()

while True:
    data = ser.readline().decode().strip()
    time.sleep(1)

    if data:
        data = float(data)
        print(data)
        if data >= calor:
            print(imagen())