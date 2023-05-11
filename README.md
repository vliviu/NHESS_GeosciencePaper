# NHESS_GeosciencePaper
This code certifies the accuracy of regression methods using Artificial Intelligence
first published in our paper:
"An attempt to model the relationship between MMI attenuation and engineering ground-motion parameters 
using artificial neural networks and genetic algorithms"  
in Nat. Hazards Earth Syst. Sci., 10, 2527–2537, 2010

Html page is here, from which you can check it:
https://nhess.copernicus.org/articles/10/2527/2010/nhess-10-2527-2010.pdf

1) The first method "LinearRegression.py" retrieves exactly the coefficients from the MMI equation (9):
MMI = 8.824+0.417M −7.960logR+0.380PGA +1.105Ia −0.551CAV
This simple python scripts replaces all the work described in the paper by our GA-ANN combination.

The 'data.csv' is the actual data from Table I in the paper and should be placed in a sub-folder called 'data'.

2) The 2nd program  "nonlinearRegression.py" which uses keras with tensorflow backend verifies in an other the accuracy
of our calculus, and it gives a RMSE error of approx. 0.75 %.

The requirements.txt file specifies Python (3.9/3/10) packages that one should install (using conda/pip commands).

