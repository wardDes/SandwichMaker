import pyinputplus as pyip, time

costs = {
      'wheat': 0.20,
      'white': 0.10,
      'sourdough': 0.30,
      'tofu': 0.10,
      'turkey': 0.20,
      'chicken': 0.30,
      'ham': 0.40,
      'cheddar': 0.10,
      'swiss': 0.20,
      'mozzarella': 0.30,
      'mayo': 0.10,
      'mustard': 0.10,
      'lettuce': 0.10,
      'tomato': 0.20,
}
# wheat,ham,swiss,mayo,mustard,lettuce, tomato, = 0.2+0.4+0.2+-0.1+0.1+0.1+0.1= 1.2
# sourdough, chicken,mozzarella, mayo,mustard, tomato = 0.30+0.30+0.30+0.30 = 1.2

ordTot = 0.00
ordSndwichTot = 0.00
mtbrdchz= {}
condmnts ={}

while True:
   breadType = pyip.inputMenu(['wheat', 'white', 'sourdough'], 
   prompt="Enter the desired type of bread\n", numbered=True)
   #print(breadType, costs[breadType])
   ordSndwichTot += costs[breadType]
   mtbrdchz['bread']= breadType
   #print("{0:.2f}".format(ordSndwichTot))
   print()
   meatType = pyip.inputMenu(['chicken', 'turkey','ham','tofu'],
   prompt="Enter the type of meat for the sandwich\n", numbered=True)
   #print(meatType, costs[meatType])
   mtbrdchz['meat']= meatType
   ordSndwichTot += costs[meatType]
   #print("{0:.2f}".format(ordSndwichTot))
   print()
   optCheese = pyip.inputYesNo("Would you like cheese on you sandwich?")
   if optCheese =='yes':
      cheeseType = pyip.inputMenu(['cheddar','swiss','mozzarella'], numbered=True)
      mtbrdchz['cheese']= cheeseType
      #print(cheeseType, costs[cheeseType])
      ordSndwichTot += costs[cheeseType]
      ordSndwichTot = round(ordSndwichTot, 2)
      #print("{0:.2f}".format(ordSndwichTot))
   print()
   optMayo = pyip.inputYesNo("Would you like mayo on you sandwich?")
   if optMayo == 'yes':
      # add 'mayo' to complete sandwich dictionary or list
      print('mayo added')
      ordSndwichTot += costs['mayo']
      condmnts['mayo']=True
   print()
   optMustard = pyip.inputYesNo("Would you like mustard on you sandwich?")
   if optMustard == 'yes':
      # add 'mayo' to complete sandwich dictionary or list
      print('mustard added')
      ordSndwichTot += costs['mustard']
      condmnts['mustard']=True
   print()
   optLettuce = pyip.inputYesNo("Would you like lettuce on you sandwich?")
   if optLettuce == 'yes':
      # add 'mayo' to complete sandwich dictionary or list
      print('lettuce added')
      ordSndwichTot += costs['lettuce']
      condmnts['lettuce']=True
   print()
   optTomato = pyip.inputYesNo("Would you like tomato on you sandwich?")
   if optTomato == 'yes':
      # add 'mayo' to complete sandwich dictionary or list
      print('tomato added')
      ordSndwichTot += costs['tomato']
      condmnts['tomato']=True
   print()
   numSndwchs = pyip.inputNum('Enter number of sandwiches of this type desired: ',
   min=1, lessThan=6)
   #print("{0:.2f}".format(ordSndwichTot))
   print()
   print('Your sandwich order:')

   for i in mtbrdchz:
      print(i, ":", mtbrdchz.get(i))
   for i in condmnts:
      print(i, ":", condmnts.get(i))
   print()
   ordSubmit = pyip.inputYesNo('Confirm sandwich ingredients correct: ')
   if ordSubmit == 'yes':
      ordSndwichTot *= numSndwchs
      ordTot = ordSndwichTot
      print("Total: ${0:.2f}".format(ordTot))
      break
   else:
      print('Please resubmit your sandwich order.')
      mtbrdchz.clear()
      condmnts.clear()
      print()
      time.sleep(2)
      continue
