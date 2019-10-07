**Process Order API**

This is a very small API (one endpoint) written with Flask framework, for academic purposes. 

The `/process_order` endpoint will verify the stock of a product and will generate a payment on Stripe

*How to run it*

Local:

`AWS_ACCESS_KEY=<your_aws_access_key> AWS_SECRET_ACCESS_KEY=<your_aws_secret_key> STRIPE_API_KEY=<your_stripe_api_key> FLASK_APP=app.py flask run`

Go to http://localhost:5000/process_order

Prod:

`AWS_ACCESS_KEY=<your_aws_access_key> AWS_SECRET_ACCESS_KEY=<your_aws_secret_key> STRIPE_API_KEY=<your_stripe_api_key> gunicorn --bind 0.0.0.0:8000 wsgi:app`

Go to http://localhost:8000/process_order

Docker:

`docker build -t <your-namespace>/process_order .`

`docker run -p 8000:8000 -e AWS_ACCESS_KEY=<your_aws_access_key> -e AWS_SECRET_ACCESS_KEY=<your_aws_secret_key> -e STRIPE_API_KEY=<your_stripe_api_key> --rm <your-namespace>/process_order`

Go to http://localhost:8000/process_order

