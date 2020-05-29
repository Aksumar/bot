#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def get_pizzas_by_ingradients(ingredients:list):
    hits = dict() # pizza['name'] -> No of ingredients found
    for pizza in pizzas:
        for addon in ingredients:
            if addon[:3] in pizza['contents']:
                if pizza['name'] in hits.keys():
                    hits[pizza['name']] += 1
                else:
                    hits[pizza['name']] = 1
    return sorted(hits.items(), key=lambda x: x[1])[-1]

