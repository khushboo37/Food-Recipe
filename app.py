from flask import Flask, render_template, request, redirect
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client['food_recipes']
recipes_collection = db['recipes']

@app.route('/')
def index():
    recipes = recipes_collection.find()
    return render_template('index.html', recipes=recipes)

@app.route('/add_recipe', methods=['GET', 'POST'])
def add_recipe():
    if request.method == 'POST':
        name = request.form['name']
        ingredients = request.form['ingredients']
        instructions = request.form['instructions']
        recipes_collection.insert_one({
            'name': name,
            'ingredients': ingredients,
            'instructions': instructions
        })
        return redirect('/')
    return render_template('add_recipe.html')

if __name__ == '__main__':
    app.run(debug=True)
