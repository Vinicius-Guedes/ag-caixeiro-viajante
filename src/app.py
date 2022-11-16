import tkinter
import tkinter.messagebox
import customtkinter

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")


class App(customtkinter.CTk):
    WIDTH = 1024
    HEIGHT = 640

    def __init__(self):
        super().__init__()

        self.title("CustomTkinter complex_example.py")
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
        self.frame_left.grid_rowconfigure(6, weight=1)
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

        self.entryPop = customtkinter.CTkEntry(master=self.frame_left,
                                            width=140,
                                            placeholder_text="Tamanho da população")
        self.entryPop.grid(row=3, column=0, pady=10, padx=20)

        self.entryGeracoes = customtkinter.CTkEntry(master=self.frame_left,
                                            width=140,
                                            placeholder_text="Qtde. Gerações")
        self.entryGeracoes.grid(row=4, column=0, pady=10, padx=20)

        self.btnRun = customtkinter.CTkButton(master=self.frame_left,
                                                text="Iniciar",
                                                width=140,
                                                command=self.button_event)
        self.btnRun.grid(row=5, column=0, pady=10, padx=20)

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
        self.canvas.create_line(0,0,100,100)
        self.canvas.create_text(50, 50, text="1", fill="black", font=('Roboto 8'))
        self.canvas.pack()

        self.labelGeracao = customtkinter.CTkLabel(master=self.frame_botton,
                                              text="Geração:",
                                              text_font=("Roboto Medium", -14))
        self.labelGeracao.grid(row=0, column=0, pady=10, padx=8)
        self.labelIndividuo = customtkinter.CTkLabel(master=self.frame_botton,
                                              text="Individuo:",
                                              text_font=("Roboto Medium", -14))
        self.labelIndividuo.grid(row=1, column=0, pady=10, padx=8)
        self.labelMenorDistancia = customtkinter.CTkLabel(master=self.frame_botton,
                                              text="Menor Distancia:",
                                              text_font=("Roboto Medium", -14))
        self.labelMenorDistancia.grid(row=2, column=0, pady=10, padx=8)

    def button_event(self):
        print("Button pressed")

    def change_appearance_mode(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def on_closing(self, event=0):
        self.destroy()

if __name__ == "__main__":
    app = App()
    app.mainloop()
