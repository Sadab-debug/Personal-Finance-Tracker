import customtkinter as ctk
from settings import Settings
from utils.button import Button
from utils.frame import Frame
from function import Function
from firebase import FireBase

ctk.set_default_color_theme("blue")

class Main(ctk.CTk):
    '''
    A class to manage overall actions of software

    attributes:
        settings(Settings): stores Settings class and all components of it
        signup_frame(Frame): creates a frame for signup
        gmail_entry(ctkEntry): creates an entry box for gmail
        password_entry(ctkEntry): create an entry box for password
        signup_btn(Button): creates a button for signup

    mehtods:
        __init__(self): initializes all the components of app
        signupFrame(self): creates a frame for signup
        setUpSignupWidgets(self): sets up all the widgets inside the SignupFrame
    '''
    def __init__(self):
        super().__init__()
        self.settings = Settings()
        self.func = Function()
        self.firebase_db = FireBase()

        self.email = self.gmail_entry.get()
        self.password = self.password_entry.get()

        # Deactivate automatic DPI awareness for manual control over scaling
        ctk.deactivate_automatic_dpi_awareness()

        # Set scaling factors to make the app responsive
        ctk.set_widget_scaling(1.2)   # Scale widgets and text size by 120%
        ctk.set_window_scaling(1.1)   # Scale the entire window size by 110%

        # initialize window
        self.geometry(f"{self.settings.WIDTH}x{self.settings.HEIGHT}")
        self.title(self.settings.CAPTION)
        self.configure(fg_color=self.settings.bg_color)
        

        # login frame
        self.signupFrame()

        # FIXME: gmail_entry not found

    def signupFrame(self):
        '''creates a frame for login'''
        self.signup_frame = Frame(
            master=self,
            width=800,
            height=600,
            x=0.5,
            y=0.5,
            anchor='center',
        )

        # display login icon
        self.func.displayImage(
            frame=self.signup_frame.getFrame(),
            image_path="images/login_icon.png",
            size=(100,100),
            position=(0.5, 0.2)
        )
        self.setupSignupWidgets()
        self.firebase_db.login(email=self.email, password=self.password)

    def setupSignupWidgets(self):
        '''sets up all the widgets inside the loginFrame'''

        # entry box for gmail
        self.gmail_entry = ctk.CTkEntry(
            master=self.signup_frame.getFrame(),
            width=500,
            height=48,
            corner_radius=20,
            border_width=3,
            border_color=self.settings.secondary_accent,
            fg_color="transparent",
            placeholder_text="Enter gmail",
            placeholder_text_color=self.settings.subtle_txt
        )
        self.gmail_entry.place(relx=0.5, rely=0.4, anchor='center')

        # entry box for password
        self.password_entry = ctk.CTkEntry(
            master=self.signup_frame.getFrame(),
            width=500,
            height=48,
            corner_radius=20,
            border_width=3,
            border_color=self.settings.secondary_accent,
            fg_color="transparent",
            placeholder_text="Create a strong password",
            placeholder_text_color=self.settings.subtle_txt
        )
        self.password_entry.place(relx=0.5, rely=0.5, anchor='center')

        # button for signup
        self.signup_btn = Button(
            master=self.signup_frame.getFrame(),
            txt="Signup",
            x=0.3,
            y=0.6,
        )

        # button for login
        self.login_btn = Button(
            master=self.signup_frame.getFrame(),
            txt="Login",
            x=0.5,
            y=0.6,
        )




if __name__ == "__main__":
    app = Main()
    app.mainloop()