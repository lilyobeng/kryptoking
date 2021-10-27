from bs4 import BeautifulSoup

import requests
import time


  #program to get the current price of crypto

#Get the price of crypto:

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
                    
            time.sleep(3)


main()


