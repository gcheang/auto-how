from flask import Blueprint, redirect, render_template, request, flash, jsonify, url_for
# from flask_login import login_required, current_user
# from .models import Note
# from . import db
# from sqlalchemy.sql import func
import json
import string

from .response import answer_question, generate_image
import random

# courseText
# quizQuestions
# response
# summary
# images

prompt = "default"
courseParagraphs = []
courseImages = []

# usually easier to keep the name the same as the file
views = Blueprint('views', __name__)

# homepage
@views.route('/', methods=['GET', 'POST'])
def home():
    return render_template('query.html', prompt="", courseParagraphs="", courseImages="")

@views.route('/generate-response', methods=['POST'])
def generate_response():
    prompt = json.loads(request.data)
    promptText = prompt['text']
    print(promptText)
    return jsonify({"resp": answer_question(promptText), "image_url": generate_image(promptText)})
