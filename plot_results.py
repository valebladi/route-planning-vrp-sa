#!/usr/bin/env python3
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
from joypy import joyplot

sns.set_theme()

### settings to get publication-ready plots
dpi = 600						# resolution of saved .png figures
cm = 1/2.54						# centimeters in inches
column_width = 8.4*cm					# width of single paper column
double_column_width = 17.4*cm				# width over both columns
fsize = 10						# change the font size here
params = {'legend.fontsize': fsize*0.8,
          'axes.labelsize': fsize*0.9,
          'axes.titlesize': fsize,
          'xtick.labelsize': fsize*0.8,
          'ytick.labelsize': fsize*0.8,
          'axes.titlepad': fsize*1.5,
          'font.family': 'serif',
          'font.serif': ['cmr10']}
plt.rcParams.update(params)
sns.set_context("paper", rc={"font":"cmr10", "font.size":fsize*0.8,"axes.titlesize":fsize*0.9,"axes.labelsize":fsize*0.8, "xtick.labelsize": fsize*0.8, "ytick.labelsize": fsize*0.8})
# if necessary: change font family (example: https://www.alanshawn.com/tech/2021/03/27/matplotlib-latex-style.html)

# check font; returns the default font name, if font is not installed
#import matplotlib
#from matplotlib.font_manager import findfont, FontProperties
#print(findfont(FontProperties(family=matplotlib.rcParams['font.family'])))

### folder config
figures_dir = os.path.join(os.path.dirname(__file__), 'figures')
data_dir = os.path.join(os.path.dirname(__file__), 'data')
if not os.path.isdir(figures_dir): os.makedirs(figures_dir)
if not os.path.isdir(data_dir): os.makedirs(data_dir)

############ Experiment 1: get intuition about influence of initial solution method and permutation operator distribution - values copied from Valerias table ############
### input data
data = pd.DataFrame(np.array([
["4/1", "1/1", 2930.0, 2906.6, 3020.6, 2973.3],
["1/4", "1/1", 3032.0, 3035.6, 3268.0, 3213.3],
["1/1", "4/1", 3033.3, 3035.5, 3290.8, 3271.3],
["1/1", "1/4", 2870.8, 2881.1, 2901.5, 2881.6],
["4/4", "1/1", 2979.2, 2990.8, 3193.3, 3129.3],
["4/1", "4/1", 2965.6, 2979.4, 3197.8, 3144.0],
["4/1", "1/4", 2856.2, 2863.7, 2880.7, 2847.6],
["1/4", "4/1", 3087.7, 3087.7, 3374.6, 3293.7],
["1/4", "1/4", 2930.5, 2935.5, 2982.6, 2907.7],
["1/1", "4/4", 2942.5, 2977.6, 3039.6, 3026.8],
["4/4", "4/1", 3046.2, 3041.4, 3191.3, 3231.5],
["4/4", "1/4", 2872.1, 2874.3, 2986.3, 2881.2],
["4/1", "4/4", 2897.3, 2895.3, 2917.5, 2915.5],
["1/4", "4/4", 2991.5, 3008.3, 3126.9, 3058.9],
["4/4", "4/4", 2918.9, 2923.7, 3018.5, 2996.7],
["1/1", "1/1", 2918.9, 2923.7, 3018.5, 2996.7]]
), columns=['Weight: 2-opt/relocate', 'Weight: global relocate/global exchange', 'median cost 1', 'median cost 2', 'median cost 3', 'median cost 4'])
data['median cost 1'] = data['median cost 1'].astype(float)
data['median cost 2'] = data['median cost 2'].astype(float)
data['median cost 3'] = data['median cost 3'].astype(float)
data['median cost 4'] = data['median cost 4'].astype(float)

### prepare data for visualization
data_nn_ber = data.pivot('Weight: 2-opt/relocate', 'Weight: global relocate/global exchange', 'median cost 1')
data_sw_ber = data.pivot('Weight: 2-opt/relocate', 'Weight: global relocate/global exchange', 'median cost 2')
data_nn_ch = data.pivot('Weight: 2-opt/relocate', 'Weight: global relocate/global exchange', 'median cost 3')
data_sw_ch = data.pivot('Weight: 2-opt/relocate', 'Weight: global relocate/global exchange', 'median cost 4')
data['Weight: 2-opt/relocate/global relocate/global exchange'] = data['Weight: 2-opt/relocate'] + "/" + data['Weight: global relocate/global exchange']
data_ber = data[['median cost 1', 'median cost 2']]
data_ch = data[['median cost 3', 'median cost 4']]

### get extrema for identical scaling
min_val_ber = data[['median cost 1', 'median cost 2']].min().min()
max_val_ber = data[['median cost 1', 'median cost 2']].max().max()
min_val_ch = data[['median cost 3', 'median cost 4']].min().min()
max_val_ch = data[['median cost 3', 'median cost 4']].max().max()

### draw plots
fig1, (ax1, ax2) = plt.subplots(1, 2, figsize=(double_column_width, 0.5*double_column_width), constrained_layout=True)
sns.heatmap(data_nn_ber, annot=True, fmt='.0f', linewidths=.5, ax=ax1, vmin=min_val_ber, vmax=max_val_ber,cbar=False)
sns.heatmap(data_sw_ber, annot=True, fmt='.0f', linewidths=.5, ax=ax2, vmin=min_val_ber, vmax=max_val_ber,cbar=False)
ax1.set_title('Initial solution: nearest neighbor')
ax2.set_title('Initial solution: sweep')
#fig1.suptitle('Example berlin52')

fig2, (ax3, ax4) = plt.subplots(1, 2, figsize=(double_column_width, 0.5*double_column_width), constrained_layout=True)
sns.heatmap(data_nn_ch, annot=True, fmt='.0f', linewidths=.5, ax=ax3, vmin=min_val_ch, vmax=max_val_ch,cbar=False)
sns.heatmap(data_sw_ch, annot=True, fmt='.0f', linewidths=.5, ax=ax4, vmin=min_val_ch, vmax=max_val_ch,cbar=False)
ax3.set_title('Initial solution: nearest neighbor')
ax4.set_title('Initial solution: sweep')
#fig2.suptitle('Example ch130')

fig3a, ax5 = plt.subplots(1, 1, figsize=(column_width, 0.55*double_column_width), constrained_layout=True)
sns.heatmap(data_ber.values, xticklabels=['Nearest neighbor','Sweep'], yticklabels=data['Weight: 2-opt/relocate/global relocate/global exchange'].values, annot=True, fmt='.0f', linewidths=.5, ax=ax5, vmin=min_val_ber, vmax=max_val_ber, cbar=False)
ax5.set(xlabel='', ylabel=' ')
fig3b, ax6 = plt.subplots(1, 1, figsize=(column_width, 0.55*double_column_width), constrained_layout=True)
sns.heatmap(data_ch.values, xticklabels=['Nearest neighbor','Sweep'], yticklabels=data['Weight: 2-opt/relocate/global relocate/global exchange'].values, annot=True, fmt='.0f', linewidths=.5, ax=ax6, vmin=min_val_ch, vmax=max_val_ch, cbar=False)
ax6.set(xlabel='', ylabel=' ')
ax5.xaxis.set_ticks_position('top')
ax6.xaxis.set_ticks_position('top')
ax5.tick_params(top=False)
ax5.tick_params(axis='y', pad=15.0)
ax6.tick_params(top=False)
ax6.tick_params(axis='y', pad=15.0)
fig3a.text(0.02, 0.8905, 'SA parameter')
fig3b.text(0.02, 0.8905, 'SA parameter')
ax5.set_title('Example berlin52')
ax6.set_title('Example ch130')


############ Experiment 2: select algorithm parameters - input values directly from csv file ############
### read data
data_parameter_search = pd.read_csv(os.path.join(data_dir, 'results_2_parameter_search.csv'))

### reformat weights for fancy labeling
data_parameter_search['TWOOPT weight'] = data_parameter_search['TWOOPT weight'].astype(int).astype(str)
data_parameter_search['RELOCATE weight'] = data_parameter_search['RELOCATE weight'].astype(int).astype(str)
data_parameter_search['GLOBAL_RELOCATE weight'] = data_parameter_search['GLOBAL_RELOCATE weight'].astype(int).astype(str)
data_parameter_search['GLOBAL_EXCHANGE weight'] = data_parameter_search['GLOBAL_EXCHANGE weight'].astype(int).astype(str)
### shorten initial solution for space-saving labeling
data_parameter_search['initial'] = data_parameter_search['initial'].replace("NEARESTNEIGHBOR_MA", "NN").replace("SWEEP_HEURISTIC_MA", "Sweep")

### split examples
data_parameter_search_ber = data_parameter_search[data_parameter_search['file'] == 'berlin52.tsp']
data_parameter_search_ch = data_parameter_search[data_parameter_search['file'] == 'ch130.tsp']

### calc median cost for all parameter sets
data_ber = data_parameter_search_ber.groupby(['initial', 'TWOOPT weight', 'RELOCATE weight', 'GLOBAL_RELOCATE weight', 'GLOBAL_EXCHANGE weight', 'Tmax'])['cost (best solution)'].median()
data_ch = data_parameter_search_ch.groupby(['initial', 'TWOOPT weight', 'RELOCATE weight', 'GLOBAL_RELOCATE weight', 'GLOBAL_EXCHANGE weight', 'Tmax'])['cost (best solution)'].median()
data_ber = data_ber.reset_index()
data_ch = data_ch.reset_index()

### merge colums to get y axis labels (weights & initial solution)
data_ber['Weight: 2-opt/relocate/global relocate/global exchange & Initial solution'] = data_ber['TWOOPT weight'] + "/" + data_ber['RELOCATE weight'] + "/" + data_ber['GLOBAL_RELOCATE weight'] + "/" + data_ber['GLOBAL_EXCHANGE weight'] + "\n& " + data_ber['initial']
data_ch['Weight: 2-opt/relocate/global relocate/global exchange & Initial solution'] = data_ch['TWOOPT weight'] + "/" + data_ch['RELOCATE weight'] + "/" + data_ch['GLOBAL_RELOCATE weight'] + "/" + data_ch['GLOBAL_EXCHANGE weight'] + "\n& " + data_ch['initial']

### reformat to get sns heatmap data
data_ber_plot = data_ber.pivot('Weight: 2-opt/relocate/global relocate/global exchange & Initial solution', 'Tmax', 'cost (best solution)')
data_ch_plot = data_ch.pivot('Weight: 2-opt/relocate/global relocate/global exchange & Initial solution', 'Tmax', 'cost (best solution)')

### draw plot
fig4a, ax7 = plt.subplots(1, 1, figsize=(column_width, column_width*0.75), constrained_layout=True)
heatmap_ber = sns.heatmap(data_ber_plot, annot=True, fmt='.0f', linewidths=.5, ax=ax7, cbar=False)
fig4b, ax8 = plt.subplots(1, 1, figsize=(column_width, column_width*0.75), constrained_layout=True)
heatmap_ch = sns.heatmap(data_ch_plot, annot=True, fmt='.0f', linewidths=.5, ax=ax8, cbar=False)
heatmap_ber.set_yticklabels(labels=heatmap_ber.get_yticklabels(), rotation=0, ha='center')
heatmap_ch.set_yticklabels(labels=heatmap_ch.get_yticklabels(), rotation=0, ha='center')
ax7.set(xlabel = 'T$_{max}$', ylabel=' ')
ax8.set(xlabel = 'T$_{max}$', ylabel=' ')
ax7.xaxis.set_ticks_position('top')
ax8.xaxis.set_ticks_position('top')
ax7.xaxis.set_label_position('top')
ax8.xaxis.set_label_position('top')
fig4a.text(0.02, 0.8305, 'SA parameter')
fig4b.text(0.02, 0.8305, 'SA parameter')
ax7.tick_params(top=False)
ax7.tick_params(axis='y', pad=25.0)
ax8.tick_params(top=False)
ax8.tick_params(axis='y', pad=25.0)
ax7.set_title('Example berlin52')
ax8.set_title('Example ch130')


############ Experiment 3: evaluate influence of number of iterations and initial temperature - input values directly from csv file ############
### input data
data_iterations_tmax_input = pd.read_csv(os.path.join(data_dir, 'results_3_iterations.csv'))

### reformat to get one colum per Tmax level
data_iterations_tmax = data_iterations_tmax_input.pivot(columns='Tmax', values='cost (best solution)')
data_iterations_tmax['iterations'] = data_iterations_tmax_input['iterations']
data_iterations_tmax.columns = ['T$_{max}$= $\,$10','T$_{max}$= $\,$50','T$_{max}$=200','iterations'] 

### draw plot
fig5, ax9 = joyplot( 
    data=data_iterations_tmax, 
    by='iterations',
    column=['T$_{max}$= $\,$10','T$_{max}$= $\,$50','T$_{max}$=200'], 
    color=['#274e13', 'red', '#f1c232'],
    legend=True,
    loc="lower right",
    alpha=0.6,
    overlap=0.85,
    yrot=90,
    figsize=(column_width, 0.66*double_column_width),
    background='w', 
    title="Influence of T$_{max}$ and number of iterations"
)
ax9[data_iterations_tmax['iterations'].nunique()].set(xlabel='Cost (kWh)')
ax9[int(data_iterations_tmax['iterations'].nunique()/2)].set(ylabel='Relative frequency')
fig5.subplots_adjust(bottom=0.1)
fig5.text(0.01, 0.02, 'Iterations')



############ save images
for fileformat in ['.png','.pdf']:
    fig1.savefig(os.path.join(figures_dir, 'heat_1_berlin52_weights_init' + fileformat), dpi=dpi, pad_inches=0.0)
    fig2.savefig(os.path.join(figures_dir, 'heat_1_ch130_weights_init' + fileformat), dpi=dpi, pad_inches=0.0)
    fig3a.savefig(os.path.join(figures_dir, 'heat_1_berlin52_ch130_weights_init_A' + fileformat), dpi=dpi, pad_inches=0.0)
    fig3b.savefig(os.path.join(figures_dir, 'heat_1_berlin52_ch130_weights_init_B' + fileformat), dpi=dpi, pad_inches=0.0)
    fig4a.savefig(os.path.join(figures_dir, 'heat_2_berlin52_ch130_tmax_weights_init_A' + fileformat), dpi=dpi, pad_inches=0.0)
    fig4b.savefig(os.path.join(figures_dir, 'heat_2_berlin52_ch130_tmax_weights_init_B' + fileformat), dpi=dpi, pad_inches=0.0)
    fig5.savefig(os.path.join(figures_dir, 'hist_3_ch130_tmax_iterations' + fileformat), dpi=dpi, pad_inches=0.0)



plt.show()

