#!/bin/bash

### Options - general options ###
repetitions="50"					# number of python calls per set of settings: [positive integer]
debug="OFF"						# amount of command line output (OFF MIN FULL)
show_gui="OFF"						# enables GUI, if set != OFF (OFF SOLUTION STEPS)
### Options - test specific options with default values ###
files="berlin52"					# problem instances: list of input files (thesis1 berlin52 monbijou-james-simon ch130)
initial_slns="SWEEP"			# list of initial solution methods (NEARESTNEIGHBOR RANDOM NEARESTNEIGHBOR_MA SWEEP_HEURISTIC_MA)
declare -a operator_weights_list=(			# distribution of neighborhood operators (TWOOPT RELOCATE GLOBAL_RELOCATE GLOBAL_EXCHANGE): list of [4*positive float]
"0.4 0.1 0.1 0.4")
t_maxs="100.0"						# maximum temperature value: list of [positive float]
t_mins="0.01"						# minimum temperature value: list of [positive float]
iterations_list="10000"				# iterations while simulated annealing: list of [positive integer]

### Benchmark loops ###
function run_benchmark() {
	for file in $files
	do
		for initial_sln in $initial_slns
		do
			for operator_weights in "${operator_weights_list[@]}";
			do
				for iterations in $iterations_list
				do
					for t_max in $t_maxs
					do
						for t_min in $t_mins
						do
							for ((z=0; z<$repetitions;z++))
							do	
								#echo "$z"
								command="python3 solver.py --file $file --initial $initial_sln --operator_weights $operator_weights --debug $debug --iterations $iterations --show_gui $show_gui --temperature_maximum $t_max --temperature_minimum $t_min" 
								echo $command
								$command
							done
						done
					done
				done
			done 
		done 
	done
}

function rename_results() {
	new_name="results_${benchmark}_$(date +%F_%H-%M-%S).csv"
	if mv results.csv $new_name > /dev/null 2>&1; then
		echo "Test $benchmark: Saved output to $new_name!"
	else
		echo "Test $benchmark: No output saved!"
	fi
}

rm results.csv

### Benchmark 1
benchmark="1"
echo "Test 1: Get first intuition about the influence of permutation operators and the initial solution."
files="berlin52"
initial_slns="SWEEP NEARESTNEIGHBOR"
declare -a operator_weights_list=("1 1 1 4" "1 1 4 1" "1 4 1 1" "4 1 1 1" "1 1 4 4" "1 4 1 4" "1 4 4 1" "4 1 1 4" "4 1 4 1" "4 4 1 1" "1 4 4 4" "4 1 4 4" "4 4 1 4" "4 4 4 1" "1 1 1 1")
t_maxs="100.0"
iterations_list="10000" # berlin52 is smaller
#run_benchmark # TODO uncomment to run this benchmark

files="ch130"
t_maxs="100.0"
iterations_list="100000" # ch130 is larger
#run_benchmark # TODO uncomment to run this benchmark

rename_results


### Benchmark 2
benchmark="2"
echo "Test 2: Select a good parameter set per example file."
files="berlin52"
initial_slns="SWEEP NEARESTNEIGHBOR"
declare -a operator_weights_list=("1 1 1 4" "4 1 1 4" "4 4 1 4")
t_maxs="10.0 50.0 100.0 200.0 500.0"
iterations_list="10000"
#run_benchmark # TODO uncomment to run this benchmark

files="ch130"
iterations_list="100000"
#run_benchmark # TODO uncomment to run this benchmark

rename_results

### Benchmark 3
benchmark="3"
echo "Test 3: Evaluate influence of number of iterations."
files="ch130"
initial_slns="SWEEP"
declare -a operator_weights_list=("4 1 1 4")
t_maxs="10.0 50.0 200.0"
iterations_list="3000 10000 30000 100000 300000"
#run_benchmark # TODO uncomment to run this benchmark

rename_results

### Benchmark 4
benchmark="4"
echo "Test 4: Evaluate SA parameters on a line and a circle"
files="line circle"
initial_slns="SWEEP NEARESTNEIGHBOR"
t_maxs="100.0"
declare -a operator_weights_list=("1 1 1 4" "1 1 4 1" "1 4 1 1" "4 1 1 1" "1 1 4 4" "1 4 1 4" "1 4 4 1" "4 1 1 4" "4 1 4 1" "4 4 1 1" "1 4 4 4" "4 1 4 4" "4 4 1 4" "4 4 4 1" "1 1 1 1")
iterations_list="1000 10000"
run_benchmark
rename_results