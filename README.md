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
## Instalation


1. Clone the repository:
To clone the repository, use the following command: 
  git clone https://github.com/ciminomariano/fixtradingchallenge.git

2. Navigate to the project directory:
   cd fixtradingchallenge
3. Create a virtual environment:
   python3 -m venv venv
4. Activate the virtual environment:
   source venv/bin/activate
5. Install the project dependencies:
   pip install -r requirements.txt


## Run the Server

To run the server, use the following command:

1. Navigate to the folder app/api
2. Run the next command
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

The server will start running on `https://localhost:8000`.

## Usage

The app is deployed on Heroku so you can test on the fly or
locally.

The swagger Documentation for the endpoint is on the next link

https://fixtradingchallenge-4ce59f8b8ab0.herokuapp.com/docs

The postman request can be pointed to
https://fixtradingchallenge-4ce59f8b8ab0.herokuapp.com/

To send a test order, you can use Postman or any HTTP client of your choice.
Set the necessary parameters for the order, such as symbol, quantity, and order type. 
Make a POST request to the following endpoint:

In the folder Collections of the project there is a Postman
collection to test the api with all the parameters set.
The link is the next
https://github.com/ciminomariano/fixtradingchallenge/tree/main/collections

You just need to import the collection on Postman

Check the response to verify the success or failure of the order.

## Documentation


To connect to the FIX API, there are some steps that you must complete. Detailed documentation and API references can be found in the following links:

    
    Technical Documentation Of The Project 
    Video Tutorial
    FIX API Documentation https://tradermade.com/docs/fix-api
    FIX Protocol https://www.fixtrading.org/what-is-fix/

Contributing

Contributions to this project are welcome. Please follow the guidelines outlined in the CONTRIBUTING.md file to contribute to the project.

## License

This project is licensed under the [MIT License](LICENSE).