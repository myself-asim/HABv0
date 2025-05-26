import time
import tkinter
import customtkinter

customtkinter.set_appearance_mode('DARK')

app = customtkinter.CTk()
app.geometry('700x400')
app.minsize(700, 400)
app.maxsize(700, 400)

ConnectText = customtkinter.StringVar(app, '')

def Connecting():
    if username.get() == 'RootX' and password.get() == 'IamRootX(::)':
        time.sleep(0.3)
        ConnectText.set('SuccessFully LoggedIn')

    else:
        ConnectText.set('UserName Or PassWord Is Wrong')

Frame = customtkinter.CTkFrame(app, fg_color='black')
Frame.pack(fill='both', expand=True)

Label = customtkinter.CTkLabel(Frame, text='LOGIN INTO \n HETEROGENOUS AUTOMATED BLOCKv0\n(HABv0)')
Label.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)

ConnectLabel = customtkinter.CTkLabel(Frame, textvariable=ConnectText)
ConnectLabel.place(relx=0.5, rely=0.9, anchor=tkinter.CENTER)

username = customtkinter.CTkEntry(Frame, 250, 25, placeholder_text='UserName',fg_color='black', text_color='white', border_width=0)
username.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)

userline = customtkinter.CTkLabel(Frame, text='─' * 35, text_color='white', font=('Arial', 10))
userline.place(relx=0.5, rely=0.45, anchor=tkinter.CENTER)


password = customtkinter.CTkEntry(Frame, 250, 25, placeholder_text='PassWord', show='*',fg_color='black', text_color='white', border_width=0)
password.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)

passline = customtkinter.CTkLabel(Frame, text='─' * 35, text_color='white', font=('Arial', 10))
passline.place(relx=0.5, rely=0.65, anchor=tkinter.CENTER)

Button = customtkinter.CTkButton(master=app, text='Submit', width=250, height=25, fg_color='white', text_color='black', command=Connecting, hover_color='Grey', bg_color='transparent', corner_radius=0)
Button.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)

app.mainloop()