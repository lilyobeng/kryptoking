from bs4 import BeautifulSoup
import requests
import time
import smtplib
import ssl
from email.mime.text import MIMEText as MT
from email.mime.multipart import MIMEMultipart as MM



#store the email addresses for the receiver and senders password.

receiver = 'temofav577@forfity.com'
sender = 'temofav577@forfity.com'

sender_password = 'put password here'


def send_email(sender, receiver, sender_password, text_price):
    # Create a MIMIMultipart object

    msg = MM()
    msg['Subject'] = "New Crypto Price Alert !"
    msg ['From'] = sender
    msg ['To'] = receiver 

    #Create the HTML for the message

    HTML = """
        <html>
        <body>
        <h1> New Crypto Price Alert ! </h1>