**Process Order API**

This is a very small API (one endpoint) written with Flask framework, for academic purposes. 

The `/process_order` endpoint will verify the stock of a product and will generate a payment on Stripe

*How to run it*

Local:

`AWS_ACCESS_KEY=<your_aws_access_key> AWS_SECRET_ACCESS_KEY=<your_aws_secret_key> STRIPE_API_KEY=<your_stripe_api_key> EPSAGON_KEY=<your_epsagon_key> FLASK_APP=app.py flask run`

POST http://localhost:5000/process_order

`
{
 "order": "1",
 "product": "Nike",
 "amount": 400
}
`

Prod:

`AWS_ACCESS_KEY=<your_aws_access_key> AWS_SECRET_ACCESS_KEY=<your_aws_secret_key> STRIPE_API_KEY=<your_stripe_api_key> EPSAGON_KEY=<your_epsagon_key> gunicorn --bind 0.0.0.0:8000 wsgi:app`

POST http://localhost:8000/process_order

`
{
 "order": "1",
 "product": "Nike",
 "amount": 400
}
`

Docker:

`docker build -t <your-namespace>/process_order .`

`docker run -p 8000:8000 -e AWS_ACCESS_KEY=<your_aws_access_key> -e AWS_SECRET_ACCESS_KEY=<your_aws_secret_key> -e STRIPE_API_KEY=<your_stripe_api_key> -e EPSAGON_KEY=<your_epsagon_key> --rm <your-namespace>/process_order`

POST http://localhost:8000/process_order
`
{
 "order": "1",
 "product": "Nike",
 "amount": 400
}
`
