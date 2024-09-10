# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 14:18:09 2024

@author: klot_pa
"""
import os
import random
from flask import Flask, render_template, request

app = Flask(__name__)

# Function to get all image files for a given letter
def get_images_for_letter(letter):
    # Assuming the images are stored in 'static/images'
    image_folder = f"./static/images"
    # List all files in the folder and filter the ones that match the pattern for the letter
    images = [f for f in os.listdir(image_folder) if f.startswith(letter) and f.endswith('.png')]
    return images

# Route for the homepage
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name").lower()  # Get the name input and convert it to lowercase
        images = []

        # Loop through each letter in the name and randomly pick an image
        for letter in name:
            if letter.isalpha():  # Check if the character is a letter
                available_images = get_images_for_letter(letter)
                if available_images:  # If there are images for this letter
                    random_image = random.choice(available_images)  # Randomly pick an image
                    images.append(f"/static/images/{random_image}")

        return render_template("index.html", images=images, name=name)
    return render_template("index.html", images=None)

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)
