from flask import Flask, jsonify
from flask_cors import CORS


# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

RESOURCES = [
    {
        "title": "Fibonacci",
        "content": "Fibonacci Sequence",
        "imageUrl": "https://i.pinimg.com/originals/98/82/d5/9882d569f7e0b5665fe3b2edd5069b06.png",
        "rating": 4,
    },
    {
        "title": "DNA",
        "content": "You have enough DNA in your body to, if fully unravelled, stretch from Pluto to the Sun – not just once, but a staggering 17 times.",
        "imageUrl": "https://upload.wikimedia.org/wikipedia/commons/4/4c/DNA_Structure%2BKey%2BLabelled.pn_NoBB.png",
        "rating": 5,
    },
]

# enable CORS
CORS(app, resources={r"/*": {"origins": "*"}})


# sanity check route
@app.route("/ping", methods=["GET"])
def ping_pong():
    return jsonify("pong!")

@app.route('/resources', methods=['GET'])
def all_books():
    return jsonify({
        'status': 'success',
        'resources': RESOURCES
    })


if __name__ == "__main__":
    app.run()
