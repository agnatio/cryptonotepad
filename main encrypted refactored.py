import tkinter as tk
from tkinter import filedialog
import encrypt
import authentication

class Notepad:
    def __init__(self):
        self.current_file = ""
        self.aes = None
        self.root = tk.Tk()
        self.root.geometry("+600+200")
        self.root.title("Simple Notepad")

        self.text_area = tk.Text(self.root, width=100, height=40)
        self.text_area.pack()
        self.menubar = tk.Menu(self.root)
        self.root.config(menu=self.menubar)

        self.file_menu = tk.Menu(self.menubar)
        self.menubar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Open", command=self.open_text)
        self.file_menu.add_command(label="Save", command=self.save_text)
        self.file_menu.add_command(label="Save As", command=self.save_text_as)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.exit_text)

        self.authenticate()
        self.root.mainloop()
        
    def authenticate(self):
        password = authentication.get_password()
        self.aes = encrypt.AES256(password)
        
    def open_text(self):
        file_path = filedialog.askopenfile(mode='r')
        if file_path:
            self.current_file = file_path.name
            data = file_path.read()
            data = self.handle_crypto(data, "decrypt")
            self.text_area.delete("1.0", tk.END)
            self.text_area.insert("1.0", data)
            file_path.close()
        self.set_title()

    def save_text(self):
        if self.current_file:
            self.handle_file_operation(self.current_file, "save")
        else:
            self.save_text_as()

    def save_text_as(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt")
        if file_path:
            self.current_file = file_path
            self.handle_file_operation(file_path, "save")
        self.set_title()

    def handle_file_operation(self, file_path, mode):
        with open(file_path, mode) as file:
            data = self.text_area.get("1.0", tk.END)
            data = self.handle_crypto(data, mode)
            file.write(data)

    def handle_crypto(self, data, mode):
        try:
            if mode == "encrypt":
                print("Saving with encryption")
                data = self.aes.encrypt(data.encode()).decode()
            else:
                print("Opening with decryption")
                data = self.aes.decrypt(data.encode()).decode()
        except:
            print(f"{mode.capitalize()} without encryption")
            pass
        return data
    
    def set_title(self):
        if self.current_file:
            self.root.title("Simple Notepad - " + self.current_file)
        else:
            self.root.title("Simple Notepad")

    def exit_text(self):
        self.root.destroy()

if __name__ == '__main__':
    Notepad()