#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def get_pizza_price(name, dough, size):
    name = name[6:]
    if name == 'жульен':
        if dough == 'тонкое' and size == 20: return 217
        elif if dough == 'тонкое' and size == 31: return 397
        elif if dough == 'тонкое' and size == 36: return 579
        elif if dough == 'толстое' and size == 20: return 277
        elif if dough == 'толстое' and size == 31: return 527
        elif if dough == 'толстое' and size == 36: return 600
        else: return 0
    elif name == 'карри с цыпленком':
        if dough == 'тонкое' and size == 20: return 387
        elif if dough == 'тонкое' and size == 31: return 637
        elif if dough == 'тонкое' and size == 36: return 797
        elif if dough == 'толстое' and size == 20: return 395
        elif if dough == 'толстое' and size == 31: return 675
        elif if dough == 'толстое' and size == 36: return 835
        else: return 0
    elif name == 'дижонская':
        if dough == 'тонкое' and size == 20: return 383
        elif if dough == 'тонкое' and size == 31: return 617
        elif if dough == 'тонкое' and size == 36: return 797
        elif if dough == 'толстое' and size == 20: return 397
        elif if dough == 'толстое' and size == 31: return 657
        elif if dough == 'толстое' and size == 36: return 817
        else: return 0
    elif name == 'фермерская':
        if dough == 'тонкое' and size == 20: return 375
        elif if dough == 'тонкое' and size == 31: return 617
        elif if dough == 'тонкое' and size == 36: return 797
        elif if dough == 'толстое' and size == 20: return 397
        elif if dough == 'толстое' and size == 31: return 655
        elif if dough == 'толстое' and size == 36: return 815
        else: return 0
    
    elif name == 'аджапсандал с ягненком':
        if dough == 'тонкое' and size == 20: return 387
        elif if dough == 'тонкое' and size == 31: return 695
        elif if dough == 'тонкое' and size == 36: return 957
        elif if dough == 'толстое' and size == 20: return 397
        elif if dough == 'толстое' and size == 31: return 797
        elif if dough == 'толстое' and size == 36: return 997
        else: return 0
    elif name == 'кальцоне охотничья':
        return 179
    elif name == 'кальцоне пепперони':
        return 179
    elif name == 'кальцоне французская':
        return 179
    
    elif name == 'кальцоне суприм':
        return 179
    elif name == 'морская делюкс':
        if dough == 'тонкое' and size == 20: return 389
        elif if dough == 'тонкое' and size == 31: return 799
        elif if dough == 'тонкое' and size == 36: return 1027
        elif if dough == 'толстое' and size == 20: return 397
        elif if dough == 'толстое' and size == 31: return 849
        elif if dough == 'толстое' and size == 36: return 1147
        else: return 0
    elif name == 'французская':
        if dough == 'тонкое' and size == 20: return 327
        elif if dough == 'тонкое' and size == 31: return 587
        elif if dough == 'тонкое' and size == 36: return 745
        elif if dough == 'толстое' and size == 20: return 387
        elif if dough == 'толстое' and size == 31: return 695
        elif if dough == 'толстое' and size == 36: return 889
        else: return 0
    elif name == 'драконий хвост':
        if dough == 'тонкое' and size == 20: return 329
        elif if dough == 'тонкое' and size == 31: return 687
        elif if dough == 'тонкое' and size == 36: return 897
        elif if dough == 'толстое' and size == 20: return 359
        elif if dough == 'толстое' and size == 31: return 759
        elif if dough == 'толстое' and size == 36: return 935
        else: return 0
        
    elif name == 'мексиканская':
        if dough == 'тонкое' and size == 20: return 315
        elif if dough == 'тонкое' and size == 31: return 537
        elif if dough == 'тонкое' and size == 36: return 915
        elif if dough == 'толстое' and size == 20: return 377
        elif if dough == 'толстое' and size == 31: return 717
        elif if dough == 'толстое' and size == 36: return 947
        else: return 0
    elif name == 'грибная':
        if dough == 'тонкое' and size == 20: return 295
        elif if dough == 'тонкое' and size == 31: return 495
        elif if dough == 'тонкое' and size == 36: return 735
        elif if dough == 'толстое' and size == 20: return 315
        elif if dough == 'толстое' and size == 31: return 615
        elif if dough == 'толстое' and size == 36: return 799
        else: return 0
    elif name == 'охотничья':
        if dough == 'тонкое' and size == 20: return 315
        elif if dough == 'тонкое' and size == 31: return 575
        elif if dough == 'тонкое' and size == 36: return 767
        elif if dough == 'толстое' and size == 20: return 395
        elif if dough == 'толстое' and size == 31: return 715
        elif if dough == 'толстое' and size == 36: return 899
        else: return 0
    elif name == 'пепперони':
        if dough == 'тонкое' and size == 20: return 329
        elif if dough == 'тонкое' and size == 31: return 547
        elif if dough == 'тонкое' and size == 36: return 727
        elif if dough == 'толстое' and size == 20: return 369
        elif if dough == 'толстое' and size == 31: return 599
        elif if dough == 'толстое' and size == 36: return 787
        else: return 0
        
    elif name == 'цезарь':
        if dough == 'тонкое' and size == 20: return 399
        elif if dough == 'тонкое' and size == 31: return 725
        elif if dough == 'тонкое' and size == 36: return 967
        elif if dough == 'толстое' and size == 20: return 419
        elif if dough == 'толстое' and size == 31: return 815
        elif if dough == 'толстое' and size == 36: return 999
        else: return 0
    elif name == 'суприм':
        if dough == 'тонкое' and size == 20: return 375
        elif if dough == 'тонкое' and size == 31: return 635
        elif if dough == 'тонкое' and size == 36: return 837
        elif if dough == 'толстое' and size == 20: return 395
        elif if dough == 'толстое' and size == 31: return 787
        elif if dough == 'толстое' and size == 36: return 999
        else: return 0
    elif name == 'классика':
        if dough == 'тонкое' and size == 20: return 319
        elif if dough == 'тонкое' and size == 31: return 535
        elif if dough == 'тонкое' and size == 36: return 717
        elif if dough == 'толстое' and size == 20: return 345
        elif if dough == 'толстое' and size == 31: return 617
        elif if dough == 'толстое' and size == 36: return 815
        else: return 0
    elif name == 'сальмоне':
        if dough == 'тонкое' and size == 20: return 417
        elif if dough == 'тонкое' and size == 31: return 955
        elif if dough == 'тонкое' and size == 36: return 1117
        elif if dough == 'толстое' and size == 20: return 515
        elif if dough == 'толстое' and size == 31: return 1015
        elif if dough == 'толстое' and size == 36: return 1415
        else: return 0
        
    elif name == 'гавайская':
        if dough == 'тонкое' and size == 20: return 299
        elif if dough == 'тонкое' and size == 31: return 569
        elif if dough == 'тонкое' and size == 36: return 689
        elif if dough == 'толстое' and size == 20: return 367
        elif if dough == 'толстое' and size == 31: return 657
        elif if dough == 'толстое' and size == 36: return 827
        else: return 0
    elif name == 'мясная делюкс':
        if dough == 'тонкое' and size == 20: return 357
        elif if dough == 'тонкое' and size == 31: return 637
        elif if dough == 'тонкое' and size == 36: return 787
        elif if dough == 'толстое' and size == 20: return 375
        elif if dough == 'толстое' and size == 31: return 687
        elif if dough == 'толстое' and size == 36: return 847
        else: return 0
    elif name == 'маргарита':
        if dough == 'тонкое' and size == 20: return 279
        elif if dough == 'тонкое' and size == 31: return 499
        elif if dough == 'тонкое' and size == 36: return 587
        elif if dough == 'толстое' and size == 20: return 325
        elif if dough == 'толстое' and size == 31: return 515
        elif if dough == 'толстое' and size == 36: return 699
        else: return 0
    elif name == 'строганофф':
        if dough == 'тонкое' and size == 20: return 399
        elif if dough == 'тонкое' and size == 31: return 717
        elif if dough == 'тонкое' and size == 36: return 967
        elif if dough == 'толстое' and size == 20: return 447
        elif if dough == 'толстое' and size == 31: return 877
        elif if dough == 'толстое' and size == 36: return 999
        else: return 0
    
    elif name == '4 сыра':
        if dough == 'тонкое' and size == 20: return 317
        elif if dough == 'тонкое' and size == 31: return 627
        elif if dough == 'тонкое' and size == 36: return 757
        elif if dough == 'толстое' and size == 20: return 387
        elif if dough == 'толстое' and size == 31: return 657
        elif if dough == 'толстое' and size == 36: return 847
        else: return 0
    elif name == 'закрытая мясная':
        return 1087
    elif name == 'закрытая куриная':
        return 1057
    elif name == 'закрытая суприм':
        return 1057

