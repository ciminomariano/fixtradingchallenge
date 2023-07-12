# FIXTrading Challenge

This project is a Python-based API that connects 
to a FIX API-based broker server. 
It provides an endpoint to send orders using Postman.
The project is built using the FastAPI framework and is deployed on Heroku. 
The source code is version controlled using GitHub.

## Prerequisites

Before running the project, make sure you have the following prerequisites installed:

- Python 3.x
- pip (Python package manager)

## Clone the Repository

To clone the repository, use the following command:

git clone https://github.com/ciminomariano/fixtradingchallenge.git

markdown


## Setup

1. Navigate to the project directory:

cd fixtradingchallenge


2. Create a virtual environment:

python3 -m venv venv


3. Activate the virtual environment:

source venv/bin/activate


4. Install the project dependencies:

pip install -r requirements.txt


## Run the Server

To run the server, use the following command:

Navigate to the folder app/api
Run the next command
uvicorn main:app --reload --ssl-keyfile=private.key --ssl-certfile=certificate.crt

This should start your server and you will see a message like the next

INFO:     Uvicorn running on https://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [8307] using StatReload
INFO:     Started server process [8309]
INFO:     Waiting for application startup.
ERROR:root:Config file path de mi archivo: /home/mariano/python/fixtradingchallenge/app/api/clientLocal.cfg
2023-07-12 13:21:37,982 - services.fix_socket_service - INFO - FIX initiator started successfully
INFO:services.fix_socket_service:FIX initiator started successfully
INFO:     Application startup complete.
 toAdmin 8=FIX.4.49=7935=A34=15949=D103452324_client152=20230712-16:21:38.20156=FXCM98=0108=3010=182
 login Message FIX.4.4:D103452324_client1->FXCM


The server will start running on `http://localhost:8000`.

## Usage

The app is deployed on Heroku
The swagger Documentation for the endpoint is on the next link 

https://fixtradingchallenge-4ce59f8b8ab0.herokuapp.com/docs

The postman request can be pointed to
https://fixtradingchallenge-4ce59f8b8ab0.herokuapp.com/

To send a test order, you can use Postman or any HTTP client of your choice.
Set the necessary parameters for the order, such as symbol, quantity, and order type. 
Make a POST request to the following endpoint:

In the folder Collections of the project there is a Postman
collection to test the api.


As the API is deployed In



Check the response to verify the success or failure of the order.

## Documentation

For detailed documentation and API reference, refer to the [FIX API Documentation](https://tradermade.com/docs/fix-api) and the source code in the `app` directory.

## Contributing

Contributions to this project are welcome. If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).