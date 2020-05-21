#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json
import requests
from bs4 import BeautifulSoup


# In[2]:


pizzas_html = requests.get('https://www.vivatpizza.ru/menu/pizza?getAllSubgoups=true').text
burgers_html = requests.get('https://www.vivatpizza.ru/menu/burgery-new').text
soups_html = requests.get('https://www.vivatpizza.ru/menu/soup').text
salads_html = requests.get('https://www.vivatpizza.ru/menu/salad').text
side_dishes_html = requests.get('https://www.vivatpizza.ru/menu/hot_dishes').text
dishes_html = requests.get('https://www.vivatpizza.ru/menu/hot_food').text


# In[15]:


class Dish:
    def __str__(self):
        return str(self.__dict__)
    # цена - от n рублей, не ровно n!!


class DishEncoder(json.JSONEncoder):
    def default(self, o):
        return o.__dict__

dishes = []


# In[16]:


ads = BeautifulSoup(pizzas_html).find_all('div', class_='item')
print(len(ads))
for ad in ads:
    try:
        name = ad.find('div', class_='summary-header').find('a', class_='product-link-short').text
        contents = ad.find('div', class_='summary-desc').text
        price = ad.find('span', class_='total-mods-price').text
#         image_ref = ad.find('img', class_='product-img').src
        dish = Dish()
        dish.name = name
        dish.contents = contents
        dish.price = price
        dish.category = 'pizza_name'
#         dish.img_ref = image_ref
        dishes.append(dish)
    except TypeError as e:
        print('parsing error', e)
for dish in dishes:
    print(dish.name)


# In[6]:


ads = BeautifulSoup(burgers_html).find_all('div', class_='inner')
for ad in ads:
    try:
        name = ad.find('div', class_='summary-header').find('h3', class_='title').text
        contents = ad.find('div', class_='item-description').text
        weight = ad.find('div', class_='summary-header').find('p', class_='weight').text
        price = ad.find('span', class_='product-price').text
        dish = Dish()
        dish.name = name
        dish.contents = contents
        dish.weight = weight
        dish.price = price
        dish.category = 'burger_name'
        dishes.append(dish)
    except TypeError as e:
        print('parsing error', e)
print(len(dishes))


# In[7]:


ads = BeautifulSoup(soups_html).find_all('div', class_='inner')
for ad in ads:
    try:
        name = ad.find('div', class_='summary-header').find('h3', class_='title').text
        contents = ad.find('div', class_='item-description').text
        weight = ad.find('div', class_='summary-header').find('p', class_='weight').text
        price = ad.find('span', class_='product-price').text
        dish = Dish()
        dish.name = name
        dish.contents = contents
        dish.weight = weight
        dish.price = price
        dish.category = 'soup_name'
        dishes.append(dish)
    except TypeError as e:
        print('parsing error', e)
for dish in dishes:
    print(dish if dish.category=='soup' else "")


# In[8]:


ads = BeautifulSoup(salads_html).find_all('div', class_='inner')
for ad in ads:
    try:
        name = ad.find('div', class_='summary-header').find('h3', class_='title').text
        try:
            contents = ad.find('div', class_='item-description').text
        except AttributeError:
            contents = 'Описание недоступно'
        weight = ad.find('div', class_='summary-header').find('p', class_='weight').text
        price = ad.find('span', class_='product-price').text
        dish = Dish()
        dish.name = name
        dish.contents = contents
        dish.weight = weight
        dish.price = price
        dish.category = 'salad_name'
        dishes.append(dish)
    except TypeError as e:
        print('parsing error', e)
for dish in dishes:
    if dish.category=='salad':
        print(dish)


# In[19]:


ads = BeautifulSoup(side_dishes_html).find_all('div', class_='inner')
for ad in ads:
    try:
        name = ad.find('div', class_='summary-header').find('h3', class_='title').text
        try:
            contents = ad.find('div', class_='item-description').text
        except AttributeError:
            contents = 'Описание недоступно'
        weight = ad.find('div', class_='summary-header').find('p', class_='weight').text
        price = ad.find('span', class_='product-price').text
        dish = Dish()
        dish.name = name
        dish.contents = contents
        dish.weight = weight
        dish.price = price
        dish.category = 'hot_side_dishes'
        dishes.append(dish)
    except TypeError as e:
        print('parsing error', e)
for dish in dishes:
    if dish.category=='hot_side_dishes':
        print(dish)


# In[21]:


ads = BeautifulSoup(dishes_html).find_all('div', class_='inner')
for ad in ads:
    try:
        name = ad.find('div', class_='summary-header').find('h3', class_='title').text
        try:
            contents = ad.find('div', class_='item-description').text
        except AttributeError:
            contents = 'Описание недоступно'
        weight = ad.find('div', class_='summary-header').find('p', class_='weight').text
        price = ad.find('span', class_='product-price').text
        dish = Dish()
        dish.name = name
        dish.contents = contents
        dish.weight = weight
        dish.price = price
        dish.category = 'main_dishes'
        dishes.append(dish)
    except TypeError as e:
        print('parsing error', e)
for dish in dishes:
    if dish.category=='main_dishes':
        print(dish)


# In[32]:


for dish in dishes:
    print(dish)


# In[ ]:




