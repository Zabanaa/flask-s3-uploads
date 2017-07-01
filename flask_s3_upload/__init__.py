from flask import Flask, render_template, request, redirect
from werkzeug.utils import secure_filename

app     = Flask(__name__)
app.config.from_object("flask_s3_upload.config")

from .helpers import *

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/", methods=["POST"])
def upload_file():

    if "user_file" not in request.files:
        return "1. Bruv are you drunk ? Go back and select a file"

    file    = request.files["user_file"]

    """
        These attributes are also available

        file.filename               # The actual name of the file
        file.content_type
        file.content_length
        file.mimetype

    """

    if file.filename == "":
        return "2. Bruv are you drunk ? Go back and select a file"

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        output   = upload_file_to_s3(file, app.config["S3_BUCKET"])
        return output

    else:
        return redirect("/")
