import tkinter as tk
from tkinter import messagebox, font

def login():
        messagebox.showinfo("Login Successful", "Welcome!")

def forgot_password():
    messagebox.showinfo("Forgot Password", "Password reset instructions have been sent to your email.")

root = tk.Tk()
root.title("MECE")
root.geometry("400x500")

modern_font = font.Font(family="Helvetica", size=12)
modern_font_big = font.Font(family="Helvetica", size=24)

college_Name = tk.Label(root, text="Welcome to MRCE", font=modern_font_big)
college_Name.pack(pady=10)

label_name = tk.Label(root, text="name:", font=modern_font)
label_name.pack(pady=10)
entry_name = tk.Entry(root, font=modern_font)
entry_name.pack()

label_email = tk.Label(root, text="email:", font=modern_font)
label_email.pack(pady=10)
entry_email = tk.Entry(root, font=modern_font)
entry_email.pack()

label_username = tk.Label(root, text="Username:", font=modern_font)
label_username.pack(pady=10)
entry_username = tk.Entry(root, font=modern_font)
entry_username.pack()

label_password = tk.Label(root, text="Password:", font=modern_font)
label_password.pack(pady=10)
entry_password = tk.Entry(root, show="*", font=modern_font)
entry_password.pack()

login_button = tk.Button(root, text="Login", command=login, bg="light blue", font=modern_font)
login_button.pack(pady=20)

forgot_password_link = tk.Label(root, text="Forgot Password?", fg="blue", cursor="hand2", font=modern_font)
forgot_password_link.pack()
forgot_password_link.bind("<Button-1>", lambda e: forgot_password())

root.mainloop()
