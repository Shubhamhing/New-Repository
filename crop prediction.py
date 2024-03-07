from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk

# List of background image file paths
image_paths = [
    "C:/Users/HP/Downloads/crop preditcton 1.jpg",
    "C:/Users/HP/Downloads/1119534.jpg",
    "C:/Users/HP/Downloads/pxfuel.jpg",
    "C:/Users/HP/Downloads/pxfuel (1).jpg",
    "C:/Users/HP/Downloads/pxfuel (2).jpg"
    
]

def update_background(index=0):
    # Open and resize the image
    image = Image.open(image_paths[index])
    image = image.resize((w, h), Image.ANTIALIAS)

    # Create a new PhotoImage object
    background_image = ImageTk.PhotoImage(image)

    # Update the background label
    background_label.configure(image=background_image)
    background_label.image = background_image

    # Schedule the next image update after a certain interval (in milliseconds)
    root.after(3000, lambda: update_background((index + 1) % len(image_paths)))

root = Tk()
root.geometry('500x500')
root.title("Crop Prediction using Machine Learning")
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))

# Create the initial background label
image2 = Image.open(image_paths[0])
image2 = image2.resize((w, h), Image.ANTIALIAS)
background_image = ImageTk.PhotoImage(image2)
background_label = tk.Label(root, image=background_image)
background_label.image = background_image
background_label.place(x=0, y=0)

# Start the background image slideshow
update_background()

frame = Frame(root, bg="white")
frame.place(x=0, y=0, height=80, width=1700)

label = Label(frame, text="CROP PREDICTION USING MACHINE LEARNING", font=("Bold", 30),bg="white", fg="black")
label.place(x=250, y=10)

frame = tk.Frame(root, bg="white")
frame.place(x=0, y=0, height=80, width=100)

# # Load the logo image
logo_image = Image.open("C:/Users/HP/Downloads/20650644.jpg")  
logo_photo = ImageTk.PhotoImage(logo_image)

# Create a label to display the logo image
logo_label = tk.Label(frame, image=logo_photo)
logo_label.image = logo_photo  # Keep a reference to prevent garbage collection
logo_label.place(x=0,y=0)

#conectivite 
def reg():
    from subprocess import call
    call(["python","cp.registration.py"])
    
def log():
    from subprocess import call
    call(["python","cp.login.py"])  
#ADD BUTTON
registration_button = tk.Button(root, text="Registration",command=reg,font=("bold", 15), bg="green", fg="black", padx=20, pady=10)
registration_button.place(x=500, y=400, height=35, width=120)

login_button = tk.Button(root, text="Login",command=log,font=("bold", 15), bg="green", fg="black", padx=20, pady=10)
login_button.place(x=660, y=400, height=35, width=120)

exit_button = tk.Button(root, text="Exit", font=("bold", 15), bg="red", fg="black", padx=20, pady=10,command=root.quit)
exit_button.place(x=570, y=470,height=35, width=120)

# home_button = tk.Button(root, text="Home",font=("bold", 15), bg="white", fg="black", padx=20, pady=10)
# home_button.place(x=1020, y=81, height=30, width=90)

# about_button = tk.Button(root, text="About",font=("bold", 15), bg="white", fg="black", padx=20, pady=10)
# about_button.place(x=1190, y=81, height=30, width=90)



root.mainloop()
