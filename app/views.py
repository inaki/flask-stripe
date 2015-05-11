import os
from flask import render_template, request
from app import app
import stripe

stripe_keys = {
  'secret_key': os.environ['SECRET_KEY'],
  'publishable_key': os.environ['PUBLISHABLE_KEY']
}

stripe.api_key = stripe_keys['secret_key']


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='CSA Box Buydown', key=stripe_keys['publishable_key'])


@app.route('/charge', methods=['POST'])
def charge():
    amount = 500

    customer = stripe.Customer.create(
        email='customer@example.com',
        card=request.form['stripeToken']
    )

    charge = stripe.Charge.create(
        customer=customer.id,
        amount=amount,
        currency='usd',
        description='Flask Charge'
    )

    return render_template('charge.html', amount=amount)
