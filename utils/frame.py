import customtkinter as ctk
from settings import Settings

class Frame:
    '''
    A class to manage overall behaviour of all frames

    attributes:
        settings(Settings): inherits all the properties of Settings class
        frame(ctkFrame): creates and manages the frame

    methods:
        __init__(self, master, width, height, x, y, anchor=None): initializes the frame
        getFrame(self): returns the Ctk object of frame
    '''
    def __init__(self, master, width, height, x, y, anchor=None):
        '''
        creates and manages the frame

        Args:
            master(tk.Tk): The main window or parent widget
            width(int): The width of the frame in pixel
            height(int): The height of the frame in pixel
            x(relx): locate anchor of this widget between 0.0 and 1.0 relative to width of master (1.0 is right edge)
            y(rely): locate anchor of this widget between 0.0 and 1.0 relative to height of master (1.0 is bottom edge)
            anchor(NSEW): position anchor according to given direction
        '''
        self.settings = Settings()
        self.frame = ctk.CTkFrame(
            master=master,
            width=width,
            height=height,
            corner_radius=20,
            fg_color=self.settings.frame_color,
            border_width=3,
            border_color=self.settings.secondary_accent,
        )
        self.frame.place(relx=x, rely=y, anchor=anchor)

    def getFrame(self):
        return self.frame