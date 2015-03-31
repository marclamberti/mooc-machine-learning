'''
Mini project for the Machine Learning Mooc Week 1
This project uses Linear Regression with Gradien Descent and Normal equation
to predict the price of an appartment which will we want to sell through www.agence-centre.fr
'''

import mechanize

APPARTMENT_FOR_SELL_URL = 'http://www.agence-centre.fr/type_bien/3-33/a-vendre.html'

# Initilize mechanize
br = mechanize.Browser()
br.set_handle_robots(False)

# Open the url where the appartments are for sell
response = br.open(APPARTMENT_FOR_SELL_URL)
content = response.read()

print content