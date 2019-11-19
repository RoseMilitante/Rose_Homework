from flask import Flask, render_template

# Import our pymongo library, which lets us connect our Flask app to our Mongo database.
import pymongo

# Import scrape_mars
import scrape_mars

# Create an instance of our Flask app.
app = Flask(__name__)

# Create connection variable
conn = 'mongodb://localhost:27017/mars_db'

# Pass connection to the pymongo instance.
client = pymongo.MongoClient(conn)

# Connect to a database. Will create one if not already available.
db = client.mars_db

# Drops collection if available to remove duplicates
db.mars.drop()

# Set route
@app.route('/')
def index():
    # Store the entire mars collection in a list
    mars = list(db.mars.find())
    
    # Return the template with the mars list passed in
    return render_template('index.html', mars=mars)

@app.route("/scrape")
def scrape():
    mars = client.db.mars
    mars_data = scrape_mars.scrape()
    mars.update({}, mars_data)
    return "Done scraping."


if __name__ == "__main__":
    app.run(debug=True)