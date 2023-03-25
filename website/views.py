from flask import Blueprint, redirect, render_template, request, flash, jsonify, url_for
# from flask_login import login_required, current_user  
# from .models import Note
# from . import db
# from sqlalchemy.sql import func
import json
import string

from .response import get_steps, generate_dalle,get_images
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
    steps =  get_steps(promptText)
    print(steps)
    dallE_steps = generate_dalle(steps)
    print(dallE_steps)
    image_links = get_images(dallE_steps)
    print(image_links)
    return jsonify(dict(zip(steps,image_links)))
