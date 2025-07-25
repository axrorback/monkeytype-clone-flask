from flask import Blueprint, render_template, request, jsonify
from .utils import generate_text
from .models import TypingTest
from . import db

main = Blueprint('main', __name__, template_folder='templates', static_folder='static')

@main.route('/')
def index():
    # HTML sahifani qaytaramiz
    return render_template('index.html')

@main.route('/api/text')
def get_text():
    level = request.args.get('level', 'easy')
    return jsonify({"text": generate_text(level)})

@main.route('/api/submit', methods=['POST'])
def submit_result():
    data = request.get_json()
    test = TypingTest(**data)
    db.session.add(test)
    db.session.commit()
    return jsonify({"message": "Natija saqlandi!"})
