import tkinter as tk
from tkinter import ttk, filedialog
from Backend.AppAutomatas import AppAutomatas
import os

class AplicacionAutomatas(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Generador de Autómatas")
        self.master.geometry("600x500")
        self.pack(fill=tk.BOTH, expand=True)
        self.crear_widgets()
        self.generador = AppAutomatas()

    def crear_widgets(self):
        # Configuración del área de texto
        self.area_texto = tk.Text(self, wrap=tk.WORD, height=10, font=("Helvetica", 12), bg="#F0F0F0", bd=2, relief=tk.SUNKEN)
        self.area_texto.pack(padx=10, pady=10, fill=tk.X)

        # Configuración del botón para generar autómata
        self.boton_generar = tk.Button(self, text="Generar Autómata", command=self.generar_automata, bg="#0000ff", fg="white", font=("Helvetica", 12, "bold"), bd=2, relief=tk.RAISED)
        self.boton_generar.pack(pady=10)

        # Área de texto para mostrar el autómata
        self.resultado = tk.Text(self, wrap=tk.WORD, height=15, font=("Helvetica", 12), bg="#F0F0F0", bd=2, relief=tk.SUNKEN)
        self.resultado.pack(padx=10, pady=10, fill=tk.X)

    def generar_automata(self):
        expresion_regular = self.area_texto.get("1.0", "end-1c")
        automata = self.generador.generar_automata(expresion_regular)
        self.resultado.delete("1.0", tk.END)
        self.resultado.insert(tk.END, automata)
