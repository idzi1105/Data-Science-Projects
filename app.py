from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy # type: ignore
from datetime import datetime

app = Flask(__name__) # makes an instance of the Flask class
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///study_planner.db' #sqlite database location
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(app)

class StudySession(db.Model):
    id = db.Column(db.Integer, primary_key=True) #unique ID for each session
    subject = db.Column(db.String(100), nullable = False) #so subject name isnt empty
    date = db.Column(db.DateTime, default=datetime.utcnow) #date of study session (auto sets to current date and time)
    hours = db.Columnn(db.Float, nullable = False) #Study hours which cant be empty

    def __repr__(self):
        return f'<StudySession {self.subject} - {self.hours} hours>'
    
