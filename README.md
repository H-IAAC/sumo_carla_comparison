# `Comparative Analysis of Synthetic Inertial Data Quality from CARLA and SUMO Driving Simulators`

CARLA and SUMO are widely adopted open-source simulators in autonomous driving and intelligent transportation systems (ITS). While neither was initially designed to generate high-fidelity inertial data such as that from an Inertial Measurement Unit (IMU), both have been employed in diverse research contexts—including visual-inertial SLAM, motion planning, and navigation under adverse conditions—where inertial data plays a critical role. In this study, we evaluate the quality of inertial data produced by CARLA and SUMO through a direct comparison with the naturalistic UAH-DriveSet dataset, which contains IMU data across various real-world driving behaviors. Despite SUMO's lack of a built-in physics engine for detailed inertial simulation, our analysis reveals that it performs better in qualitative and quantitative assessments. To our knowledge, this is the first systematic comparison of its kind, and it highlights important limitations in current simulation tools, offering valuable insights for researchers relying on simulated inertial data in autonomy-related studies.

This project was developed as part of the Cognitive Architectures research line from 
the Hub for Artificial Intelligence and Cognitive Architectures (H.IAAC) of the State University of Campinas (UNICAMP).
See more projects from the group [here](https://github.com/brgsil/RepoOrganizer).

[![](https://img.shields.io/badge/-H.IAAC-eb901a?style=for-the-badge&labelColor=black)](https://hiaac.unicamp.br/)
[![](https://img.shields.io/badge/-Arq.Cog-black?style=for-the-badge&labelColor=white&logo=data:image/svg%2bxml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4gPHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI1Ni4wMDQiIGhlaWdodD0iNTYiIHZpZXdCb3g9IjAgMCA1Ni4wMDQgNTYiPjxwYXRoIGlkPSJhcnFjb2ctMiIgZD0iTTk1NS43NzQsMjc0LjJhNi41Nyw2LjU3LDAsMCwxLTYuNTItNmwtLjA5MS0xLjE0NS04LjEtMi41LS42ODksMS4xMjNhNi41NCw2LjU0LDAsMCwxLTExLjEzNi4wMjEsNi41Niw2LjU2LDAsMCwxLDEuMzY4LTguNDQxbC44LS42NjUtMi4xNS05LjQ5MS0xLjIxNy0uMTJhNi42NTUsNi42NTUsMCwwLDEtMi41OS0uODIyLDYuNTI4LDYuNTI4LDAsMCwxLTIuNDQzLTguOSw2LjU1Niw2LjU1NiwwLDAsMSw1LjctMy4zLDYuNDU2LDYuNDU2LDAsMCwxLDIuNDU4LjQ4M2wxLC40MSw2Ljg2Ny02LjM2Ni0uNDg4LTEuMTA3YTYuNTMsNi41MywwLDAsMSw1Ljk3OC05LjE3Niw2LjU3NSw2LjU3NSwwLDAsMSw2LjUxOCw2LjAxNmwuMDkyLDEuMTQ1LDguMDg3LDIuNS42ODktMS4xMjJhNi41MzUsNi41MzUsMCwxLDEsOS4yODksOC43ODZsLS45NDcuNjUyLDIuMDk1LDkuMjE4LDEuMzQzLjAxM2E2LjUwNyw2LjUwNywwLDAsMSw1LjYwOSw5LjcyMSw2LjU2MSw2LjU2MSwwLDAsMS01LjcsMy4zMWgwYTYuNCw2LjQsMCwwLDEtMi45ODctLjczMmwtMS4wNjEtLjU1LTYuNjgsNi4xOTIuNjM0LDEuMTU5YTYuNTM1LDYuNTM1LDAsMCwxLTUuNzI1LDkuNjkxWm0wLTExLjQ2MWE0Ljk1LDQuOTUsMCwxLDAsNC45NTIsNC45NUE0Ljk1Nyw0Ljk1NywwLDAsMCw5NTUuNzc0LDI2Mi43MzlaTTkzNC44LDI1Ny4zMjVhNC45NTIsNC45NTIsMCwxLDAsNC4yMjEsMi4zNDVBNC45Myw0LjkzLDAsMCwwLDkzNC44LDI1Ny4zMjVabS0uMDIyLTEuNThhNi41MTQsNi41MTQsMCwwLDEsNi41NDksNi4xTDk0MS40LDI2M2w4LjA2MSwyLjUuNjg0LTEuMTQ1YTYuNTkxLDYuNTkxLDAsMCwxLDUuNjI0LTMuMjA2LDYuNDQ4LDYuNDQ4LDAsMCwxLDIuODQ0LjY1bDEuMDQ5LjUxOSw2LjczNC02LjI1MS0uNTkzLTEuMTQ1YTYuNTI1LDYuNTI1LDAsMCwxLC4xMTUtNi4yMjksNi42MTgsNi42MTgsMCwwLDEsMS45NjYtMi4xMzRsLjk0NC0uNjUyLTIuMDkzLTkuMjIyLTEuMzM2LS4wMThhNi41MjEsNi41MjEsMCwwLDEtNi40MjktNi4xbC0uMDc3LTEuMTY1LTguMDc0LTIuNS0uNjg0LDEuMTQ4YTYuNTM0LDYuNTM0LDAsMCwxLTguOTY2LDIuMjY0bC0xLjA5MS0uNjUyLTYuNjE3LDYuMTMxLjc1MSwxLjE5MmE2LjUxOCw2LjUxOCwwLDAsMS0yLjMsOS4xNjRsLTEuMS42MTksMi4wNiw5LjA4NywxLjQ1MS0uMUM5MzQuNDc1LDI1NS43NSw5MzQuNjI2LDI1NS43NDQsOTM0Ljc3OSwyNTUuNzQ0Wm0zNi44NDQtOC43NjJhNC45NzcsNC45NzcsMCwwLDAtNC4zMTYsMi41LDQuODg5LDQuODg5LDAsMCwwLS40NjQsMy43NjIsNC45NDgsNC45NDgsMCwxLDAsNC43NzktNi4yNjZaTTkyOC43LDIzNS41MzNhNC45NzksNC45NzksMCwwLDAtNC4zMTcsMi41LDQuOTQ4LDQuOTQ4LDAsMCwwLDQuMjkxLDcuMzkxLDQuOTc1LDQuOTc1LDAsMCwwLDQuMzE2LTIuNSw0Ljg4Miw0Ljg4MiwwLDAsMCwuNDY0LTMuNzYxLDQuOTQsNC45NCwwLDAsMC00Ljc1NC0zLjYzWm0zNi43NzYtMTAuMzQ2YTQuOTUsNC45NSwwLDEsMCw0LjIyMiwyLjM0NUE0LjkyMyw0LjkyMywwLDAsMCw5NjUuNDc5LDIyNS4xODdabS0yMC45NTItNS40MTVhNC45NTEsNC45NTEsMCwxLDAsNC45NTEsNC45NTFBNC45NTcsNC45NTcsMCwwLDAsOTQ0LjUyNywyMTkuNzcyWiIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoLTkyMi4xNDMgLTIxOC4yKSIgZmlsbD0iIzgzMDNmZiI+PC9wYXRoPjwvc3ZnPiA=)](https://github.com/brgsil/RepoOrganizer)

## Repository Structure

- **!Carla_generator**: Folder containing the notebook and the map necessary to run the simulation and generate the data.
- **!Sumo_generator**: Folder containing the notebook and the SUMO files necessary to run the simulation and generate the data.
- **UAH-DRIVESET-v1**: Folder containing the data from the UAH-Driveset.
- **data_experiment1_carla_100Hz**: Folder containing the data from both normal and aggressive drivers generate by CARLA in 100Hz.
- **data_experiment1_sumo_100Hz**: Folder containing the data from both normal and aggressive drivers generate by SUMO in 100Hz.
- **plots**: Folder containing plots and images to support the comparison.
- **custom_libs**: Folder containing important scripts necessary for custom CARLA simulations.
- **envs**: Folder containing the `.yml` files to create the conda environments necessary to run the SUMO and CARLA simulations. Optional.
- **experiment1.ipynb**: Notebook to make the comparisons.

## Dependencies / Requirements

To run the experiments with the already generated data, one should simply install the packages under `requirements.txt` via `pip install -r requirements.txt`. 

If you wish to run the simulations and make changes to them, the conda environments to run the scripts are provided in the repository. Since the dependencies are different for each simulator, it is important to use the correct environment.

### (Optional) SUMO Installation and Environment:
To create the environment run `conda env create -f sumo-env.yml` inside the `/envs` folder.

The full instalation guide can be found at the [SUMO Installation Guide](https://sumo.dlr.de/docs/Installing/index.html).

### (Optional) CARLA Installation and Environment:
To create the environment run `conda env create -f sumo-env.yml` inside the `/envs` folder. 

**IMPORTANT**: CARLA agents are used to simulate driver behaviors, but there are steps required to make them work properly in case one desires to have the exact same results, since changes to their parameters had to be made. More on this can be found at the **Installation / Usage** section.

The full instalation guide can be found at the [CARLA Installation Guide](https://carla.readthedocs.io/en/latest/start_quickstart/#carla-installation).

## Installation / Usage

### `experiment1.ipynb`

This is the main file for the comparisons. In it, it is possible to provide the path of SUMO and CARLA data and define which of the drivers in the UAH-Driveset are going to be used for comparison.

The script also generates histograms, umaps and raw data plots, as well as the KL-divergence between the histograms for the simulators and the real data.

### `SUMO_generator`

This folder allows the customization of the simulation and trajectories and behaviors of the vehicles simulated in SUMO by making changes to `experiment1_runner.ipynb`.

The notebook allows for the customizatio of several driving parameters, start and end edges of the simulation, and provides the code to run and save the data generated, as well as all the intermediate files used by SUMO.

### `CARLA_generator`

This folder allows the customization of sensor parameters, behavior parameters, simulation parameters by making changes to `experiment1_runner.ipynb`.

CARLA agents are used o simulate driver behaviors, but one of the files used inside the agents scripts is outdated and must be correct. The code provided by CARLA is using an old version of TensorFlow with deprecated functions. 
The custom file updated to run the experiment can be found at `custom_libs/networks.py` and it should replace the file with the same name under `~/miniconda3/envs/carla-env/lib/python3.8/site-packages/agents/scripts`.

The results collected for this experiment made changes to how the agens parameters in CARLA to achieve a fair comparison and those changes had to me make directly to the source code. This makes the process more manual, but it is still simple. 

The first change is made to `/opt/carla-simulator/PythonAPI/carla/agents/navigation/behavior_types.py` (the `opt/carla-simulator`folder is created after installing CARLA), where the parameters for each vehicle class are defined. In it we changed the values of `max_speed`and `speed_lim_dist` for the normal and aggressive drivers. The new version can be found in the repo at `custom_libs/behavior_types.py`.

Next we have to create a custom agent to override the `update_information` function inside the agent, since it was getting incorrect maximum speeds from the roads, keeping the vehicle stuck at a 40 km/h speed. The code for the custom agent is provided at `custom_libs/custom_agent.py` and must be pasted inside the `/opt/carla-simulator/PythonAPI/carla/agents/navigation` folder.

Now, one should be able to run the simulation correctly and make changes to the parameters as desired.

## Citation

**Waiting for publication**

## Authors

- 2024-2025 Renan Matheus S. Florencio: Computer Engineering, State University of Campinas (Unicamp)
- 2024-2025 Paula Dornhofer P. Costa: Professor at School of Electrical and Computer Engineering, State University of Campinas (Unicamp)
  
## Acknowledgements

This project is part of the Hub for Artificial Intelligence and Cognitive Architectures
(H.IAAC- Hub de Inteligência Artificial e Arquiteturas Cognitivas). We acknowledge the 
support of PPI-Softex/MCTI by grant 01245.013778/2020-21 through the Brazilian Federal Government.
