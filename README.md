# JET Restaurant Finder

This project is a simple Flask application that uses the Just Eat API to retrieve and filter restaurant data based on a given postcode. The application focuses specifically on restaurant information and displays the following details from the 'restaurant object': Name, Cuisines, Numeric Rating, and Address.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.12 or higher
- Flask 3.0.3 or higher
- Requests 2.31.0 or higher

You can install the dependencies with the following command:

```bash
poetry install
```

### Running the Application

To run the application, navigate to the project directory and run the following command:

```bash
flask run
```

The application will start running at `http://0.0.0.0:8080`.

## Usage

To get restaurant data for a specific postcode, make a GET request to the `/restaurants/<postcode>` endpoint. Replace `<postcode>` with the actual postcode you want to search for.

The response will be a JSON object containing the restaurant data.
