from PIL import Image
import customtkinter as ctk

class Function:
    '''
    A class to store universally used functions

    methods:
        displayImage(self, frame, image_path, size=(100, 100), position=(0.5, 0.2)): Displays an image on the provided frame.
    '''
    def displayImage(self, frame, image_path, size=(100, 100), position=(0.5, 0.2)):
        '''
        Displays an image on the provided frame.

        Args:
            frame (CTkFrame): The frame on which to display the image.
            image_path (str): Path to the image file.
            size (tuple): Size to which the image should be resized (width, height).
            position (tuple): Relative position to place the image (relx, rely).
        '''
        img = Image.open(image_path)
        img = img.resize(size, Image.LANCZOS)
        self.image_tk = ctk.CTkImage(dark_image=img, size=size)


        # label to display img
        img_label = ctk.CTkLabel(
            master=frame,
            image=self.image_tk,
            text=""
        )

        img_label.configure(width=size[0], height=size[1])

        img_label.place(relx=position[0], rely=position[1], anchor="center")