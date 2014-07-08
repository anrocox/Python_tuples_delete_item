#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 7, 2014

@author: anroco

How to remove an item from a tuple in python?

¿Como remover un elemento de una tupla en python?
'''

#create a tuple
tupla = 's', 'r', 't', 'f', 'q', 'v'
print (tupla)

#tuples are immutable, so you can not remove elements
#using merge of tuples with the + operator to remove an item, create new tuple.
tupla = tupla[:2] + tupla[3:]
print(tupla)

#converting the tuple to list
lista = list(tupla)
#use different ways to remove an item of the list
lista.remove('q')
#converting the tuple to list
tupla = tuple(lista)
print(tupla)
