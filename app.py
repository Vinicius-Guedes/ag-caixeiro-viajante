import tkinter
import tkinter.messagebox as mb
import customtkinter
from caixeiroViajante import CaixeiroViajante


customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

class App(customtkinter.CTk):
    WIDTH = 1024
    HEIGHT = 640

    def __init__(self) -> None:
        super().__init__()

        self.title("Caixeiro Viajante")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.resizable(False, False)

        # ============ create two frames ============

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self,
                                                 width=180,
                                                 corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        self.frame_right = customtkinter.CTkFrame(master=self, corner_radius=0)
        self.frame_right.grid(row=0, column=1, sticky="nswe")
        # ============ frame_left ============

        self.frame_left.grid_rowconfigure(0, minsize=10)
        self.frame_left.grid_rowconfigure(7, weight=1)
        self.frame_left.grid_rowconfigure(8, minsize=20)
        self.frame_left.grid_rowconfigure(11, minsize=10)

        self.label_1 = customtkinter.CTkLabel(master=self.frame_left,
                                              text="Caixeiro Viajante",
                                              text_font=("Roboto Medium", -16))
        self.label_1.grid(row=1, column=0, pady=10, padx=10)

        self.entryCidades = customtkinter.CTkEntry(master=self.frame_left,
                                            width=140,
                                            placeholder_text="Qtde. de cidades")
        self.entryCidades.grid(row=2, column=0, pady=10, padx=20)

        self.entryCidadeInicial = customtkinter.CTkEntry(master=self.frame_left,
                                            width=140,
                                            placeholder_text="Ponto de partida")
        self.entryCidadeInicial.grid(row=3, column=0, pady=10, padx=20)

        self.entryPop = customtkinter.CTkEntry(master=self.frame_left,
                                            width=140,
                                            placeholder_text="Tamanho da população")
        self.entryPop.grid(row=4, column=0, pady=10, padx=20)

        self.entryGeracoes = customtkinter.CTkEntry(master=self.frame_left,
                                            width=140,
                                            placeholder_text="Qtde. Gerações")
        self.entryGeracoes.grid(row=5, column=0, pady=10, padx=20)

        self.btnRun = customtkinter.CTkButton(master=self.frame_left,
                                                text="Iniciar",
                                                width=140,
                                                command=self.button_event)
        self.btnRun.grid(row=6, column=0, pady=10, padx=20)

        self.label_mode = customtkinter.CTkLabel(master=self.frame_left, text="Appearance Mode:")
        self.label_mode.grid(row=9, column=0, pady=0, padx=20, sticky="w")

        self.optionmenu_1 = customtkinter.CTkOptionMenu(master=self.frame_left,
                                                        values=["Light", "Dark", "System"],
                                                        command=self.change_appearance_mode)
        self.optionmenu_1.grid(row=10, column=0, pady=10, padx=20, sticky="w")

        # ============ frame_right ============
        self.frame_right.rowconfigure((0, 1), weight=1)
        self.frame_right.columnconfigure(0, weight=1)
        self.frame_top = customtkinter.CTkFrame(self.frame_right)
        self.frame_top.grid(row=0, column=0, columnspan=3, sticky="nswe", pady=12, padx=8)
        self.frame_top.columnconfigure(0, weight=1)
        self.frame_botton = customtkinter.CTkFrame(self.frame_right)
        self.frame_botton.grid(row=1, column=0, columnspan=3, sticky="nswe", pady=12, padx=8)

        self.canvas = customtkinter.CTkCanvas(self.frame_top, height=384, width=384, bd=0,  bg="#ffffff")
        self.canvas.grid(row=0, column=0)
        self.canvas.pack()

        self.labelGeracao = customtkinter.CTkLabel(master=self.frame_botton,
                                              text="Gerações:",
                                              text_font=("Roboto Medium", -14))
        self.labelGeracao.grid(row=0, column=0, pady=10, padx=8, sticky="w")
        self.labelIndividuo = customtkinter.CTkLabel(master=self.frame_botton,
                                              text="Individuo:",
                                              text_font=("Roboto Medium", -14))
        self.labelIndividuo.grid(row=1, column=0, pady=10, padx=8, sticky="w")
        self.labelMenorDistancia = customtkinter.CTkLabel(master=self.frame_botton,
                                              text="Menor Distancia:",
                                              text_font=("Roboto Medium", -14))
        self.labelMenorDistancia.grid(row=2, column=0, pady=10, padx=8, sticky="w")

    def create_circle(self, x, y, r, canvas) -> None:
        x0 = x - r
        y0 = y - r
        x1 = x + r
        y1 = y + r
        canvas.create_oval(x0, y0, x1, y1, outline="#00F", fill="#00F")

    def desenhaCidade(self, cidades) -> None:
        margin = 42
        offset = 3
        pontos = list()
        for index, cidade in enumerate(cidades):
            pontos.append([ (cidade.pontoX * offset) + margin, (cidade.pontoY * offset) + margin ])
            for index2, cidade2 in enumerate(cidades):
                if not (cidade.pontoX == cidade2.pontoX and cidade.pontoY == cidade2.pontoY):
                    self.canvas.create_line(
                        (cidade.pontoX * offset) + margin,
                        (cidade.pontoY * offset) + margin,
                        (cidade2.pontoX * offset) + margin,
                        (cidade2.pontoY * offset) + margin
                    )
        for index, cords in enumerate(pontos):
            self.create_circle(cords[0], cords[1], 10, self.canvas)
            self.canvas.create_text(
                cords[0],
                cords[1],
                text=str(index), fill="#FFF", font=('Roboto 16')
            )

    def validarInput(self) -> bool:
        if self.entryCidades.get() == "" or self.entryPop.get() == "" or self.entryGeracoes.get() == "" or self.entryCidadeInicial.get() == "":
            return False
        
        try:
            int(self.entryCidades.get())
            int(self.entryCidadeInicial.get())
            int(self.entryPop.get())
            int(self.entryGeracoes.get())
            return True
        except:
            return False

    def button_event(self) -> None:
        self.labelGeracao.destroy()
        self.labelIndividuo.destroy()
        self.labelMenorDistancia.destroy()
        self.canvas.delete("all")

        if not self.validarInput():
            mb.showerror(title = "ERRO!", message = "Só são permitidos valores numericos e inteiros nos campos")
            return

        caixeiroViajante = CaixeiroViajante(
            int(self.entryCidades.get()),
            int(self.entryPop.get()),
            int(self.entryGeracoes.get()),
            int(self.entryCidadeInicial.get())
        )
        self.desenhaCidade(caixeiroViajante.getGeracaoCidades())
        resultado = caixeiroViajante.run(False)

        self.labelGeracao = customtkinter.CTkLabel(master=self.frame_botton,
                                              text="Gerações: " + str(resultado[0]),
                                              text_font=("Roboto Medium", -14))
        self.labelGeracao.grid(row=0, column=0, pady=10, padx=8, sticky="w")
        self.labelIndividuo = customtkinter.CTkLabel(master=self.frame_botton,
                                              text="Individuo: " + str(resultado[1]),
                                              text_font=("Roboto Medium", -14))
        self.labelIndividuo.grid(row=1, column=0, pady=10, padx=8, sticky="w")
        self.labelMenorDistancia = customtkinter.CTkLabel(master=self.frame_botton,
                                              text="Menor Distancia: " + str(resultado[2]),
                                              text_font=("Roboto Medium", -14))
        self.labelMenorDistancia.grid(row=2, column=0, pady=10, padx=8, sticky="w")

    def change_appearance_mode(self, new_appearance_mode) -> None:
        customtkinter.set_appearance_mode(new_appearance_mode)

    def on_closing(self, event=0) -> None:
        self.destroy()

if __name__ == "__main__":
    app = App()
    app.mainloop()
