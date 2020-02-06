from flask import  Flask
from config import Config
import mongoengine

db = mongoengine

app = Flask(__name__)
app.config.from_object(Config)

db.connect('ReadingComprehensionDB')
app.run(debug=True)
from app import routes , models
