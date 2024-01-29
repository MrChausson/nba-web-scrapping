# Web Scraping Workshop

# Made by

## Clement Chausson
## Clement De Laage De Meux
## Grégoire Biendiné

---

## Introduction

This workshop will introduce you to the basics of web scraping using Python. We will be using the [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) library to parse HTML and XML documents. We will also be using the [requests](https://requests.readthedocs.io/en/master/) library to make HTTP requests.
Some other libraries will be used for the other parts of the workshop, but I will introduce them when we will need them.

## Prerequisites

- Basic knowledge of Python
- Basic knowledge of HTML
- Basic knowledge of HTTP

In this first part of the workshop, you will enter the world of the web. You will have to understand how http requests work.
If you don't, it will be harder to understand, but you can still follow the workshop if you don't understand something
you can always ask me.

## Setup

1. Clone this repository
2. Install the required packages using `pip install -r requirements.txt`
3. Follow the steps of this README

## What is web scraping?

Web scraping is the process of extracting data from websites. This can be done manually, but it is usually done automatically using a script. Web scraping is used for a variety of purposes, such as data mining, contact scraping, price monitoring, etc.
A good example of web scraping is for lead generation. Any company needs clients, but the first step is of course to find them.
You can do it manually, look for clients in the streets, or have a web scraping script that will look for clients for you on the internet.
For example, imagine your client target is doctors, then you will look for a website that lists all the doctors of a city, and scrape them.
Here you then have a list of all the doctors of a city. Of course, it's not that easy because some websites are harder to scrape, or just because there is no website where you can find such information.
Another good use of web scraping that could be really useful for you is web scraping internship and job opportunities on websites like LinkedIn, Indeed, etc.
You create your scrapper that will then get all the jobs for you, and automatically send your CV.

## How do you scrape?

There are many ways to scrape a website, but the most common way is to use the [requests](https://requests.readthedocs.io/en/master/) library to make HTTP requests and the [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) library to parse HTML and XML documents.
When you do a http request to a website, you will most of the time get the HTML code, if there is no error.
Then you will parse the HTML code to get the data you want.

For example, you can try with the home page of Google. Go to [google.com](https://www.google.com/) and right-click on the page, then click on inspect.
You will see the HTML code of the page. On this HTML code, you will be able to see some information such as the title of the page.
Of course, this example is really simplistic, but it's just to show you how it works.

## Let's start scraping

---

### 1. Making a request

First, we will make a request to a website. We will use the [requests](https://requests.readthedocs.io/en/master/) library to make the request.
We will use the [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) library to parse the HTML code.
First of all, we will import the libraries into the code:

```python
import requests
from bs4 import BeautifulSoup
```

The objective of this first part is to parse a [website](https://www.basketball-reference.com/leagues/NBA_2023_per_game.html) containing information about the best basketball players of 2023.
On this website, you will find a table of all the players with some statistics about their performance.

To get all this information, you will first need to use the `requests` library. With it, you can do a simple `get` request
to the link that I gave you, you will get the HTML code of the page.

```python
response = requests.get("https://www.basketball-reference.com/leagues/NBA_2023_per_game.html")
```

### 2. Parsing the HTML code

Now that you have the HTML code of the website, you will need to parse it to get the information you want.
First, set the BeautifulSoup parser up with the information you have, and the type of information you will be parsing.

```python
soup = BeautifulSoup(response.content, "html.parser")
```

Now that you have the parser, you will need to find the table that contains the information you want.
To do that, you will need to inspect the HTML code of the website.
You will need to be looking for the tag of the table, and the class of the table.
You can do that by right-clicking on the table, and then click on inspect.

Once you have the tag and the class/id of the table, you will be able to find it with the `select` method of BeautifulSoup.
This method will return you a list of all the elements that match the tag and the class/id you gave it.

```python
table = soup.select("h1#title")
```

This is how you would use the `select` method to find the title of the website that is a `h1` tag with the id `title`.
We will then parse this table to get the following information:

- Name
- Age
- Position
- Team
- Total Games
- Points per Game
- Total Rebounds per Game

Once you have selected the table, you will need to parse it to get the information you want.
A simple `for` loop through the list that was obtained with the `select` method will do the trick.
Inside that loop trick you will have to use the `select` method again to get the information you want.
Remember how you did with the table, it will be the same way, find the tag and the class/id.

### 3. Exporting the data

Once the list of players is fully parsed, I am going to need you to create a DataFrame with the information you got.
You can simply use the `pandas` library to do that.

```python
import pandas as pd

df = pd.DataFrame(players_list)
``` 

With this DataFrame, you are now able to export the data to a CSV file thanks to the `to_csv` method.
Just in case, I will also need you to export the data to an SQLite database, don't worry it's really easy.
You will need to use the `to_sql` method of the DataFrame, and give it the connection to the database.
You can use the `sqlite3` library to create the connection to the database.

```python
import sqlite3

conn = sqlite3.connect("players.db")
```

# Part 2—Dynamic Web Scraping and Automation with Selenium

---

## Introduction

In this part of the workshop, we will be using Selenium to scrape a dynamic website.
We will also be using the [requests](https://requests.readthedocs.io/en/master/) library to make HTTP requests.
Now that you know how to scrape a simple website, we will see how to scrape a dynamic website.

## What is a dynamic website?

A dynamic website is a website that changes depending on the user, the time, or any other factor.
For example, a website that shows the current time is a dynamic website because it changes depending on the time.
A dynamic website is usually made with JavaScript, and that's why it's harder to scrape.
When you do a request to a dynamic website, you will get the HTML code of the website, but without the JavaScript code.
This means that when you request the HTML code, the code will not have been modified by the JavaScript code.
This is why you will need to use Selenium to scrape a dynamic website.

## Let's start scraping

---

With Selenium, you will be able to scrape a dynamic website, it will also allow you to automate some tasks.
For example, Selenium can open a Google Chrome window, and then go to a website, and click on a button.
This is really useful when you want to automate some tasks.

### 1. The goal

The main goal of this part is to be able to automate the sending of a message on WhatsApp.
You will need to open a Google Chrome window, go to WhatsApp, and then send a message to a specific person.
The issue is that Google and WhatsApp are dynamic websites that are linked to your accounts.
You will need to find a way to login to your accounts in the Selenium window.

### 2. Open WhatsApp

To open WhatsApp, you will need to use the `webdriver` module of Selenium.
This module will allow you to open a Google Chrome window, and then go to a website.
You will need to use the `get` method of the `webdriver` module to go to a website.

```python
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")
time.sleep(15)
```

This should open a window and go to WhatsApp.
We will wait 15 seconds, so we can clearly see what is happening before Selenium closes the window.
As you can see, Selenium opens Google without any problem, but it doesn't log you in.
So your WhatsApp window is asking you to scan the QR code to log in.
First, we will need to load your Chrome Profile so that it loads your account information.
To do that, you will need to use the `ChromeOptions` class of Selenium.

```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument("--user-data-dir={path-of-profile}")
options.add_argument("--profile-directory={profile-name}")
driver = webdriver.Chrome(options=options)
driver.get("https://web.whatsapp.com/")
time.sleep(15)
```

You can find the path of your Chrome Profile by going to `chrome://version/` in Google Chrome.
You will then need to copy the path of the `Profile Path` field.
You will need to remove the last part of the path, for example,
if the path is `/home/{username}/.config/google-chrome/Default`, you will need to remove the `/Default` part, which is the profile name.
You will need to replace the `{path-of-profile}` with the path you copied.
You will also need to replace the `{profile-name}` with the profile name you removed from the path.
Once this has been done, the Chrome window should open with the profile loaded.
You will then need to scan the QR code to log in to your WhatsApp account.
Once you have done it once, it should not ask you to scan the QR code again.

### 3. Send a message

Now that you are logged in to your WhatsApp account, you will need to send a message to a specific person.
To do that, you will need to find the person you want to send a message to.
Remember the first part of the workshop, you will need to inspect the HTML code of the website to find the tag and the class/id of the element you want to find.
Here, you are looking for the search bar element in the HTML code of the website.
Inspect the website to help you find it.
Once you have found the element in the code, right-click it and click on Copy > Copy Xpath.
This will copy the Xpath of the element, which is a unique path to the element in the HTML code.
You will then need to use the `find_element` method of the `webdriver` module to find the element.

```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument("--user-data-dir={path-of-profile}")
options.add_argument("--profile-directory={profile-name}")
driver = webdriver.Chrome(options=options)
driver.get("https://web.whatsapp.com/")
search_bar = driver.find_element("xpath", "{xpath-of-search-bar}")
```

You will need to replace the `{xpath-of-search-bar}` with the Xpath you copied.
Once you have done this, you will see that the window should close and the program crashes.
This is because you need to wait for the element to load before you can find it.
This is what we were talking about with the dynamic websites.
You will need to wait for the element to load before you can find it.
To do that, you will need to use the `WebDriverWait` class of Selenium.

```python
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument("--user-data-dir={path-of-profile}")
options.add_argument("--profile-directory={profile-name}")
driver = webdriver.Chrome(options=options)
driver.get("https://web.whatsapp.com/")
search_bar = WebDriverWait(driver, 15).until(EC.presence_of_element_located(("xpath", "{xpath-of-search-bar}")))
search_bar.click()
time.sleep(15)
```

You will need to replace the `{xpath-of-search-bar}` with the Xpath you copied.
As you can see, now the program waits for the element to load before it tries to find it.
And then, it clicks it, and waits for 15 seconds before closing the window.
Now that you have found the search bar, you will need to send a message to a specific person.
To do that, you will have to insert the name of the person into the search box.
How can you do that?
You will need to use the `send_keys` method of the `search_bar` variable.
It is time for you to [google man](https://www.selenium.dev/documentation/webdriver/actions_api/keyboard/)
to find how to send keys to an element.


Now that you have sent the name of the person to the search bar, you will need to find the person in the list of contacts.
To do that, if you inputted the name of the person correctly, the person should be the first one in the list.
There are two ways of doing that, you can either use the `find_element` method, or 
simply send the `ENTER` key to the search bar. This will basically open the chat of the first person in the list.

### **Remember to wait for the element to appear**

Once the chat has been open, again, look for the message box element to be able to send a message.
Once you have found the element, you will need to send the message you want to send.
To do that, you will need to use the `send_keys` method of the element and press the `ENTER` key.
This will send the message to the person.
