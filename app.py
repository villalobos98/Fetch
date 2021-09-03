from flask import Flask, jsonify, request, render_template
from Transaction import Transaction

app = Flask(__name__)

transaction_list = []


@app.route('/', methods=['GET', 'POST'])
def up():
    if request.method == "GET":
        return render_template('README.html')


@app.route('/add_transaction/', methods=['POST', 'GET'])
def add_transaction():
    if request.method == 'GET':
        return render_template('add_transaction_view.html')

    if request.method == 'POST':

        # Parse out request data from body of incoming request
        # Parse out request data from Form of incoming request
        # I can also parse out data from body of incoming request
        # But I have chosen to make the View so that using this application doesn't require Postman
        # which I can adjust to make it work as well, it was my first implementation

        # data = request.get_json()
        # date = data['timestamp']
        # payer = data['payer']
        # points = data['points']

        date = request.form.get('timestamp')
        payer = request.form.get('payer')
        points = int(request.form.get('points'))

        # Check if points are
        if points < 0:
            return "Negative points are not possible"

        transaction = Transaction(date, payer)
        transaction_list.append(transaction)

        for transaction in transaction_list:
            if transaction.payer == payer and transaction.date == date:
                transaction.add_transaction(points)

        transaction_dict = transaction.__dict__
        return jsonify(transaction_dict)


@app.route('/spend_points/', methods=['GET', 'POST'])
def spend_points():
    # parse out data from Json body
    # data = request.get_json()
    # points = data['points']
    if request.method == 'GET':
        return render_template('spend_points_view.html')
    if request.method == 'POST':
        points = int(request.form.get('points'))

        # Sort by the oldest transaction date
        transaction_list.sort(key=lambda x: x.date, reverse=True)
        for transaction in transaction_list:
            if transaction.points - points < 0:
                return "Error payer points cannot go negative"
            else:
                transaction.points -= points

        response_transaction = []
        for el in transaction_list:
            response_transaction.append({"payer": el.payer, "points": el.points})

        return jsonify(response_transaction)


@app.route('/points_balance/', methods=['GET'])
def view_points_balance():
    if request.method == "GET":
        payer_points = {}
        for transaction in transaction_list:
            payer_points[transaction.payer] = transaction.points

        print(jsonify(payer_points))
        return jsonify(payer_points)


if __name__ == '__main__':
    app.debug = True
    app.run(use_reloader=True)
