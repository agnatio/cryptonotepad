import tkinter as tk
from tkinter import filedialog
import getpass
import encrypt


#Variable to store the current file path
current_file = ""
entered_pass = ""

def check_auth():
    global entered_pass
    global aes
    entered_pass = entry.get()
    aes = encrypt.AES256(bytes(entered_pass, 'utf-8'))
    key = 'gAAAAABjyajjzbJ0xnBc_SBueDZMH6jQN5Jg_GdzxIVOAfUoJDHXR48vl99d7mpHwHfWRGh0gwCXYPwK4jbp8XvksECztxujuQ=='
    try:
        
        if aes.decrypt(key.encode()).decode() == 'textToMatch':
            print("Success")
            auth_window.destroy()
    except:
        print("Incorrect password, closing program.")
        auth_window.destroy()
        exit()
    

def save_text_as():
    global current_file
    current_file = filedialog.asksaveasfilename(defaultextension=".txt")
    if current_file:
        with open(current_file, "w") as file:
            data = text_area.get("1.0", tk.END)
            data = aes.encrypt(data.encode()).decode()
            print(data)
            file.write(data)
    set_title()

def save_text():
    global current_file
    if current_file:
        with open(current_file, "w") as file:
            data = text_area.get("1.0", tk.END)
            data = aes.encrypt(data.encode()).decode()
            print(data)
            file.write(data)
    else:
        save_text_as()

def open_text():
    global current_file
    file = filedialog.askopenfile(mode='r') 
    if file:
        current_file = file.name
        data = file.read()
        data = aes.decrypt(data.encode()).decode()
        print(data)
        text_area.delete("1.0", tk.END)
        text_area.insert("1.0", data)
        file.close()
    set_title()

def set_title():
    if current_file:
        root.title("Simple Notepad - "+current_file)
    else:
        root.title("Simple Notepad")


def set_title():
    if current_file:
        root.title("Simple Notepad - "+current_file)
    else:
        root.title("Simple Notepad")

def exit_text():
    root.destroy()




# create a small window for authorization and place it in center of screen
auth_window = tk.Tk()
auth_window.title("Authorization")
auth_window.geometry("300x100")
auth_window.resizable(False, False)
auth_window.eval('tk::PlaceWindow %s center' % auth_window.winfo_pathname(auth_window.winfo_id()))

label = tk.Label(auth_window, text="Please enter the password:")
label.pack()

entry = tk.Entry(auth_window, show="*", width=20)
entry.pack()
entry.bind('<Return>', lambda event: check_auth())

button = tk.Button(auth_window, text="Submit", command=check_auth)
button.pack()

auth_window.mainloop()



root = tk.Tk()
root.title("Simple Notepad")

text_area = tk.Text(root, width=100, height=80)
text_area.pack()
# Create the menu
menubar = tk.Menu(root)
root.config(menu=menubar)

file_menu = tk.Menu(menubar)
menubar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=open_text)
file_menu.add_command(label="Save As", command=save_text_as)
file_menu.add_command(label="Save", command=save_text)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_text)

root.mainloop()














# import tkinter as tk
# from tkinter import filedialog

# root = tk.Tk()
# root.title("Simple Notepad")

# text_area = tk.Text(root, width=100, height=80)
# text_area.pack()



# def save_text():
#     file = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
#     if file:
#         data = text_area.get("1.0", tk.END)
#         file.write(data)
#         file.close()

# def open_text():
#     file = filedialog.askopenfile(mode='r', defaultextension=".txt")
#     if file:
#         data = file.read()
#         text_area.delete("1.0", tk.END)
#         text_area.insert("1.0", data)
#         file.close()

# def exit_text():
#     root.destroy()

# # Create the menu
# menubar = tk.Menu(root)
# root.config(menu=menubar)

# file_menu = tk.Menu(menubar)
# menubar.add_cascade(label="File", menu=file_menu)
# file_menu.add_command(label="Open", command=open_text)
# file_menu.add_command(label="Save", command=save_text)
# file_menu.add_separator()
# file_menu.add_command(label="Exit", command=exit_text)

# root.mainloop()

