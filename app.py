from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def hello():
    dic = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
    return render_template("index.html", time=dic["time"]["updated"],
                           USD=dic["bpi"]["USD"]["description"],
                           EUR=dic["bpi"]["EUR"]["description"],
                           GBP=dic["bpi"]["GBP"]["description"],
                           pd=dic["bpi"]["USD"]["rate"],
                           pg=dic["bpi"]["GBP"]["rate"],
                           pe=dic["bpi"]["EUR"]["rate"])


if __name__ == '__main__':
    app.run(debug=True)
