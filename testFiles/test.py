import operator    
parsedResult = {'paper': 0.45938486, 'cardboard': 0.42542723, 'plastic': 0.06604799, 'metal': 0.036904056, 'glass': 0.012235973}
material =  max(parsedResult.items(), key=operator.itemgetter(1))[0]
print(material)
