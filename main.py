#Importando API
from iqoptionapi_master import iqoptionapi
from iqoptionapi.stable_api import IQ_Option

#Importando demais bibliotecas
from tkinter import *
from datetime import datetime
from dateutil import tz

# Declarando variáveis
login = ''
password = ''


iq = IQ_Option(login, password)
