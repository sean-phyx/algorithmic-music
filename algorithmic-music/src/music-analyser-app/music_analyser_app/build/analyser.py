import tkinter
import tkinter.ttk
import tkinter.messagebox
from tkinter.filedialog import askopenfile 
import customtkinter
from translations import translations

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"
selectedlanguage = translations.eng

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        iconIm = tkinter.PhotoImage(file = "C:\\Users\\armat\\Documents\\algorithmic-music\\algorithmic-music\\src\\music-analyser-app\\music_analyser_app\\build\\assets\\frame0\\app_icon.png")
        self.iconphoto(False, iconIm)
        self.title("Music Analyser")
        self.geometry(f"{1100}x{580}")
        self.option_add('*tearOff', False)

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)

        # create the upload section
        self.sidebar_upload_frame = customtkinter.CTkFrame(self.sidebar_frame, fg_color='#171717')
        self.sidebar_upload_frame.grid(row=1, column=0, padx=10, pady=5)

        self.sidebar_upload_button = customtkinter.CTkButton(self.sidebar_upload_frame, command=self.open_file, text=getlang('file_upload_button'))
        self.sidebar_upload_button.grid(row=1, column=0, padx=10, pady=5)
        self.sidebar_upload_text = customtkinter.CTkLabel(self.sidebar_upload_frame, text=getlang('no_upload_text'))
        self.sidebar_upload_text.grid(row=2, column=0, padx=10, pady=5)

        # create the buttons to perform functions in the sidebar
        self.sidebar_menu_frame = customtkinter.CTkFrame(self.sidebar_frame, fg_color='#171717')
        self.sidebar_menu_frame.grid(row=2, column=0, padx=10, pady=5)

        self.sidebar_generate_chroma_buton = customtkinter.CTkButton(self.sidebar_menu_frame, command=self.generate_chroma, text=getlang('generate_chroma_button'))
        self.sidebar_generate_chroma_buton.grid(row=1, column=0, padx=10, pady=5)

    # method to open a file
    def open_file(self):
        file_path = askopenfile(mode = 'r', filetypes=[('MP3 Files', '*mp3')])
        if file_path is None:
            return
        file_name = file_path.name.split('/')
        file_name = file_name[-1]
        self.sidebar_upload_text.configure(text=file_name)

    def generate_chroma(self):
        return NotImplemented



def getlang(texttoget):
    try:
        return selectedlanguage.get(texttoget)
    except:
        # TODO PASS OUT AN ERROR with the ErrorReporter.
        return
        
if __name__ == "__main__":
    app = App()
    app.mainloop()