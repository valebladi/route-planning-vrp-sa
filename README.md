# Multiple MURMEL route planning

The introduced algorithm generates a route optimizing energy consumption of multiple service robots collaborating with a mobile depot, called 'mothership'. It is a variant of the vehicle routing problem (VRP). The algorithm is based on simulated annealing, using the nearest neighbor heuristic or sweep heuristic to generate an initial solution.

More parts of the paper are stored at
[Tubcloud 1](https://tubcloud.tu-berlin.de/apps/files/?dir=/Shared/MURMEL%40Cloud/00_Studentische_Arbeiten/42_Springer%20Paper_CooperativeDecisionMaking),
[Tubcloud 2](https://tubcloud.tu-berlin.de/apps/files/?dir=/Shared/MURMEL%40Cloud/00_Studentische_Arbeiten/99_Umland/SHK/Paper%20Route%20Planning) and
[Google Docs](https://docs.google.com/document/d/1iZD63-35Do6MSJe9J0OHxx0cQL0RzMivoUCvUhkGyhQ/edit?usp=sharing).

## Running requirements

This code is written in Python 3. To run the code, the libraries numpy, matplotlib, argparse, pandas, joypy and seaborn need to be installed. The libraries can be fetched with the python package manager:

```
sudo apt install python3-pip
pip3 install numpy matplotlib argparse pandas seaborn joypy
```

The code is tested under Ubuntu 20.04 with python 3.8.


## Execute files

### Route planning

`solver.py` executes the planning algorithm. Different command line arguments can be set to modify output, algorithm parameters and the example problem. Try for example:

```
python3 solver.py 
python3 solver.py --help
python3 solver.py --file berlin52 --debug OFF --show_gui STEPS --iterations 10000 --temperature_maximum 50 --temperature_minimum 0.01 --initial SWEEP

```

These command line arguments can be used:

* `--file` Filename of TSP example file, which is stored at the folder `example_problems`. Already supplied example files: `berlin52`, `ch130`, `ch150`, `eil76`, `kroD100`, `monbijou-james-simon` and `thesis1`.
* `--debug` Defines the amount of command line debugging messages. Options: `OFF`, `MIN` and `FULL`.
* `--initial` Chooses the initial solution strategy. Options: `NEARESTNEIGHBOR` and `SWEEP`.
* `--operator_weights` Defines the weights for the permutation operators. It will be normalized to the sum 1, to be a valid probability distribution. Usage: `weight_two_opt weight_relocate weight_global_relocate weight_global_exchange`.
* `--iterations` Defines the number of iterations per simulated annealing run. Attention: runtime increases approximately linearly with the number of iterations. Options: `[positive integer value]`.
* `--n_murmels` Defines the number MURMEL robots. Options: `[positive integer value]`.
* `--murmel_capacity` Defines the number of visited dustbins, until the next mothership stop is required. Options: `[positive integer value]`.
* `--show_gui` Creates a GUI which shows route, cost and temperature at the end (`SOLUTION`) or over time (`STEPS`). If the GUI is enabled, shown results are saved as `.png` and `.pdf` images at the folder `figures`. Options: `OFF`, `SOLUTION` and `STEPS`.
* `--draw_changes` Visualizes the last changed edges as dashed purple lines, if true and GUI is enabled. Options: `True` and `False`.
* `--temperature_maximum` Sets the maximum annealing temperature. The algorithm uses a geometric cooling schedule. Hence, the maximum temperature is equal to the initial temperature. Options: `[positive float value]`.
* `--temperature_minimum` Sets the minimum annealing temperature. Should be lower than temperature_maximum. Options: `[positive float value]`.

The example `monbijou-james-simon` offers distances on the path network (from [Gupta, Kremer]) which are used at the cost function. Remove `monbijou-james-simon_distances.csv` in the folder `example_problems` to use linear geographic distances.

### Benchmarking

`run_tests.sh` runs several tests in queue. It uses solver.py and passes the options via command line interface. The required parameter set is defined in `run_tests.sh`. The benchmark script can be executed without options:
```
./run_tests.sh 

```

### Visualisation

`plot_results.py` does statistical evaluation using included benchmark results at the folder `data` and shows the results in heatmaps and histograms. It can be called using:
```
python3 plot_results.py

```

The shown results are saved as `.png` and `.pdf` images at the folder `figures`.

## Known problems

* Routes are sometimes inequally devided between n MURMEL's. (Example: berlin52 and n_murmels = 10; we get local tour lengths: 6,6,6,6,6,6,6,6,3,0 (plus start node))

## About

The code is written by Valeria Bladinieres, Tobias Umland and Jacob Bräutigam.
