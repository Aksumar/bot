#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def get_pizza_price(name):
    name = name[6:]
    for pizza in pizzas:
        if pizza['name'] == name:
            return pizza['price']
    return None

