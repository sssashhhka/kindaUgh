import customtkinter as ui


class SignInWindow(ui.CTk):
    def __init__(self):
        super().__init__()

        # Settings
        self.title("kindaUgh")
        self.geometry("400x600")
        # self.resizable(False, False)

        # Fonts
        button_f = ui.CTkFont("Inter", size=15)
        label_f = ui.CTkFont("Inter", weight="bold", size=40)

        # Widgets
        self.exit_b = ui.CTkButton(self, text="Exit", command=exit, corner_radius=0, height=50, font=button_f)
        self.label = ui.CTkLabel(self, text="Sign In", font=label_f)
        self.frame_a = ui.CTkFrame(self, corner_radius=10)
        self.usr_box = ui.CTkEntry(self.frame_a, placeholder_text="Username", font=button_f)
        self.pss_box = ui.CTkEntry(self.frame_a, placeholder_text="Password", font=button_f)
        self.sign_in_b = ui.CTkButton(self.frame_a, text="Sign In", font=button_f)
        self.sign_up_b = ui.CTkButton(self.frame_a, text="Sign Up", font=button_f)
        self.or_text = ui.CTkLabel(self.frame_a, text="or", font=button_f)
        self.console = ui.CTkTextbox(self, state="normal", activate_scrollbars=False, font=button_f,
                                     text_color="#999999")

        # Global grid config
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)

        # frame_a grid config
        self.frame_a.columnconfigure(1, weight=1)
        self.frame_a.rowconfigure(0, weight=1)
        self.frame_a.rowconfigure(1, weight=1)
        self.frame_a.rowconfigure(2, weight=1)

        # Widgets global placement
        self.label.grid(row=0, column=0, pady=(25, 0), sticky="news")
        self.frame_a.grid(row=1, column=0, padx=10, pady=10, sticky="news")
        self.console.grid(row=2, column=0, padx=10, pady=10, sticky="news")
        self.exit_b.grid(row=3, column=0, sticky="ews")

        # Widgets frame_a placement
        self.usr_box.grid(row=0, column=0, padx=7, pady=7, sticky="nsew", columnspan=3)
        self.pss_box.grid(row=1, column=0, padx=7, pady=7, sticky="nsew", columnspan=3)
        self.sign_up_b.grid(row=2, column=0, padx=(7, 3), pady=7, sticky="nsew")
        self.or_text.grid(row=2, column=1, padx=3, pady=7, sticky="nsew")
        self.sign_in_b.grid(row=2, column=2, padx=(3, 7), pady=7, sticky="nsew")

        # Other preferences
        self.console.insert("0.0", "Enter your username and password then press sign in or sign up")
        self.console.configure(state="disabled")


app = SignInWindow()
if __name__ == "__main__":
    app.mainloop()
