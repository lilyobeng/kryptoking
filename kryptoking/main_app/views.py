
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Post, Comment
from .forms import CommentForm


from datetime import datetime, timedelta

import plotly.graph_objects as go
import pandas as pd

 


from bs4 import BeautifulSoup

import requests
import time

# Create your views here.

class PostCreate(LoginRequiredMixin,CreateView):
   model = Post
   fields = ['body']

   def form_valid(self, form):
      form.instance.user = self.request.user
      return super().form_valid(form)

class PostUpdate(LoginRequiredMixin, UpdateView):
  model = Post
  fields = ['body']

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


def get_crypto_price(coin):
    #Get the price of crypto:
    url = f'https://www.google.com/search?q={coin}price'
    # Make a request to the website:
    HTML = requests.get(url)
    #Parse the HTML
    soup = BeautifulSoup(HTML.text, 'html.parser')
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

url = 'https://www.google.com/search?q=bitcoin+price'
  
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')

fig = go.Figure(data=[go.Candlestick(x=df['Date'],
       open=df['AAPL.Open'], high=df['AAPL.High'],
       low=df['AAPL.Low'], close=df['AAPL.Close'])
                     ])

fig.update_layout(xaxis_rangeslider_visible=False)
fig.show()



# Make a request to the website:

HTML = requests.get(url)

#Parse the HTML

soup = BeautifulSoup(HTML.text, 'html.parser')

#print soup to find where the text is that contains the price of the cryptocurrency

print(soup.prettify())