12-10-2023 16:10:15

Five files are generated for surface reactions:

"Surface reactions file" contains the reactions (reactants + products) with branching ratios for the channels. 298 reactions were found.
Format is: 3(a11),1x,5(a11),1x,f5.2,e9.2,1x,12a,2(i2),i3
Columns 1 to 3: Reactants
Columns 4 to 9: Products
Column 10: Branching ratio
Column 11: uncertainty on the branching ratio
Column 12: Type of surface (this column is mostly blank for the moment)
Columns 13 to last:  Number, Numbers_of_data, Recommendation

"Surface energy activation" file contains activation barriers for surface reactions. 72 data were found.
Format is: 3(a11),1x,5(a11),1x,3(e11.3), 1x,12a,2(i2),i3
Columns 1 to 3: Reactants
Columns 4 to 9: Products
Columns 10 to 12: pre-exponential, activation barrier and uncertainty on the activation barrier.
Column 13: Type of surface (this column is mostly blank for the moment)
Columns 14 to last:  Number, Numbers_of_data, Recommendation

"Surface reaction barrier" file contains the barrier width for surface reactions with activation energies. 0 data were found.
Columns 1 to 3: Reactants
Columns 4 to 9: Products
Columns 10 : barrier width
Column 11: Type of surface (this column is mostly blank for the moment)
Columns 12 to last:  Number, Numbers_of_data, Recommendation


"Desorption energy" file contains the species desorption energies. 214 data were found.
Format is: a11,e10.3,e9.2,1x,e10.3,e9.2,i2,a9,i2
Column 1: species name
Columns 2 and 3: pre-exponential factor and its uncertainty
Columns 4 and 5:  desorption energy and its uncertainty
Column 6: Order of the desorption
Column 7: Type of surface
Column 8: Recommendation

"Diffusion energy" file contains the species diffusion energies. 8 data were found.
Format is: a11,e10.3,e9.2,1x,e10.3,e9.2,a9,a9,i2
Column 1: species name
Columns 2 and 3: pre-exponential factor and its uncertainty
Columns 4 and 5:  diffusion energy and its uncertainty
Column 6: Type of surface
Column 7: Type of diffusion
Column 8: Recommendation
-> Number is the number of the reaction in the downloaded network.

-> Numbers of data is the number of data in the downloaded network when several values are present in KIDA. When a user selects a range of temperature and that several rate coefficients in KIDA can be in agreement with his/her search, all data will be included in the network. We then expect the user to choose one of the values. If the reactions are particularly important, we advise the user to contact KIDA to get advises. 
These reactions that are present more than once in the network are listed below. 

-> Recommendation is the recommendation given by experts in KIDA. 
1 means that there is no recommendation (experts have not looked at the data). 
2 means that the value has been validated by experts over the Trange
3 means that it is the recommended value over Trange.