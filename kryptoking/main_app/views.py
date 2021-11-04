
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Post, Comment
from .forms import CommentForm


<<<<<<< HEAD
import pandas as pd
=======
from datetime import datetime, timedelta


>>>>>>> 5aab093dc7ccbf45fa5716fb56035eb586e7e86b



from bs4 import BeautifulSoup

import requests


# Create your views here.

class PostCreate(LoginRequiredMixin,CreateView):
  model = Post
  fields = ['topic','body']

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class PostUpdate(LoginRequiredMixin, UpdateView):
  model = Post
  fields = ['topic', 'body']

class PostDelete(LoginRequiredMixin, DeleteView):
  model = Post
  success_url = '/post/'


   
def home(request):
  return render(request, 'home.html')



def post_detail(request, post_id):
  post = Post.objects.get(id=post_id)
  comment_form = CommentForm()
  return render(request, 'post/detail.html', {'post': post, 'comment_form': comment_form})


def add_comment(request, post_id):
  form = CommentForm(request.POST)
  if form.is_valid():
    new_comment = form.save(commit=False)
    new_comment.post_id = post_id
    new_comment.save()
  return redirect('detail', post_id=post_id)


def delete_comment(request, id):

  context = {}
  obj = get_object_or_404(Comment, id = id)
  if request.method == 'POST':
    obj.delete()
    return redirect('/')
  return render(request, 'post/delete_comment.html', context)

receiver = 'variablefromform'
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
# send_alert()

def get_crypto_price(coin):
    #Get the price of crypto:
  url = 'https://www.google.com/search?q='+coin+'price'
    # Make a request to the website:
  HTML = requests.get(url)
    #Parse the HTML
  soup = BeautifulSoup(HTML.text, 'html.parser')
  print(soup)
    #Find the current price 
  text = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
  return text



@login_required
def krypto_index(request):
    query = request.GET.get('q')
    if query:
      current_price = get_crypto_price(query)
      print(current_price,"this is the price")

      return render(request, 'post/index.html', {'current_price': current_price, 'query': query})
    
    else:
      return render(request, 'post/index.html')





  
@login_required
def post_index(request):
  post = Post.objects.all()
  comment = Comment.objects.all()
  return render(request, 'post/post_index.html', {'post': post, 'comment': comment})




def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)



  #program to get the current price of crypto

#Get the price of crypto:

<<<<<<< HEAD

# url = 'https://www.google.com/search?q='+coin+'+price'
=======



url = 'https://www.google.com/search?q=bitcoin+price'
  



>>>>>>> 5aab093dc7ccbf45fa5716fb56035eb586e7e86b


# # Make a request to the website:

# HTML = requests.get(url)

# #Parse the HTML

# soup = BeautifulSoup(HTML.text, 'html.parser')

# #print soup to find where the text is that contains the price of the cryptocurrency

# print(soup.prettify())