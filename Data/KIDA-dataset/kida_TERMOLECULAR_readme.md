12-10-2023 16:10:59

Number of reactions in the downloaded network: 80

Format of the file: 3(a11),1x,6(a11),1x,3(e10.3,1x),2(e9.2),i7,2x,3(e10.3,1x),2(e9.2),i7,x2,e10.3,i7,i7,i3,i6,i2,i3
The different columns are:
Columns 1 to 3: Reactants 
Columns 4 to 9: Products 
Columns 10 to 15: alpha, beta, gamma, F, g and Formula number to compute k0
Columns 16 to 21: alpha, beta, gamma, F, g and Formula number to compute kinf
Column 22: Fc
Columns 23 and 24: Tmin and Tmax 
Columns 25 to last:  General Formula, Number, Numbers_of_(alpha, beta, gamma), Recommendation

-> alpha, beta, gamma are the parameters to compute the rate coefficients. The formula depends on the type of reaction. See https://kida.astrochem-tools.org/help.html

-> F is the uncertainty factor on the rate coefficient. g is the temperature dependence of this uncertainty factor. Type of uncertainty : lognormal (logn) , normal (norm) , loguniform (logu) , uniform (unit). (See https://kida.astrochem-tools.org/help.html)

-> Itype is the type of reaction (See https://kida.astrochem-tools.org/help.html)

-> Trange is the range of temperatures the rate coefficient is valid. Extrapolations outside this range has to be done with caution.. When we do not have information on Trange, default values are used: -9999,9999.

-> Formula is a number that referes to the formula needed to compute the rate coefficient of the reaction. 
3: Kooij 
6: 3-body
Correspondances of the names to the mathematical expression can be found at this address: https://kida.astrochem-tools.org/help.html


-> Number is the number of the reaction in the downloaded network.

-> Numbers of (alpha, beta, gamma) is the number of (alpha, beta, gamma) in the downloaded network when several values are present in KIDA. When a user selects a range of temperature and that several rate coefficients in KIDA can be in agreement with his/her search, all data will be included in the network. We then expect the user to choose one of the values. If the reactions are particularly important, we advise the user to contact KIDA to get advises. 
These reactions that are present more than once in the network are listed below. 

-> Recommendation is the recommendation given by experts in KIDA. 
1 means that there is no recommendation (experts have not looked at the data). 
2 means that the value has been validated by experts over the Trange
3 means that it is the recommended value over Trange.

----------------------------------------------------------------------------------------------------------------------------------------
As a result of your search, we have found 1 reactions with more than one rate coefficient in KIDA and no clear recommendation in respect with the range of temperature you asked. 
These reactions have the following numbers in the downloaded network :

undefined
