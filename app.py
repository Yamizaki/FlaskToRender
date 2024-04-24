from flask import Flask, render_template
from routes.todo import todo

from  dotenv import load_dotenv
import os 
from config.mongodb import mongo

load_dotenv()

app = Flask(__name__)

# Conexion con Mongo
app.config['MONGO_URI'] = os.getenv('MONGO_URI')
mongo.init_app(app)
# Endpoints

@app.route('/')
def index():
    return render_template('index.html')

##############


##############





# Trababa de manera similar al URL PATTERNS ed DJANGO
app.register_blueprint(todo, url_prefix='/todo')

# Inicializador
if __name__ == '__main__':
    app.run(debug=True)