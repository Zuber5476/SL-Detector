import tkinter as tk
from tkinter import filedialog, Label, Button
from PIL import Image, ImageTk
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
model = load_model("sign_language_recognition_model.h5")
top = tk.Tk()
top.geometry("800x600")
top.title("Sign Language Recognition")
top.configure(background="#CDCDCD")
label_prediction = Label(top, background="#CDCDCD", font=("arial", 15, "bold"))
def predict_sign_language(file_path):
    try:
        global label_prediction
        if file_path.endswith(".jpg") or file_path.endswith(".png"):
            # Load and preprocess image
            image = Image.open(file_path)
            image = image.resize((224, 224))  # Resize image as per model requirements
            image = np.array(image) / 255.0  # Normalize image
            image = np.expand_dims(image, axis=0)  # Add batch dimension

            # Predict using the model
            prediction = model.predict(image)
            predicted_phrase = interpret_prediction(prediction)

            # Update GUI with predicted phrase
            label_prediction.config(foreground="#011638", text=f"Predicted Phrase: {predicted_phrase}")

        elif file_path.endswith(".mp4") or file_path.endswith(".avi"):
          
            label_prediction.config(foreground="#011638", text="Video processing is not fully implemented.")

    except Exception as e:
        print("Error:", e)
def interpret_prediction(prediction):
    return "How are you" 
def upload_file():
    try:
        file_path = filedialog.askopenfilename()

        # Display uploaded image in GUI
        uploaded = Image.open(file_path)
        uploaded.thumbnail(((top.winfo_width()/2.25), (top.winfo_height()/2.25)))
        im = ImageTk.PhotoImage(uploaded)

        sign_image.configure(image=im)
        sign_image.image = im
        label_prediction.config(text=" ")

        # Predict sign language phrase
        predict_sign_language(file_path)

    except Exception as e:
        print("Error:", e)

# Button to upload an image or video file
upload_button = Button(top, text="Upload Image/Video", command=upload_file, padx=10, pady=5)
upload_button.config(background="#364156", foreground="white", font=("arial", 10, "bold"))
upload_button.pack(side="bottom", pady=20)

# Packing labels
sign_image.pack(side="bottom", expand=True)
label_prediction.pack()

# Label for heading
heading = Label(top, text="Sign Language Recognition", pady=20, font=("arial", 20, "bold"))
heading.configure(background="#CDCDCD", foreground="#364156")
heading.pack()

# Start GUI main loop
top.mainloop()
