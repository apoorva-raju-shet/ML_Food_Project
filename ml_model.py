from pymongo import MongoClient
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import config

def run_model():

    # connect mongodb
    client = MongoClient(config.MONGO_URI)
    db = client[config.DATABASE_NAME]
    collection = db[config.COLLECTION_NAME]

    # fetch data
    data = list(collection.find({}, {"_id":0}))
    df = pd.DataFrame(data)

    print("Dataset from MongoDB:")
    print(df.head())

    # create calorie category (classification)
    def category(cal):
        if cal < 100:
            return "Low"
        elif cal < 250:
            return "Medium"
        else:
            return "High"

    df["calorie_level"] = df["calories"].apply(category)

    # features and label
    X = df[['protein','carbs','fibre','sugar','potassium']]
    y = df['calorie_level']

    # split data
    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)

    # model
    model = DecisionTreeClassifier()
    model.fit(X_train,y_train)

    accuracy = model.score(X_test,y_test)
    print("\nModel Accuracy:", accuracy)
    print("====================================")

    print("\nFood Nutrition & Predicted Category\n")

    for index, row in df.iterrows():
        features = [[row['protein'], row['carbs'], row['fibre'], row['sugar'], row['potassium']]]
        prediction = model.predict(features)

        print("Food:", row['food'])
        print("Calories:", row['calories'])
        print("Protein:", row['protein'])
        print("Carbs:", row['carbs'])
        print("Predicted Category:", prediction[0])
        print("----------------------------------")

    return accuracy