import sys, getopt
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

def compute_sabatier(rxn_nrj,steps):
    sab = np.zeros(steps)
    sab[:] = rxn_nrj/steps
    return sab

def load_features(filename, cols):
    return np.loadtxt(filename,usecols = cols)

def stdize(X):
    """ x_std = (x - mu) / sigma """

    mu = np.mean(X, axis=0)
    sigma = np.std(X, axis=0)

    X -= mu
    X /= sigma
    return X

def distance(X):
    """ Compute Pairwise Distance Matrix
    with Euclidean norm 
    dist(x, y) = sqrt(dot(x, x) - 2 * dot(x, y) + dot(y, y))
    """

    X2 = np.sum(X**2, axis=1)[:,np.newaxis]
    Y2 = np.sum(X**2, axis=1)
    XY = -2 * np.dot(X,X.T)
    dist = X2+Y2+XY
    
    # Cure floating point round up  errors
    np.maximum(dist, 0, out=dist)
    np.fill_diagonal(dist, 0)

    return np.sqrt(dist, out=dist)


def main(argv):
    filename = ''
    try:
        opts, args = getopt.getopt(argv,"hi:f:r:s:d:c:",["ifile=","fcol=","rxn=","stp=","desc","dcol"])
    except getopt.GetoptError:
        print('epsim.py -i <datafile> -f [feature columns in base 0] -r <reaction energy> -s <number of reaction steps> -d <descriptor file> -c <desc column>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('epsim.py -i <datafile> -f [feature columns in base 0] -r <reaction energy> -s <number of reaction steps> -d <descriptor file> -c <desc column>')
            print("e.g. python  epsim.py -i mydata.txt -f 1,2,3,4,5,6 -r -30.738 -s 6 -d descript.dat -c 1 ")
            sys.exit()
        elif opt in ("-i", "--ifile"):
            filename = arg
        elif opt in ("-f", "--fcol"):
            cols = tuple(np.array(arg.split(','),dtype=int))
        elif opt in ("-r", "--rxn"):
            rxn_nrj = float(arg)
        elif opt in ("-s", "--stp"):
            steps = int(arg)
        elif opt in ("-d", "--desc"):
            desc_file = arg
        elif opt in ("-c", "--dcol"):
            desc_col = int(arg)

    # Sanity check
    if steps != len(cols):
        print("The number of features must be equal to the reaction steps")
        sys.exit(2)

    sab = compute_sabatier(rxn_nrj,steps)
    save = True
    feat = load_features(filename, cols)
    feat = np.vstack((feat,sab))
    feat_STD = stdize(feat)
    dist = distance(feat_STD)[-1,:]

    if save:
        np.save('sim', dist)

    X = np.loadtxt(desc_file, usecols = desc_col)
    Y = 1 - (dist/np.linalg.norm(dist))

    fig, ax = plt.subplots()

    ax.axes.get_xaxis().set_visible(True)
    ax.axes.get_yaxis().set_visible(False)

    cax = ax.scatter(X,Y,s=10)
    plt.xlabel(r'Descriptor [kcal/mol]')
    plt.savefig("epsim.png")
    plt.show()
    return

if __name__ == "__main__":
    main(sys.argv[1:])
