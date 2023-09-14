from tkinter import *
import random
import string
def generator():
    password_length = int(length_entry.get())
    
    if password_length < 4:
        password_label.config(text="PASSWORD LENGTH MUST BE ATLEAST 4 CHARACTERS")
        return
    
    password_strength = choice.get()
    if password_strength == 1:
        characters = string.ascii_letters + string.digits
    elif password_strength == 2:
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        characters = string.ascii_letters + string.digits + string.punctuation + string.ascii_letters.upper()

    generated_password = ''.join(random.choice(characters) for _ in range(password_length))
    password_label.config(text="Generated Password: " + generated_password)
Font="Ariel",20,"bold"
gui = Tk()
gui.configure(bg="black")
gui.title("RANDOM PASSWORD GENERATOR")
length_label = Label(gui, text="Password Length",font=Font,fg="white",bg="black")
length_label.grid(pady=5) 
length_entry = Entry(gui,width=20)
length_entry.grid(pady=5)
strength_label = Label(gui, text="Password Strength",font=Font,fg="white",bg="black")
strength_label.grid(pady=5)
choice = StringVar()
choice.set(1) 
weakradiobutton = Radiobutton(gui, text="Low", variable=choice, value=1,font=Font,bg="green")
weakradiobutton.grid(pady=5)
mediumradiobutton = Radiobutton(gui, text="Medium", variable=choice, value=2,font=Font,bg="blue")
mediumradiobutton.grid(pady=5)
strongradiobutton = Radiobutton(gui, text="STRONG", variable=choice, value=3,font=Font,bg="red")
strongradiobutton.grid(pady=5)
generate_button = Button(gui, text="Generate Password", command=generator,font=Font,bg="orange")
generate_button.grid(pady=5)
password_label = Label(gui, text="",font=Font,bg="black",fg="white")
password_label.grid(pady=5)
gui.mainloop()