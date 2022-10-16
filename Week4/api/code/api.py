from flask import Flask, request
import random
import json
import os

app = Flask(__name__)

@app.route('/meal')
def meal_pick():
    meals = [
    {'Meal': 'Mushroom Burger',
     'Price': '$10.00'},
    {'Meal': 'Crispy Fried Chicken',
     'Price': '$11.00'},
    {'Meal': 'Fish & Chips',
     'Price': '$10.00'},
    {'Meal': 'Spaghetti & Meatballs',
     'Price': '$12.00'},
    {'Meal': 'Hotdog Sandwish',
     'Price': '$10.00'},
    {'Meal': 'Macaroni Soup',
     'Price': '$3.99'},
    {'Meal': 'Tex Mex Chill',
     'Price': '$3.99'},
    {'Meal': 'Frensh Fries',
     'Price': '$4.50'},
    {'Meal': 'Fried Calamari',
     'Price': '$9.99'},
    {'Meal': 'Beef Taco',
     'Price': '$7.50'},
    {'Meal': 'Water',
     'Price': '$2.99'},
    {'Meal': 'Sparking Water',
     'Price': '$3.99'},
    {'Meal': 'Soda in A Bottle',
     'Price': '$4.50'},
    {'Meal': 'Orange Juice',
     'Price': '$6.00'},
    {'Meal': 'Fresh Lemonade',
     'Price': '$7.50'},]
    meal_picked = random.choice(meals)
    return json.dumps(meal_picked)

if __name__ == '__main__':
    app.run(host="0.0.0.0")



