EPSim
============
Energy Profile Similarity Maps

EPSim is a python program that allows computing the similarity between the Sabatier's ideal reaction energies profile for a given catalytic cycle and the energy profile of potential catalysts. The computed similarities are then locally saved and automatically plotted as a function of a chemically and physically well-defined descriptor.


Requirements
------------
* Python_ 3.5 or later
* Anaconda_ 3

Installation
------------
Add ``~/EPSim`` to your $PYTHONPATH environment variable.

Usage:
-----
epsim.py -i <datafile> -f [feature columns in base 0] -r <reaction energy> -s <number of reaction steps> -d <descriptor file> -c <desc column>')

-i Name of the file containing the reaction energies for each catalyst.
-f List of indices corresponding to the columns that contain the reaction energy of each step of the cycle.
-r Reaction energy.
-s Number of steps in the catalystic cycle.
-d File containing the descriptor variable.
-c index of the column containing the descriptor in the descriptor file.



Example
-------
python  epsim.py -i ./example\_data/mydata.txt -f 1,2,3,4,5,6 -r -30.738 -s 6 -d ./example\_data/descript.dat -c 1


.. _Python: http://www.python.org/
.. _Anaconda : https://www.anaconda.com/

