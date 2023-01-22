import tkinter as tk
import getpass
import encrypt

def get_password():
    # create a  window for authorization and place it in center of screen
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
    return entry.get()

def check_auth():
    entered_pass = entry.get()
    try:
        if encrypt.AES256(bytes(entered_pass, 'utf-8')).decrypt(authorisation.key.encode()).decode() == 'textToMatch':
            print("Successful authentication")
            auth_window.destroy()
    except:
        print("Incorrect password, closing program.")
        auth_window.destroy()
        exit()
