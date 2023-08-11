import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import main

width = 400
height = 250

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Filename Changer")
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        center_x = int(screen_width/2 - width / 2)
        center_y = int(screen_height/2 - height / 2)
        self.geometry(f'{width}x{height}+{center_x}+{center_y}')
        self.resizable(False, False)
        self.iconbitmap(r'static\favicon.ico')

        self.create_widgets()

    def choose_drt(self, btn):
        directory = filedialog.askdirectory()
        if directory:
            btn.delete(0, tk.END)  # Clear the entry field
            btn.insert(0, directory)

    def change_name(self, name, path, name_ety, path_ety):
        try:
            main.name_changer(name, path)
            messagebox.showinfo("Success", "Success! Name has been changed.")
            name_ety.delete(0, tk.END)
            path_ety.delete(0, tk.END)

        except:
            messagebox.showerror("Error! Something went wrong.")    

    def create_widgets(self):
        drt = ttk.Label(self, text="Select Directory:")
        drt.pack(padx=10, pady=5, anchor=tk.NW)

        frm = ttk.Frame(self)
        frm.columnconfigure(0, weight=3)
        frm.columnconfigure(1, weight=1)
        frm.pack()

        frame1 = tk.Frame(self, width=400)
        frame1.pack(padx=10)

        drt_value = tk.StringVar()
        drt_entry = ttk.Entry(frame1, textvariable=drt_value, width=50)
        drt_entry.pack(side=tk.LEFT)

        drt_btn = ttk.Button(frame1, text="select", command=lambda: self.choose_drt(btn=drt_entry))
        drt_btn.pack(side=tk.LEFT)

        name = ttk.Label(self, text="Enter Name:")
        name.pack(padx=10, pady=10, anchor=tk.NW)

        name_value = tk.StringVar()
        name_entry = ttk.Entry(self, textvariable=name_value)
        name_entry.pack(padx=10, fill=tk.X, anchor=tk.NW)

        done_btn = ttk.Button(self, text="change", command=lambda: self.change_name(name_value.get(), drt_value.get(), name_entry, drt_entry), cursor="hand2")
        done_btn.pack(pady=20, ipadx=20)

        

if __name__ == '__main__':
    app = App()
    app.mainloop()