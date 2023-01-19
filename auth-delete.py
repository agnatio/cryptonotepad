import tkinter as tk


# write authorisation window with password entry

def check_auth():
    if entry.get() == "Secret":
        auth_window.destroy()
    else:
        label.config(text="Incorrect password, please try again:")

auth_window = tk.Tk()
auth_window.title("Authorization")
label = tk.Label(auth_window, text="Please enter the password:")
label.pack()
entry = tk.Entry(auth_window, show="*")
entry.pack()
button = tk.Button(auth_window, text="Submit", command=check_auth)
button.pack()
auth_window.mainloop()