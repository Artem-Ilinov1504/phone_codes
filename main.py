from flask import Flask, render_template, request
app = Flask(__name__)


@app.route("/")
@app.route("/main")
def index():
    return render_template("index.html")


@app.route("/recombination", methods=["GET", "POST"])
def recombination():
    phone1 = None
    country = None
    codes = {
        "Ukraine":'380',
        "Japan":'81',
        "Poland":'48',
        "Spain":'34',
        "Iceland":'354'
    }
    values_list = list(codes.values())
    keys_list = list(codes.keys())
    if request.method == "POST":
        phone1 = str(request.form.get("phone", ""))
        for i in range(len(keys_list)):
            if values_list[i] == phone1[0:3] or values_list[i] == phone1[0:2]:
                country = keys_list[i]

    return render_template("recombination.html", country=country, number= f"+{phone1}")

if __name__ == "__main__":
    app.run(debug=True)

