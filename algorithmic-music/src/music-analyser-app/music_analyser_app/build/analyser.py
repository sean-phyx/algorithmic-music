import tkinter
import tkinter.ttk
import tkinter.messagebox
from tkinter.filedialog import askopenfile, askdirectory
import customtkinter
from translations import translations
from debug.appdebugger import AppDebugger
import os

basedir = os.path.dirname(__file__)

try:
    from ctypes import windll  # Only exists on Windows.

    myappid = "mycompany.myproduct.subproduct.version"
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
except ImportError:
    pass

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
# customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"
selectedlanguage = translations.eng

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.debugger = AppDebugger.instance()
        self.debugger.log('initialising app gui')

        # configure window
        iconIm = tkinter.PhotoImage(file = 'algorithmic-music/src/music-analyser-app/music_analyser_app/build/assets/frame0/app_icon.png')
        self.iconphoto(False, iconIm)
        self.title("Music Analyser")
        self.geometry(f"{1100}x{580}")
        self.option_add('*tearOff', False)

        # configure grid layout (4x13)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure(tuple(range(0, 13)), weight=1)

        # create sidebar frame
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0, fg_color=('#E4E4E4', '#313231'))
        self.sidebar_frame.grid(row=0, column=0, rowspan=11, sticky='nsew')
        self.sidebar_frame.grid_rowconfigure(4, weight=1)

        # create the playback bar (bottom menu)
        self.playback_bar_frame = customtkinter.CTkFrame(self, height=10, corner_radius=0, fg_color=('#D2D2D2', '#4D5153'))
        self.playback_bar_frame.grid(row=11, column=0, rowspan=2, columnspan=4, stick='nsew')

        # create the main display frame (front and center app focus)
        self.main_app_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color=('#FFFFFF', '#2B2B2B'))
        self.main_app_frame.grid(row=0, column=1, rowspan=11, columnspan=3, sticky='nsew')
        self.main_app_frame.rowconfigure(tuple(range(0,10)), weight=1)
        self.main_app_frame.columnconfigure(tuple(range(0,10)), weight=1)

        # create the main view tabs (tabview)
        self.main_tab_view = customtkinter.CTkTabview(self.main_app_frame, fg_color=('#FFFFFF', '#000000'))
        self.main_tab_view.grid(row=0, column=0, padx=(10, 0), pady=(0, 0), rowspan=9, columnspan=10, sticky="nsew")
        self.main_tab_view.add(getlang('main_view_media'))
        self.main_tab_view.add(getlang('main_view_edit'))
        self.main_tab_view.add(getlang('main_view_settings'))

        # configure the individual view grids
        self.main_tab_view.tab(getlang('main_view_media')).grid_columnconfigure(tuple(range(0,10)), weight=1)
        self.main_tab_view.tab(getlang('main_view_media')).grid_rowconfigure(tuple(range(0,15)), weight=1)

        self.main_tab_view.tab(getlang('main_view_edit')).grid_columnconfigure(0, weight=1)

        self.label_tab_2 = customtkinter.CTkLabel(self.main_tab_view.tab(getlang('main_view_edit')), text="CTkLabel on Tab 2")
        self.label_tab_2.grid(row=0, column=0, padx=20, pady=20)

        # create the upload section in the media view
        self.sidebar_upload_frame = customtkinter.CTkFrame(self.main_tab_view.tab(getlang('main_view_media')), fg_color=('#FFFFFF', '#171717'), corner_radius=3)
        self.sidebar_upload_frame.grid(row=15, column=10, padx=0, pady=0)
        self.sidebar_upload_frame.grid_rowconfigure((0,1), weight=1)

        self.sidebar_upload_button = customtkinter.CTkButton(self.sidebar_upload_frame, command=self.open_file, text=getlang('file_upload_button'), corner_radius=3)
        self.sidebar_upload_button.grid(row=0, column=0, padx=10, pady=5)

        self.sidebar_folder_button = customtkinter.CTkButton(self.sidebar_upload_frame, command=self.open_folder, text=getlang('file_folder_button'), corner_radius=3)
        self.sidebar_folder_button.grid(row=1, column=0, padx=10, pady=5)

        # create the buttons to perform functions in the sidebar
        self.sidebar_menu_frame = customtkinter.CTkFrame(self.sidebar_frame, fg_color='#171717')
        self.sidebar_menu_frame.grid(row=2, column=0, padx=10, pady=5)


        # create the generate chroma button in the sidebar
        # TODO UI TWEAK
        # grey out the button when a file is not selected || Move to the correct page.
        self.sidebar_generate_chroma_buton = customtkinter.CTkButton(self.sidebar_menu_frame, command=self.generate_chroma, text=getlang('generate_chroma_button'))
        self.sidebar_generate_chroma_buton.grid(row=1, column=0, padx=10, pady=5)

        # create the application scaling and mode selections
        self.sidebar_appearance_frame = customtkinter.CTkFrame(self.sidebar_frame, fg_color=('#FFFFFF', '#171717'), corner_radius=3)
        self.sidebar_appearance_frame.grid(row=13, column=0, padx=10, pady=5)
        self.sidebar_appearance_frame.grid_rowconfigure(1, weight=1)

        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_appearance_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_appearance_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_appearance_frame, text='UI Scaling:', anchor='w')
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_appearance_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))


        # set the default
        self.appearance_mode_optionemenu.set("Dark")
        self.scaling_optionemenu.set("100%")

    # method to open a file
    def open_file(self):
        file_path = askopenfile(mode = 'r', filetypes=[('MP3 Files', '*mp3')])
        if file_path is None:
            return
        file_name = file_path.name.split('/')
        file_name = file_name[-1]
        self.sidebar_upload_text.configure(text=file_name)

    def open_folder(self):
        folder_path = askdirectory(initialdir='~/Music')
        for item in os.listdir(folder_path):
            # TODO grab individual files and load them.
            return

    def generate_chroma(self):
        return NotImplemented

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)



def getlang(texttoget):
    try:
        if (not selectedlanguage.get(texttoget) == None):
            return selectedlanguage.get(texttoget)
        debug = AppDebugger.instance()
        debug.error(f'Language has no translation for {texttoget}')
        return translations.eng.get(texttoget)
    except Exception as err:
        # TODO ERROR REPORTING 
        # with the ErrorReporter.
        debug = AppDebugger.instance()
        debug.error(err)
        
if __name__ == "__main__":
    app = App()
    app.mainloop()