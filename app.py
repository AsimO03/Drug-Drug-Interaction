from flask import Flask, render_template, request
from data_controller import DataController


app = Flask(__name__)

dataController = DataController("CombinedDatasetConservativeTWOSIDES.csv")

@app.route("/")
def hello_world():
    args = request.args

    # if we have medications as argument in the get URL, it's a "See Results" request
    if("medications" in args):
        # evaluate the medication
        interactions = dataController.find_drug_interactions_by_list(args['medications'].split(','))
        # get only the needed information out of the return value
        readable_interactions = [{"object": interaction["object"], "precipitant": interaction["precipitant"] , "description": interaction["label"]} for interaction in interactions]
        # return the template rendered with results in it
        return render_template("index.html", interactions=readable_interactions)

    # just return the index template without data in it
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)