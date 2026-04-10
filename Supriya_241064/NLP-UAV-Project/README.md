Natural Language Command & Control for UAVs, Supriya, Pratyush Srivastava & Akul Agarwal

OVERVIEW : 
In this project we created a model which takes a command input from the user, forward the command to an LLM, verify the LLM output, forward the verified output as input to STIL set up which eventually guides the drone according to the users desire !

User Input (Text Command)
↓
LLM (Gemini API)
↓
Structured Waypoints (JSON)
↓
DroneKit Controller
↓
ArduPilot SITL (Simulation)
↓
Drone Movement

PREREQUISITES : 
OS: Ubuntu 20.04+, Python: 3.10+, Tools Required: ArduPilot SITL; DroneKit; pymavlink; Google Gemini API (google-genai)

INSTALLATION : 
1. Clone the directory : 
git clone 
cd 

2. Create virtual environment :
python3 -m venv venv-ardupilot
source venv-ardupilot/bin/activate

3. Install libraries : 
pip install dronekit pymavlink google-genai

4. Set up API key :
export GOOGLE_API_KEY="your_api_key"

HOW TO RUN : 
run the STIL
sim_vehicle.py -v ArduCopter --console --map --out="127.0.0.14550"

run the python srcript 
python3 main_controller.py
enter the command of your choise infron of ENTER COMMAND : 

FILE DESCRIPTIONS : 
connect_test.py --> script to fly the drone to an altutide of choise
waypoint_nav.py --> script to fly drone in to a desired target
waypoint_square_nav.py --> script to fly the drone in a square 
llm_waypoints.point --> script to use llm for the extraction of desired waypoints 
geometry_utils.py --> srcipt to get the waypoints along the desired trajectories 
main_controller.py --> main script which infuses all the elements of the project and executes it

DEMO : 


WHAT I LEARNED : 
1. STIL environment
2. QGroundController
3. ubuntu interface
4. python scripts that controll drone
5. dronekit library
6. LLM integration using API keys
7. geometric function using math and matplotlib

KNOWN ISSUES 
1. API key is not working hence no response from LLM
