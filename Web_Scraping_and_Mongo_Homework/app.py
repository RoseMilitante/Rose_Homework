from flask import Flask, render_template, redirect
# Import our pymongo library, which lets us connect our Flask app to our Mongo database.
from flask_pymongo import PyMongo
# Import scrape_mars
import scrape_mars

# Create an instance of Flask app.
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_db")

# Drops collection if available to remove duplicates
#db.mars.drop()

# Set route
@app.route('/')
def home():
    # Store the entire mars collection in a list
    mars = mongo.db.collection.find_one()
    
    # Return the template with the mars list passed in
    return render_template('index.html', mars=mars)

# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():

    # mars = client.db.mars
    mars_data = scrape_mars.scrape()
    mongo.db.collection.update({}, mars_data, upsert=True)
    
    # Redirect back to home page
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)