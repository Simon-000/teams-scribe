# vtt file handling
import webvtt
# Runtime/interpreter handling
import sys
# OS interactions
import os
# Data manipulation
import pandas as pd
# XML structures
import xml.etree.ElementTree as ET
# JSON structures
import json
# Date/time utilities
from datetime import datetime
# Pop-up windows
import easygui

# Add "~/Documents/Git/teams-scribe/source/" to sys.path so we can import our bespoke modules
module_path = os.path.abspath(os.path.join(os.path.expanduser('~/Documents/Git/teams-scribe/source/')))
if module_path not in sys.path:
    sys.path.append(module_path)

# Internal packages
from llm_prompts import grab_ur_prompts_dictionary

# Define function for reading in vtt files and stripping everything other than conversation itself
def read_parse_vtt(vtt_file_path):
    """
    TODO: Google Docstring
    """
    
    # Read-in vtt file using `vtt_file_path`
    vtt_raw = webvtt.read(vtt_file_path)

    # Create placeholder for parsed vtt
    vtt_clean = ""

    # Create a list to hold all lines from `vtt_raw`
    lines = []

    # Parse `vtt_raw` by looping through each line and adding it to `lines`
    for line in vtt_raw:
        lines.extend(line.text.strip().splitlines())

    # De-duplicate `lines` and output cleaned version in `vtt_clean`
    previous = None
    for line in lines:
        if line == previous:
           continue
        vtt_clean += " " + line
        previous = line

    # Returned cleaned vtt file
    return(vtt_clean)

# Define function for parsing UR outputs based on the task the output is related to
def parse_ur_outputs(ur_task, input_string):
    """
    TODO: Google Docstring
    """

    # Import UR task dictionary
    ur_prompts_dictionary = grab_ur_prompts_dictionary()

    # Extract keys as list from the above dictionary
    ur_prompt_keys_list = list(ur_prompts_dictionary.keys())

    # Define appropriate parsing logic based on which `ur_task` was requested
    if ur_task in ur_prompt_keys_list:

        if ur_task == 'Findings Extraction':
            
            # Parse the XML string
            xml_findings_extraction = ET.fromstring(input_string.content)
            
            # Extract all variables
            table_findings_extraction = []
            for finding in xml_findings_extraction.findall('Finding'):
                sequence = finding.find('Sequence').text
                point = finding.find('Point').text
                type_ = finding.find('Type').text
                impact = finding.find('Impact').text
                table_findings_extraction.append([sequence, point, type_, impact])
            
            # Create a DataFrame from `table_findings_extraction`
            df_findings_extraction = pd.DataFrame(table_findings_extraction, columns=['Sequence', 'Point', 'Type', 'Impact'])
            
            # Convert 'Sequence' and 'Impact' columns to integers
            df_findings_extraction['Sequence'] = df_findings_extraction['Sequence'].astype(int)
            df_findings_extraction['Impact'] = df_findings_extraction['Impact'].astype(int)
            
            # Return `df_findings_extraction`
            return(df_findings_extraction)

        if ur_task == 'Direct Quotes Extraction':

            # Parse the XML string 
            xml_quotes_extraction = ET.fromstring(input_string.content)
            
            # Extract all variables
            table_quotes_extraction = []
            for finding in xml_quotes_extraction.findall('Finding'):
                sequence = finding.find('Sequence').text
                quote = finding.find('Quote').text
                impact = finding.find('Impact').text
                table_quotes_extraction.append([sequence, quote, impact])
            
            # Create a DataFrame from `table_quotes_extraction`
            df_quotes_extraction = pd.DataFrame(table_quotes_extraction, columns=['Sequence', 'Quote', 'Impact'])
            
            # Convert 'Sequence' column to integers
            df_quotes_extraction['Sequence'] = df_quotes_extraction['Sequence'].astype(int)
            
            # Return `df_quotes_extraction`
            return(df_quotes_extraction)

        if ur_task == 'Keyphrases and Entities Recognition':

            # Remove opening/closing "`" signs and "json" part of the string within `input_string` so we can treat as JSON
            preprocessed_keyphrases_recognition = input_string.content.replace("```", "").replace("json", "")
            
            # Load the JSON string
            try:
                raw_json_keyphrases_recognition = json.loads(preprocessed_keyphrases_recognition)
            except json.JSONDecodeError as e:
                print(f"JSON decoding failed: {e}")
                raw_json_keyphrases_recognition = {}
            
            # Extract all key-value pairs from above from 'Statements' field
            if raw_json_keyphrases_recognition:
                parsed_json_keyphrases_recognition = raw_json_keyphrases_recognition.get('Statements', [])
            else:
                print("No data found in requested JSON field.")
            
            # Turn above into a DataFrame
            df_keyphrases_recognition = pd.json_normalize(parsed_json_keyphrases_recognition)
            
            # Return `df_keyphrases_recognition`
            return(df_keyphrases_recognition)

        if ur_task == 'Theme Identification':

            # Remove opening/closing "`" signs and "json" part of the string within `input_string` so we can treat as JSON
            preprocessed_theme_identification = input_string.content.replace("```", "").replace("json", "")
            
            # Load the JSON string
            try:
                raw_json_theme_identification = json.loads(preprocessed_theme_identification)
            except json.JSONDecodeError as e:
                print(f"JSON decoding failed: {e}")
                raw_json_theme_identification = {}
            
            # Extract all key-value pairs from above from 'themes' field
            if raw_json_theme_identification:
                parsed_json_theme_identification = raw_json_theme_identification.get('themes', [])
            else:
                print("No data found in requested JSON field.")
            
            # Turn above into a DataFrame
            df_theme_identification = pd.json_normalize(parsed_json_theme_identification)
            

            # Return `df_theme_identification`
            return(df_theme_identification)

        else:
            display("Invalid outputs cannot be processed. Please check if `ur_task` parameter exist in dictionary generated by `grab_ur_prompts_dictionary()` method.")

    else:
        display("Invalid outputs cannot be processed. Please check if `ur_task` parameter exist in dictionary generated by `grab_ur_prompts_dictionary()` method.")
    


# Define a method for saving data frames as CSVs with file name based on current time and UR task
def save_df_to_csv(data_frame, ur_task, csv_path = "~/"):
        
    # Generate the current time
    current_time = datetime.now()
    
    # Convert the current time to a string
    string_current_time = current_time.strftime("_%H-%M-%S_%d-%m-%Y")

    # Turn `ur_task` lowercase with underscores instead of spaces
    clean_ur_task = ur_task.lower().replace(" ", "_")

    # Create full path
    output_path = csv_path + clean_ur_task + string_current_time + ".csv"

    # Save `data_frame` as CSV using above path
    data_frame.to_csv(output_path)


# Define a function generating a pop-up window with file explorer allowing to select single vtt file
def select_vtt_file():

    # Show an open file dialog and return the path to the selected file
    file_path = easygui.fileopenbox(msg="Select your VTT file", title="Open VTT File", default="*.vtt", filetypes=["*.vtt"])
    
    if file_path:
        print(f"Selected file: {file_path}")
        return file_path
    else:
        print("No file selected.")
        return None
