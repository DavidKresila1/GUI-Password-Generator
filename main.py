import tkinter as tk
import generatePassword
import pyperclip

passwordGenerator = generatePassword.passwordGenerator()

# window size
window = tk.Tk()
window.geometry("300x300")
window.maxsize(300, 300)
window.minsize(300, 300)



# window frame
def generatePasswordScreen():
    password = passwordGenerator.generator()
    label2 = tk.Label(window, text= f"Your new password is : \n {password}", state=tk.ACTIVE, font=("Arial", 17))
    label2.place(x=27, y=120)
    pyperclip.copy(password)

# window widget
label1 = tk.Label(window, text="Create your new password", font=("Arial", 17))
label1.pack()
label1.pack()
generatePasswordScreen()

window.mainloop()
