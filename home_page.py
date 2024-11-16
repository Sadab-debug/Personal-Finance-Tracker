import customtkinter as ctk
from settings import Settings

class Home(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.settings = Settings()

        # Deactivate automatic DPI awareness for manual control over scaling
        ctk.deactivate_automatic_dpi_awareness()

        # Set scaling factors to make the app responsive
        ctk.set_widget_scaling(1.2)   # Scale widgets and text size by 120%
        ctk.set_window_scaling(1.1)   # Scale the entire window size by 110%

        # initialize window
        self.geometry(f"{self.settings.WIDTH}x{self.settings.HEIGHT}")
        self.title(self.settings.CAPTION)
        self.configure(fg_color=self.settings.bg_color)

        self.button = ctk.CTkButton(self, text="Logged in succesfully", command=self.button_callbck, fg_color=self.settings.primary_accent, text_color=self.settings.txt_color)
        self.button.pack(padx=20, pady=20)

    def button_callbck(self):
        print("button clicked")

if __name__ == "__main__":
    app = Home()
    app.mainloop()