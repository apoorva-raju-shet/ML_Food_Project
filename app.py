from flask import Flask, render_template, request
from pymongo import MongoClient
import config

app = Flask(__name__)

# mongodb connection
client = MongoClient(config.MONGO_URI)
db = client[config.DATABASE_NAME]
collection = db[config.COLLECTION_NAME]

@app.route("/", methods=["GET","POST"])
def home():
    result=None
    
    if request.method=="POST":
        food_name = request.form["food"]
        
        data = collection.find_one({"food": {"$regex": f"^{food_name}$", "$options": "i"}}, {"_id":0})
        
        if data:
            result=data
        else:
            result={"food":"Not found","calories":"-","protein":"-","carbs":"-","fibre":"-","sugar":"-","potassium":"-"}
    
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)