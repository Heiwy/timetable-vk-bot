from flask import current_app as app
from .models import database
# , Chats, Timetable, SystemCommands, UserCommands


@app.route('/')
def index():
    return "<h1>Test site.</h1>"
