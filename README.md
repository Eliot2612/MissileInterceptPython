# MissileInterceptPython

MissileInterceptPython is a Python project that simulates a missile defence system, visualising both incoming missiles and interceptor responses using Pygame. The project aims to:

- Simulate missile launches and interception attempts
- Visualise trajectories and interception events in real time
- Experiment with the number and strategy of interceptors
- Integrate reinforcement learning (RL) to optimise interception strategies and maximise success rates

## Features
- Real-time 2D visualisation of missile and interceptor paths
- Configurable simulation parameters (number, speed, and launch positions of missiles/interceptors)
- Planned RL integration for training interceptors to improve interception rates
- Modular code for easy experimentation and extension

## Setup
1. Clone the repository:
	```bash
	git clone https://github.com/Eliot2612/MissileInterceptPython.git
	cd MissileInterceptPython
	```
2. Install dependencies:
	```bash
	pip install -r requirements.txt
	```

## Usage
Run the simulation:
```bash
python simulation.py
```

## Reinforcement Learning (Planned)
The project will use RL (e.g., with `stable-baselines3`) to train interceptors. The environment will provide rewards for successful interceptions and penalise failures, allowing agents to learn optimal strategies over time.

## Requirements
- Python 3.8+
- Pygame
- (Planned) stable-baselines3, gymnasium

## Licence
MIT Licence (or specify your licence)
