# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 14:18:09 2024

@author: klot_pa
"""
import os
import random
from flask import Flask, render_template, request
from flask_talisman import Talisman

app = Flask(__name__)

csp = {
    'default-src': "'self'",
    'style-src': "'self' 'unsafe-inline'"
}
Talisman(app, content_security_policy=csp)

# Function to get standard images for a letter
def get_images_for_letter(letter):
    image_folder = "./static/images"
    images = [f for f in os.listdir(image_folder) if f.startswith(letter) and f.lower().endswith('_ortho.png')]

    return images

# Function to get AI-generated images for a letter
def get_ai_images_for_letter(letter):
    image_folder = "./static/images"
    images = [f for f in os.listdir(image_folder) if f.startswith(letter) and f.endswith('.png')]
    return images

# Route for the homepage
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name").lower()  # Get the name input
        use_ai = request.form.get("use_ai")  # Check if AI checkbox is checked
        images = []

        # Loop through each letter and get images based on AI selection
        for letter in name:
            if letter.isalpha():
                if use_ai:  # If AI checkbox is checked, use AI images
                    available_images = get_ai_images_for_letter(letter)
                else:
                    available_images = get_images_for_letter(letter)
                
                if available_images:
                    random_image = random.choice(available_images)
                    images.append(f"/static/images/{random_image}")

        return render_template("index.html", images=images, name=name)

    return render_template("index.html", images=None)

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)
