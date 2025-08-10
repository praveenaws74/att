from flask import Blueprint, render_template
import datetime

main = Blueprint('main', __name__)

@main.route('/')
def index():
    students = [
        {'name': 'Alice', 'status': 'Present'},
        {'name': 'Bob', 'status': 'Absent'},
        {'name': 'Charlie', 'status': 'Present'},
    ]
    return render_template('index.html', students=students, date=datetime.date.today())
