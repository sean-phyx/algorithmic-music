import tkinter
import tkinter.ttk
import tkinter.messagebox
import customtkinter

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window

        iconIm = tkinter.PhotoImage(file = "C:\\Users\\armat\\Documents\\algorithmic-music\\algorithmic-music\\src\\music-analyser-app\\music_analyser_app\\build\\assets\\frame0\\app_icon.png")
        self.iconphoto(False, iconIm)
        self.title("Music Analyser")
        self.geometry(f"{1100}x{580}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)

if __name__ == "__main__":
    app = App()
    app.mainloop()