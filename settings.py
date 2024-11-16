class Settings:
    '''A class to manage overall settings of the app'''
    def __init__(self):
        self.WIDTH = "1280"
        self.HEIGHT = "720"
        self.CAPTION = "Personal Finance Tracker"
        self.bg_color = "#FFFFFF"
        self.primary_accent =  "#FF6B35"   # Buttons, Icons
        self.secondary_accent = "#FFA559"   # Highlights, Borders
        self.txt_color = "#2E2E2E"
        self.subtle_txt = "#757575"
        self.font = "Poppins"
        self.font_size = 14
        self.frame_color = "#F3F5F6"

        # Define a custom color theme
        self.color_theme = {
            "bg_color": self.bg_color,           # Background color
            "primary_accent": self.primary_accent,     # Button color
            "secondary_accent": self.secondary_accent, # Highlights, Borders
            "text": self.txt_color,
            "subtle_txt": self.subtle_txt
        }