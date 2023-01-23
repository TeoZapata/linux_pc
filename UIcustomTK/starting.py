import customtkinter as ctk


ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("green")


root = ctk.CTk()
root.geometry("500x500")

def login():
    print("text")

frame = ctk.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both",expand=True)

label = ctk.CTkLabel(master=frame, text="login System")

label.pack(pady=12,padx=10)

entry1= ctk.CTkEntry(master=frame, placeholder_text="Username")
entry1.pack(pady=12, padx=10)

entry2= ctk.CTkEntry(master=frame, placeholder_text="Password",show="*")
entry2.pack(pady=12, padx=10)

botton= ctk.CTkButton(master=frame, text="Login", command=login)
botton.pack(pady=12, padx=10)




root.mainloop()