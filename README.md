# Chatbot for Disputes

## Initial Setup:
This repo currently contains the starter files.

Clone repo and create a virtual environment
```
$ git clone https://github.com/python-engineer/chatbot-deployment.git
$ cd chatbot-deployment
$ python3 -m venv venv
$ . venv/bin/activate
```
Install dependencies
```
$ (venv) pip install Flask torch torchvision nltk
```
Install nltk package
```
$ (venv) python
>>> import nltk
>>> nltk.download('punkt')
```

Run
```
$ (venv) python train.py
```
This will dump data.pth file. And then run
the following command to test it in the console.
```
$ (venv) python chat.py
```

## Flask Deployment
The API was deployed using Flask and can be found in app.py
To use the deployed chatbot simply paste the following URL in your browser:

  https://peerpocket-disputes.onrender.com/chat?message=<CUSTOMER_QUERY>

<em>Sample Query</em>
  https://peerpocket-disputes.onrender.com/chat?message=hi

<i>Replace <CUSTOMER_QUERY> with the query</i>

This chatbot was trained on the data contained in intents.json file which can handle user's questions on:
1. Greeting
2. Farewell
3. Thanks
4. Peer to peer loans
5. Part payments
6. Loan Application Process
7. Becoming a lender
8. Interest rates
9. Minimum loan amount
10. Late repayment
11. Loan defaulters
12. Additional Charges
13. Double Payment
14. Password Reset
15. Early Repayment
