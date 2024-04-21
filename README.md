# JET Restaurant Finder

This project is a simple Flask application that uses the Just Eat API to retrieve and filter restaurant data based on a given postcode. The application focuses specifically on restaurant information and displays the following details from the 'restaurant object': Name, Cuisines, Numeric Rating, and Address.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.12 or higher
- Flask 3.0.3 or higher
- Requests 2.31.0 or higher
- Poetry 1.1.11 or higher

### Steps

1. **Clone the repository**

   You can clone the repository by running the following command in your terminal:

   ```bash
   git clone https://github.com/IsiomaIloh/JET_restaurant_finder.git
    ```
   
2. **Navigate to the project directory**

   Change your current directory to the project's directory:

   ```bash
   cd JET_restaurant_finder
   ```

3. **Install the dependencies**

   You can install the dependencies by running the following command:

   ```bash
   poetry install
   ```
   
   ```bash
   poetry shell
   ```
   
4. **Running the Application**

   To run the application, navigate to the project directory and run the following command:

   ```bash
   flask run --host=0.0.0.0 --port=8080
   ```

   The application will start running at `http://127.0.0.1:8080/`.

5. **Testing the Application**

   To run the tests, navigate to the project directory and run the following command:

   ```bash
   pytest
   ```

   This will run all the tests in the project.


## Usage

To get restaurant data for a specific postcode, you need to:

1. Navigate to the homepage of the application.
2. Enter the desired postcode into the search bar and submit the form.
3. The application will then display a list of restaurants in the form of cards, each containing information about a restaurant in the specified postcode area.

Each restaurant card will display the following information:

- Restaurant Name
- Cuisines offered
- Numeric Rating
- Address

Please note that the restaurant data is retrieved from the Just Eat API.
