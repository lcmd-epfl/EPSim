EPSim: Energy Profile Similarity Maps
==============================================

![epsim logo](./images/epsim_logo.png)

## Contents
* [About](#about-)
* [Install](#install-)
* [Examples](#examples-)

## About [↑](#about)


EPSim is a python program that allows computing the similarity between the Sabatier's ideal reaction energies profile for a given catalytic cycle and the energy profile of potential catalysts. The computed similarities are then locally saved and automatically plotted as a function of a chemically and physically well-defined descriptor.

The code runs on pure python with minimal dependencies: 
- `numpy`
- `matplotlib`
- `pandas`


## Install [↑](#install)

Download and add EPSim.py to your path. No strings attached. Run as:

```python
python epsim.py -i <datafile> -f [feature columns in base 0] -r <reaction energy> -s <number of reaction steps> -d <descriptor file> -c <desc column>
```

-i Name of the file containing the reaction energies for each catalyst. <br>
-f List of indices corresponding to the columns that contain the reaction energy of each step of the cycle. <br>
-r Reaction energy. <br>
-s Number of steps in the catalystic cycle. <br>
-d File containing the descriptor variable. <br>
-c index of the column containing the descriptor in the descriptor file. <br>

## Examples [↑](#examples)

Example input can be found in the example_data directory. Run as: 
```python
python  epsim.py -i mydata.txt -f 1,2,3,4,5,6 -r -30.738 -s 6 -d descript.dat -c 1
```

---


