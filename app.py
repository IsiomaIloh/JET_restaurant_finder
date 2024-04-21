import os

from flask import Flask, jsonify, Response

from jetApp.api_calls import get_restaurants_from_jet

app = Flask(__name__)


@app.route('/restaurants/<postcode>', methods=['GET'])
def get_restaurants(postcode) -> Response:
    response = get_restaurants_from_jet(postcode)
    return jsonify(response)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))

    app.run(host='0.0.0.0', port=port)
