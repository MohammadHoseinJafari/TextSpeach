#Task 1-1

import numpy as np

# for calculate normal randomly selection (probabilities without distributions)
def Uinform(Names):
    return np.random.choice(Names)

# for calculate distributed randomly selection (probabilities with distributions)
def Distributed(Names,Distributions):
    # at this section of code i should normalizations Distributions list ( sum(Dist) == 1 or close to 1 )
    return np.random.choice(Names, p = Distributions)

# function for get name and distribute list and call above functions
def implementation():
    Names = []
    Distributions = []

    while True:
      _name  = str(input('Enter your Name : '))
      # condition to stop the while loop
      if _name == "" :
        break
      _alpha = float(input('Enter your Distributions : ')) # float Data Type
      Names.append(_name)
      Distributions.append(_alpha)

    print("uniform probability :",Uinform(Names))
    print("Distributed probability :",Distributed(Names,Distributions))

#call implementation function
implementation()