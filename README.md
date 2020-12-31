# python-email-client
This is a program to send email with python


# PYTHON EMAIL CLIENT

This code sends an email with a text message and an image attached
This code is configured to use gmail smtp

To run this code, make sure that your account is able to allow program connections

The code reads the account information from a .env file it is not present in the repository you need to create it

the .env file must include

``
EMAIL =
PASSWORD =
TO =
``
email - login email
password - email password entered
to - recipient's email

The content of the message is obtained from the message.txt file
Feel free to change it

The attached image is obtained from the project's root directory looking for the extension, the code takes only the first .jpeg file found.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

```
python  ^3.8
decouple ^3.3
```

### Installing

You can install the dependences with pip 

```
python -m pip install python-decouple
```

## Run

```
python main.py
```

This command will send the email if you have already configured your .env file

## Authors

* **Anderson F lima**

## Acknowledgments

* This code is for self-improvement only

