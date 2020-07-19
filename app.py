from flask import Flask, render_template
from flask_pymongo import PyMongo
import scraping

# set up flask instance
app = Flask(__name__)
# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# add route
@app.route("/")
def index():
   mars = mongo.db.mars.find_one()
   return render_template("index.html", mars=mars)

# scraping route
@app.route("/scrape")
def scrape():
   mars = mongo.db.mars
   mars_data = scraping.scrape_all()
   mars.update({}, mars_data, upsert=True)
   # return "Scraping Successful!"
   # return render_template("index.html", mars=mars)
   return render_template("return.html", mars=mars)

@app.route("/hemisphere")
def hemisphere():
    scraping.get_mars_hemisphere()
    return "Hemisphere Scraping Successful!"

if __name__ == "__main__":
   app.run()

