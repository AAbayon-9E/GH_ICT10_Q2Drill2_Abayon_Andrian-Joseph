# weather dictionary
from pyscript import display


Weather = {
    'Location':'Manila',
    'Temperature_c':'32',
    'Humidity':'78',
    'Condition':'sunny'
}

#DISPLAY TEMPERATURE ONLY
del Weather['Location']
del Weather['Humidity']
del Weather['Condition']

#Update condition to cloudy
Weather['Condition'] = 'cloudy'

#New key-value pair
Weather ['heat_index'] = '38'

# display
display((Weather), target='output')


#display temperature only
