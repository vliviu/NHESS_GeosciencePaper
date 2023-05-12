# NHESS_GeosciencePaper
This code and the paper  given below certifies the accuracy of discovering formulas using regression methods either linear or neliniar, using Artificial Intelligence
between MMI ( modified Mercalli intensity) and related measurements:

  o PGA  peak ground acceleration

  o and PGV  peak ground velocity
  
  o Arias intensity (Ia),
  
  o acceleration response spectrum (Sa), and
  
  o cumulative absolute velocity (CAV).
  
 Our paper (me, L. Vladutu & G. Akis-Tselentis as authors) first published these formulas discovered by regression in:
 
"An attempt to model the relationship between MMI attenuation and engineering ground-motion parameters 
using artificial neural networks and genetic algorithms"  
in Nat. Hazards Earth Syst. Sci., 10, 2527–2537, 2010

Html page is here, from which you can check it:
https://nhess.copernicus.org/articles/10/2527/2010/nhess-10-2527-2010.pdf

1) The first method "LinearRegression.py" retrieves exactly the coefficients from the MMI equation (9):
MMI = 8.824+0.417M −7.960logR+0.380PGA +1.105Ia −0.551CAV.


This simple python scripts replaces all the work described in the paper by our GA-ANN combination.

The 'data.csv' is the actual data from Table I in the paper and should be placed in a sub-folder called 'data'.

2) The 2nd program  "nonlinearRegression.py" which uses keras with tensorflow backend verifies in an other way the accuracy
of our calculus, and it discover a nonlinear dependencies between MMI and measurements (given above) with a RMSE error of approx. 0.75 %.

The requirements.txt file specifies Python (3.9/3.10) packages that one should install (using conda/pip commands).

P.S. I've also added the jupyter notebook source 'nonlinearRegression.ipynb'
 
 and cleanPyCode_generatedFromJupyter.py which takes a Python source code generated from within jupyter with the command
 
!jupyter notebook --to script nonlinearRegression.ipynb

and eliminates all the "dirt" i.e. lines like # [],  #[1]: .... a.s.o. and surrounding lines and generates a clean functional python source (in this case cleaned_nonlinearRegression.py).

HTH !

Citation:
________
If you use this code or the results published in the paper, please cite our work, with details given above.

License:
________
The code is released under the MIT license.


