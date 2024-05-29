import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk  # Necesitarás instalar Pillow
from Backend.AnalizaLexico import AnalizadorLexico
import os

class AplicacionPrincipal(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Analizador Léxico GUI")
        self.master.geometry("600x500")
        self.master.iconphoto(False, tk.PhotoImage(file=r'C:\Users\cromi\Downloads\clipart2531021.png'))
        self.pack(fill=tk.BOTH, expand=True)
        self.crear_widgets()
        self.analizador = AnalizadorLexico()

    def crear_widgets(self):
        # Configuración del Canvas para la imagen de fondo
        self.canvas = tk.Canvas(self, width=600, height=600)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Ruta de la imagen descargada de Internet
        ruta_imagen = r"C:\Users\cromi\Downloads\ADELAIDA ANETTE (adelaidaanette) on Pinterest.jpg"

        if not os.path.exists(ruta_imagen):
            print(f"La ruta {ruta_imagen} no existe. Verifica la ruta.")
            return

        # Cargar la imagen de fondo
        self.imagen_fondo = Image.open(ruta_imagen)
        self.imagen_fondo = self.imagen_fondo.resize((600, 350), Image.Resampling.LANCZOS)
        self.imagen_fondo = ImageTk.PhotoImage(self.imagen_fondo)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.imagen_fondo)

        # Configuración del área de texto
        self.area_texto = tk.Text(self, wrap=tk.WORD, height=10, font=("Helvetica", 12), bg="#87CEEB", bd=2, relief=tk.SUNKEN)
        self.canvas.create_window(10, 10, anchor=tk.NW, window=self.area_texto, width=580)

        # Configuración del botón para leer archivo
        self.boton_leer_archivo = tk.Button(self, text="Insertar archivo .txt", command=self.leer_archivo, bg="#0000ff", fg="white", font=("Helvetica", 12, "bold"), bd=2, relief=tk.RAISED)
        self.canvas.create_window(10, 215, anchor=tk.NW, window=self.boton_leer_archivo, width=200)

        # Configuración del botón de analizar
        self.boton_analizar = tk.Button(self, text="Analizar", command=self.analizar_codigo, bg="#0000ff", fg="white", font=("Helvetica", 12, "bold"), bd=2, relief=tk.RAISED)
        self.canvas.create_window(10, 255, anchor=tk.NW, window=self.boton_analizar, width=200)

        # Configuración de la tabla de tokens
        estilo = ttk.Style()
        estilo.theme_use('default')
        estilo.configure("Treeview.Heading", font=("Helvetica", 12, "bold"), background="#0000ff", foreground="white")  # Cambia el color de fondo y las letras de las cabeceras
        estilo.configure("Treeview", font=("Helvetica", 10), rowheight=25)
        estilo.map('Treeview', background=[('selected', '#007BFF')], foreground=[('selected', 'white')])

        self.tabla_tokens = ttk.Treeview(self, columns=('Categoria', 'Lexema', 'Posicion'), show='headings')
        self.tabla_tokens.heading('Categoria', text='Categoría', anchor=tk.CENTER)
        self.tabla_tokens.heading('Lexema', text='Lexema', anchor=tk.CENTER)
        self.tabla_tokens.heading('Posicion', text='Posición', anchor=tk.CENTER)
        self.tabla_tokens.column('Categoria', anchor=tk.CENTER, width=100)
        self.tabla_tokens.column('Lexema', anchor=tk.CENTER, width=200)
        self.tabla_tokens.column('Posicion', anchor=tk.CENTER, width=100)
        self.canvas.create_window(10, 300, anchor=tk.NW, window=self.tabla_tokens, width=580, height=150)  # Ajusta el tamaño de la tabla

    def leer_archivo(self):
        archivo = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if archivo:
            with open(archivo, 'r', encoding='utf-8') as file:
                contenido = file.read()
                self.area_texto.delete("1.0", tk.END)
                self.area_texto.insert(tk.END, contenido)

    def analizar_codigo(self):
        codigo = self.area_texto.get("1.0", "end-1c")
        tokens = self.analizador.tokenizar(codigo)
        for i in self.tabla_tokens.get_children():
            self.tabla_tokens.delete(i)
        for token in tokens:
            categoria, lexema, linea, columna = token
            posicion = f'{linea}:{columna}'
            self.tabla_tokens.insert('', 'end', values=(categoria, lexema, posicion))

def main():
    root = tk.Tk()
    app = AplicacionPrincipal(master=root)
    app.mainloop()

if __name__ == '__main__':
    main()
