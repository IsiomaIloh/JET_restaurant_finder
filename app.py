import os

from flask import Flask, request, render_template

from jet_app.api_calls import get_restaurants_from_jet

app = Flask(__name__, template_folder='jet_app/templates')


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Extracts the postcode from the form data
        postcode = request.form['postcode'].replace(' ', '')

        return get_restaurants(postcode)

    # If it's not a POST request, it just renders the initial form page
    return render_template('index.html')


@app.route('/restaurants/<postcode>', methods=['GET'])
def get_restaurants(postcode):
    response = get_restaurants_from_jet(postcode)
    return render_template(
        'results.html',
        restaurants=response,
        postcode=postcode
    )


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))

    app.run(host='0.0.0.0', port=port)
