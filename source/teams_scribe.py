# External packages

# Runtime/interpreter handling
import sys
# OS interactions
import os
# Date/time utilities
from datetime import datetime

# Add "~/Documents/Git/teams-scribe/source/" to sys.path so we can import our bespoke modules
module_path = os.path.abspath(os.path.join(os.path.expanduser('~/Documents/Git/teams-scribe/source/')))
if module_path not in sys.path:
    sys.path.append(module_path)

# Internal packages
from openai_api import extract_ur_artifact 
from data_wrangling import read_parse_vtt, select_vtt_file
from llm_prompts import grab_vtt_into_case_study_prompt

# Prompt for turning vtt transcripts into case studies
turn_vtt_into_case_study_prompt = grab_vtt_into_case_study_prompt()

# Ask user to provide path to vtt file as a string
vtt_path = select_vtt_file()

# Ignest vtt using `read_parse_vtt` and `vtt_path`
vtt_transcript = read_parse_vtt(vtt_file_path = vtt_path)

# Generate case study using `extract_ur_artifact` with above transcript and prompt
case_study = extract_ur_artifact(
    input_data = vtt_transcript,
    ur_prompt = turn_vtt_into_case_study_prompt,
    model = "gpt-4o",
    debug = False,
    max_tokens = None,
    stop_sequence = None
)

# Generate the current time
current_time = datetime.now()

# Convert the current time to a string
string_current_time = current_time.strftime("_%H-%M-%S_%d-%m-%Y")

# Create text file name based on the above
file_name = "case_study" + string_current_time + ".txt"

# Open the file in write mode
with open(file_name, 'w') as file:
    # Redirect print output to the file
    print(case_study.content, file=file)