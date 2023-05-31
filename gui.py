# -*- coding: utf-8 -*-

import tkinter as tk
import subprocess

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        
        self.output_text = tk.Text(self.master, height=20, width=50)
        self.output_text.pack()
        self.message_label = tk.Label(self.master, text="Welcome to the Body Measurement Model \n Press Run to Execute Program", font=("Times New Roman", 12), fg="black", bg="white")
        self.message_label.place(relx=0.5, rely=0.7, anchor="center")
        self.output_text.configure(font=("Verdana", 9), fg="darkgreen")

       # self.message_label = tk.Label(self.master, text="Press the Run button to Execute the Program.", font=("Times New Roman", 12), fg="blue", bg="white")
        #self.message_label.place(relx=0.5, rely=0.9, anchor="center")
        self.message_label.pack()
        self.run_button = tk.Button(self.master, text=" Run ", padx=10, pady=3, width=10, height=2, relief="raised", command=self.run_model)
        self.run_button.pack()

    def run_model(self):
        self.output_text.delete('1.0', tk.END) # clear previous output
        process = subprocess.Popen(['python', 'C:/Users/Dhriti/OneDrive/Desktop/bmi/Body_Measurement_Model.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        while True:
            output = process.stdout.readline().decode()
            if output == '' and process.poll() is not None:
                break
            if output:
                self.output_text.insert(tk.END, output)

        process.communicate() # wait for the process to terminate

root = tk.Tk()
root.title("Body Measurement")
root.geometry("1860x700")

canvas = tk.Canvas(root, width=250, height=200)
canvas.pack()

# Load the image
image = tk.PhotoImage(file="C:/Users/Dhriti/OneDrive/Desktop/bmi/images-min.png")

# Get the dimensions of the image
image_width = image.width()
image_height = image.height()

# set the background color of the frame to white
root.configure(background='white')


# Place the image in the center of the canvas
canvas.create_image(120, 100, image=image)

app = Application(master=root)
app.mainloop()
