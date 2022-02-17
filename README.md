EPSim: Energy Profile Similarity Maps
==============================================
[//]: # "[![DOI](https://zenodo.org/badge/381737392.svg)](https://zenodo.org/badge/latestdoi/381737392):"

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
python EPSim.py [-h] [-version] -i [FILENAMES] [-df DFILENAMES] [-nd ND] [-v VERB] [-r RUNMODE] [-lsfer | -thermo | -kinetic | -es | -tof | -all] [-T TEMP] [-pm PLOTMODE] [-ic IC] [-fc FC]
                [-rm RMARGIN] [-lm LMARGIN] [-np NPOINTS] [-d] [-is IMPUTER_STRAT] [-refill]
```

You can also execute:

```python 
python setup.py install
```

to install EPSim as a python module. Afterwards, you can call EPSim as:

```python 
python -m EPSim [-h] [-version] -i [FILENAMES] [-df DFILENAMES] [-nd ND] [-v VERB] [-r RUNMODE] [-lsfer | -thermo | -kinetic | -es | -tof | -all] [-T TEMP] [-pm PLOTMODE] [-ic IC] [-fc FC]
                [-rm RMARGIN] [-lm LMARGIN] [-np NPOINTS] [-d] [-is IMPUTER_STRAT] [-refill]
```

Options can be consulted using the `-h` flag in either case.

## Examples [↑](#examples)

The examples subdirectory contains a copious amount of tests which double as examples. Any of the data files can be run as:

```python
python EPSim.py -i [FILENAME]
```



```python
python epsim.py -i <datafile> -f [feature columns in base 0] -r <reaction energy> -s <number of reaction steps> -d <descriptor file> -c <desc column>
```

-i Name of the file containing the reaction energies for each catalyst. <br>
-f List of indices corresponding to the columns that contain the reaction energy of each step of the cycle. <br>
-r Reaction energy. <br>
-s Number of steps in the catalystic cycle. <br>
-d File containing the descriptor variable. <br>
-c index of the column containing the descriptor in the descriptor file. <br>

```python
python  epsim.py -i ./example\_data/mydata.txt -f 1,2,3,4,5,6 -r -30.738 -s 6 -d ./example\_data/descript.dat -c 1
```
Regarding format, EPSim.py expects headers for all columns. The first column must contain names/identifiers. Then, EPSim.py expects a number of columns with relative free energies for the species in the catalytic cycle (in order of appearance), and a final column whose header is "Product" containing the reaction energy.


---


