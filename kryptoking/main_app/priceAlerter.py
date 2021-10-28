from bs4 import BeautifulSoup
import requests
import time
import smtplib
import ssl
from email.mime.text import MIMEText as MT
from email.mime.multipart import MIMEMultipart as MM




#############
# Get the price of crypto:

url = 'https://www.google.com/search?q=bitcoin+price'


# Make a request to the website:

HTML = requests.get(url)

#Parse the HTML

soup = BeautifulSoup(HTML.text, 'html.parser')

#print soup to find where the text is that contains the price of the cryptocurrency

print(soup.prettify())


#Create a function to get teh price of a cryptocurrency. 

def get_crypto_price(coin):
    #Get the price of crypto:

    url = 'https://www.google.com/search?q='+coin+'+price'


    # Make a request to the website:

    HTML = requests.get(url)

    #Parse the HTML

    soup = BeautifulSoup(HTML.text, 'html.parser')

    #Find the current price 
    text = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text

    return text



price = get_crypto_price('litecoin')

print(price)



#Create a function to consistently show the price of crypto when it changes

def main():
        last_price = -1

        # Creating a loop to continuously show the price
        while True:

            crypto = 'bitcoin'

            price = get_crypto_price(crypto)

            if price != last_price:

                print(crypto+' price: ', price)

                last_price = price
                    
            time.sleep(300)


# main()

#store the email addresses for the receiver and senders password.

receiver = 'pythonsendalert@gmail.com'
sender = 'pythonsendalert@gmail.com'

sender_password = 'hello!random!user*'


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
        <h2> """ +text_price+"""
        </h2>
        </body>
        </html>
        """

        #Create a html MIME text object

    MTObj = MT(HTML, 'html')
    msg.attach(MTObj)

    SSL_context = ssl.create_default_context()
    server = smtplib.SMTP_SSL(host='smtp.gmail.com', port=465, context=SSL_context)

    server.login(sender,sender_password)

    #send the email
    server.sendmail(sender,receiver, msg.as_string())


#Create a function to send the alert

def send_alert():
    last_price = -1
    #creating an infinate loop to show the price
    while True:
        coin = 'bitcoin'
        #Get the price of cryptocurrency 
        price = get_crypto_price(coin)
        #Check if price changed
        if price != last_price:
            print(coin.capitalize() + ' price: ', price)
            price_text = coin.capitalize() + ' is ' +price
            send_email(sender, receiver, sender_password, price_text)
            last_price = price #update teh last price
            time.sleep(300)


#sending alert function 
send_alert()

