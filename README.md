**Process Order API**

This is a very small API (one endpoint) written with Flask framework, for academic purposes. 

The `/process_order` endpoint will verify the stock of a product and will generate a payment on Stripe

*How to run it*

Local:

`FLASK_APP=app.py flask run`

Go to http://localhost:5000/process_order

Prod:

`gunicorn --bind 0.0.0.0:8000 wsgi:app`

Go to http://localhost:8000/process_order

Docker:

`docker build -t <your-namespace>/process_order  .`

`docker run -p 8000:8000 --rm <your-namespace>/process_order`

Go to http://localhost:8000/process_order

