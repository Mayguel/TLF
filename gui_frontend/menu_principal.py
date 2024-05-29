import tkinter as tk
from tkinter import filedialog
from main_gui import AplicacionPrincipal
from PIL import Image, ImageTk  # Necesitarás instalar Pillow
import os

class MenuPrincipal(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Menú Principal")
        self.master.geometry("400x300")
        self.master.iconphoto(False, tk.PhotoImage(file=r'C:\Users\cromi\Downloads\clipart2531021.png'))
        self.pack(fill=tk.BOTH, expand=True)
        self.crear_widgets()

    def crear_widgets(self):
        # Configuración del Canvas para la imagen de fondo
        self.canvas = tk.Canvas(self, width=400, height=300)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Ruta de la imagen descargada de Internet
        ruta_imagen = r"C:\Users\cromi\Downloads\c-baymax.jpg"

        if not os.path.exists(ruta_imagen):
            print(f"La ruta {ruta_imagen} no existe. Verifica la ruta.")
            return

        # Cargar la imagen de fondo
        self.imagen_fondo = Image.open(ruta_imagen)
        self.imagen_fondo = self.imagen_fondo.resize((400, 300), Image.Resampling.LANCZOS)
        self.imagen_fondo = ImageTk.PhotoImage(self.imagen_fondo)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.imagen_fondo)

        # Configuración del botón para abrir el Analizador Léxico
        self.boton_analizador = tk.Button(self, text="Analizador Léxico", command=self.abrir_analizador, bg="#000000", fg="white", font=("Comic Sans MS", 14, "bold"), bd=3, relief=tk.RAISED)
        self.canvas.create_window(200, 130, anchor=tk.CENTER, window=self.boton_analizador, width=200)

        # Configuración del botón para abrir Automatas
        self.boton_automatas = tk.Button(self, text="Automatas", command=self.abrir_automatas, bg="#000000", fg="white", font=("Comic Sans MS", 14, "bold"), bd=3, relief=tk.RAISED)
        self.canvas.create_window(200, 220, anchor=tk.CENTER, window=self.boton_automatas, width=200)

    def abrir_analizador(self):
        self.master.withdraw()
        nueva_ventana = tk.Toplevel(self.master)
        app = AplicacionPrincipal(master=nueva_ventana)

    def abrir_automatas(self):
        self.master.withdraw()
        nueva_ventana = tk.Toplevel(self.master)
        app = AutomataGUI(master=nueva_ventana)

class AutomataGUI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Automata Generator")
        self.master.geometry("600x500")
        self.pack(fill=tk.BOTH, expand=True)
        self.crear_widgets()
        self.generador_automata = AutomataGenerator()

    def crear_widgets(self):
        # Configuración del área de texto para la expresión regular
        self.area_texto = tk.Text(self, wrap=tk.WORD, height=2, font=("Helvetica", 12), bg="#F0F0F0", bd=2, relief=tk.SUNKEN)
        self.area_texto.pack(pady=10, padx=10, fill=tk.X)

        # Configuración del botón de generar autómata
        self.boton_generar = tk.Button(self, text="Generar Autómata", command=self.generar_automata, bg="#0000ff", fg="white", font=("Helvetica", 12, "bold"), bd=2, relief=tk.RAISED)
        self.boton_generar.pack(pady=10)

        # Área de texto para mostrar el autómata generado
        self.area_resultado = tk.Text(self, wrap=tk.WORD, height=20, font=("Helvetica", 12), bg="#F0F0F0", bd=2, relief=tk.SUNKEN)
        self.area_resultado.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

    def generar_automata(self):
        expresion_regular = self.area_texto.get("1.0", "end-1c")
        automata = self.generador_automata.generar_automata(expresion_regular)
        self.area_resultado.delete("1.0", tk.END)
        self.area_resultado.insert(tk.END, automata)

class AutomataGenerator:
    def __init__(self):
        self.automatas = []

    def generar_automata(self, expresion_regular):
        # Aquí va la lógica para convertir la expresión regular en un autómata
        # Esta es una implementación simplificada.
        automata = f"Autómata generado para: {expresion_regular}"
        self.automatas.append(automata)
        return automata

def main():
    root = tk.Tk()
    app = MenuPrincipal(master=root)
    app.mainloop()

if __name__ == '__main__':
    main()
