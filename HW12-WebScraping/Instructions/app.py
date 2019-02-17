from flask import Flask, render_template, redirect, jsonify
#import pymongo
import mars_scrape


app = Flask(__name__)

#conn = 'mongodb://localhost:27017'

#client = pymongo.MongoClient(conn)

#db = client.mars_db

@app.route("/")

def home_page():
    data = mars_scrape.scrape()
    return render_template("index.html", Title = data['Title'], News = data['News'], weather = data['Current_Weather'], facts = data['Facts'], last_image = data['Featured_Image'] )


@app.route("/data")

def display_data():
    data = mars_scrape.scrape()
    print(data)
    return jsonify(data)

 




if __name__ == "__main__":
    app.run(debug=True)

