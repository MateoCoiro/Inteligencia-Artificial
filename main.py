#@title Librerías a usar
import sys, os, re, random
import urllib, time, base64
import urllib.parse
import string
import requests
import numpy as np

from tensorflow import keras
from tensorflow.keras.models import Model
from tensorflow.keras.utils import plot_model
from keras.utils import to_categorical
from sklearn.model_selection import train_test_split

import tensorflow as tf
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
import math

from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

import os
import csv

import ipywidgets as widgets
from ipywidgets import Box, Layout
from IPython.display import clear_output
import random

print("hello")

#@title Extraer datos disponibles en la página

# funciones para manejar campos pelicula

def strbuscarEntre(text, key1, key2):
  return strbuscarEntreList(text, [key1], [key2])

def strbuscarEntreList(text, listkey1, listkey2):
 p1 = -1
 for key1 in listkey1:
  auxP1 = text.find(key1)
  if (auxP1 > -1) and ((p1 == -1) or (auxP1 < p1)):
    p1 = auxP1
 if p1 == -1:
  return ""
 else:
  p1 = p1+len(key1)
  p2 = -1
  for key2 in listkey2:
    auxP2 = text[p1:].find(key2)
    if (auxP2 > -1) and ((p2 == -1) or (auxP2 < p2)):
      p2 = auxP2
  if p2 == -1:
    return ""
  else:
    p2 = p1+p2
  return text[p1:p2]

def limpiar(text):
  if text is None:
    return ""
  else:
    text = text.replace(""", " ")
    text = text.replace("&", " & ")
    text = text.replace(" ", "")
    text = text.replace("\r\n", "")
    text = text.replace("  ", " ")
    text = text.replace("  ", " ")
    return text.strip()


class INSDParser:

 def __init__(self, baseURL="http://insd.swcombine.com/insd/", debug=False):
  self.__debug = debug
  self.__baseURL = baseURL
  self.__AttNames = ["Model", "Manufacturer", "Length", "Crew", "Troops", "Cargo Capacity", "Consumables", "Hyperdrive Multiplier", "Hyperdrive Backup", "Speed", "Hull", "Shields", "Special Features", "Weapons", "Onboard Craft"]
  print("\n** Parser de 'IMPERIAL NAVY SHIP DATABASE' incializado ** \n")

 def __getHTMLContent(self, url):
  return requests.get(url).text

 def extractSiteLinks(self, searchURL):
  # ejecuta y obtiene la página
  searchData = self.__getHTMLContent(searchURL)
  # extrae los links
  auxList = re.findall('
    """

df = pd.DataFrame.from_dict(navesList)

display( df )