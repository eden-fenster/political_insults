from flask import Flask, render_template, request


app = Flask(__name__)


# Opening page to input details.
@app.route('/')
def hello_world():
    return render_template("index.html", times=2)


@app.route('/fight', methods=['GET', 'POST'])
def fight():
    # Save details into objects.
    p1 = request.form
    p2 = request.form
    # Start fight.
    return "Loser !"


if __name__ == "__main__":
    app.run(debug=True)
