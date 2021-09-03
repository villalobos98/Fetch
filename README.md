# Fetch
README for Fetch Web Service
=======================

A web service that accepts HTTP requests and returns responses based on
the conditions outlined in the next

Description
-----------

Our users have points in their accounts. Users only see a single balance
in their accounts. But for reporting purposes we actually track their
points per payer/partner. In our system, each transaction record
contains: payer (string), points (integer), timestamp (date).

Notes
-----------
In this project I made the user experience simple, so that the anyone using this app 
could understand how to use it. 
I used used a form to send over my request data to my Flask backend server.
I do understand that I did not have to do this, I have chosen to make the View for all 3
routes so that using this application doesn't require Postman. You may use it optionally if 
you would like. 

I am able to change this code so that I can also parse out information from the body, 
which I can adjust to make it work as well, it was my first implementation. 

### Dependencies

-   click 8.0.1
-   colorama 0.4.4
-   DateTime 4.3
-   Flask 2.0.1
-   itsdangerous 2.0.1
-   Jinja2 3.0.1
-   MarkupSafe 2.0.1
-   pip 21.2.4
-   pytz 2021.1
-   setuptools 57.4.0
-   Werkzeug 2.0.1
-   zope.interface 5.4.0

### Executing program

-   How to run the program
-   Step-by-step bullets

    -   If you're running this through an IDE
    -   Go to the Fetch Directory
    -   Right click on the app.py and run Flask(app.py)
    -   To access the Add Transactions Route go to
        http://localhost:5000/add_transaction and enter form
        information
    -   To add more transactions use the back button to enter more
        information into the form
    -   To access the Spend Points Route go to
        http://localhost:5000/spend_points and enter form information
    -   To spend more points use the back button to access the form
    -   To access the Point Balances Route go to
        http://localhost:5000/points_balance and enter form information
    -   The Point Balances Route above will display all player point
        balances

Author
------

@Isaias_Villalobos
