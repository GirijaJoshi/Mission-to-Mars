# Mission-to-Mars Challenge
This challenge is to explore the HTML, Flask, Spliter and Beautifulsoup.
### Localhost
When we run flask app first page will have option to scrape the data via button or http://127.0.0.1:5000/scrape, will start scraping the data from 'https://mars.nasa.gov/news/'. Code in app.py to start the scraping:
```python
@app.route("/scrape")
def scrape():
   mars = mongo.db.mars
   mars_data = scraping.scrape_all()
   mars.update({}, mars_data, upsert=True)
   return render_template("return.html", mars=mars)
```
### Flow
Above code will call function scrape_all() from scraping.py file. Which will use spliter and Beautifulsoup to get data from website and return dictonary to API. API will connect to MongoDB and update the informaiton in specified database and specified collection. Index.html will go and get the data from MongoDB and render it on webpage using template speficied in index.html.


