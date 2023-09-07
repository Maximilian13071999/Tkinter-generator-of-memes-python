from tkinter import *
from tkinter import filedialog as fd
from tkinter.ttk import *
from PIL import ImageTk, Image

root = Tk()
root.title("GeneratorOfMemes")
root.geometry('600x500')

label = Label(text="This is GeneratorOfMemes", foreground="yellow", background="black")
label.pack()

text_of_meme = Text(width=25, height=5, background="white", foreground="green", wrap=WORD)
text_of_meme.pack()

combobox_colors = Combobox(values=["yellow", "red", "gray"])
combobox_colors.pack()

def open_image():
    path = fd.askopenfilename()
    img = Image.open(path)
    img = img.resize((250, 250))
    img = ImageTk.PhotoImage(img)
    panel = Label(root, image=img)
    panel.image = img
    panel.place(relx=0.5, rely=0.6, anchor=CENTER)
    text_label = Label(text=text_of_meme.get("1.0", END), font="Times 30", foreground=combobox_colors.get())
    text_label.place(relx=0.5, rely=0.6, anchor=CENTER)

button_get_image = Button(text="Открыть фото", command=open_image)
button_get_image.pack()

root.mainloop()

