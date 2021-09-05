from flask import Flask, jsonify, request, render_template
from Transaction import Transaction

app = Flask(__name__)

# This list will contain all transactions made by a user
transaction_list = []


# @desc: This route will return the instruction for how to use this application
@app.route('/', methods=['GET'])
def up():
    return render_template('README.html')


# @desc: This endpoint will parse out information from the incoming form request data
# and check if points are positive, and given the correct payer and timestamp
@app.route('/add_transaction/', methods=['POST', 'GET'])
def add_transaction():
    if request.method == 'GET':
        return render_template('add_transaction_view.html')

    if request.method == 'POST':

        # Parse out information from form request
        date = request.form.get('timestamp')
        payer = request.form.get('payer')
        points = int(request.form.get('points'))

        # Check if points are positive, else return error message
        if points < 0:
            return "Negative points are not possible"

        # Create a Transaction for user and store it in a list
        transaction = Transaction(date, payer)
        transaction_list.append(transaction)

        # Find the correct payer and date and update their point balance
        for transaction in transaction_list:
            if transaction.payer == payer and transaction.date == date:
                transaction.add_transaction(points)

        transaction_dict = transaction.__dict__

        # Return JSON data to view
        return jsonify(transaction_dict)


# @desc: This endpoint will parse out point information from the request form data and
# will remove points from oldest transaction timestamp
@app.route('/spend_points/', methods=['GET', 'POST'])
def spend_points():
    # If GET is made then render out view
    if request.method == 'GET':
        return render_template('spend_points_view.html')

    # If POST is made then get points
    if request.method == 'POST':
        points = int(request.form.get('points'))

        # Sort by the oldest transaction date
        transaction_list.sort(key=lambda x: x.date, reverse=False)

        # Remove points from oldest transaction date
        for transaction in transaction_list:
            if transaction.points - points < 0:
                return "Error payer points cannot go negative"
            else:
                # print(transaction.date) # DEBUGGING to see if dates are oldest first to newest
                transaction.points -= points

        response_transactions = []
        for el in transaction_list:
            response_transactions.append({"payer": el.payer, "points": el.points})

        return jsonify(response_transactions)


# This endpoint will display all users that have made a transaction
@app.route('/points_balance/', methods=['GET', "POST"])
def view_points_balance():
    if request.method == "GET":
        return render_template('points_balance_view.html')
    if request.method == "POST":
        # Create the dictionary to handle the format that we are sending back
        payer_points = {}
        for transaction in transaction_list:
            payer_points[transaction.payer] = transaction.points

        # print(jsonify(payer_points)) # USED FOR DEBUGGING
        return jsonify(payer_points)


if __name__ == '__main__':
    app.debug = True
    app.run(use_reloader=True)
