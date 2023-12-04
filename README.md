# Fetch Assessment

## Program to check the health of a set of HTTP endpoints.

1. Read an input argument to a file path with a list of HTTP endpoints in YAML format.
2. Test the health of the endpoints every 15 seconds.
3. Keep track of the availability percentage of the HTTP domain names being monitored by the program.
4. Log the cumulative availability percentage for each domain to the console after the completion of each 15-seconds test cycle.

## Prerequisites

- Python 3.x installed
- Pip package manager

## Installation

1. Clone the repository:

    `git clone https://github.com/Abhijeet-Singh1/Fetch_Assessment.git`
   
2. Inside the project folder, open the terminal to install the required Python packages using the following commands:

    `pip install pyyaml requests`

## Usage - Run the project on IDLE

1. Inside the project folder, open the terminal again and write the following command:

   `python -m idlelib.idle`
  
   This will open IDLE.

2. Open the required file.

3. Run the project.

4. Press `Ctrl + C` to terminate the program.

## Configuration

- Modify the `endpoints.yaml` file to add or remove endpoints.

## Dependencies

- `yaml`: YAML parser for Python.
- `requests`: HTTP library for Python.
