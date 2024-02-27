from flask_wtf import FlaskForm
from wtforms import StringField, validators, TextAreaField, EmailField
from wtforms.validators import InputRequired, Email

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired()])
    email = EmailField('Email', validators=[Email()])
    subject = StringField('Subject', validators=[InputRequired()])
    message_box = TextAreaField('Message', validators=[InputRequired()])
