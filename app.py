# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 14:18:09 2024

@author: klot_pa
"""

from flask import Flask, render_template, request

app = Flask(__name__)

# Route for the homepage
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name").lower()  # Get the name input and convert it to lowercase
        images = []

        # Loop through each letter in the name and generate the corresponding image paths
        for letter in name:
            if letter.isalpha():  # Check if the character is a letter
                images.append(f"/static/images/{letter}.png")

        return render_template("index.html", images=images, name=name)
    return render_template("index.html", images=None)

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)
