import customtkinter as ctk
from settings import Settings

class Button:
    '''
    A class to manage overall behaviour of all buttons

    attributes:
        settings(Settings): inherits all the properties of Settings class
        button(ctkButton): creates and manages the button

    methods:
        __init__(self, master, txt, x, y, anchor=None): initializes the button
    '''
    def __init__(self, master, txt, x, y, anchor=None):
        '''
        creates and manages the button

        Args:
            master(tk.Tk): The main window or parent widget
            txt(str): The text for displaying on the button
            x(relx): locate anchor of this widget between 0.0 and 1.0 relative to width of master (1.0 is right edge)
            y(rely): locate anchor of this widget between 0.0 and 1.0 relative to height of master (1.0 is bottom edge)
            anchor(NSEW): position anchor according to given direction
        '''
        self.settings = Settings()
        self.button = ctk.CTkButton(
            master=master,
            width=150,
            height=40,
            corner_radius=20,
            text=txt,
            fg_color=self.settings.primary_accent,
            text_color=self.settings.txt_color,
        )
        self.button.place(relx=x, rely=y, anchor=anchor)
        