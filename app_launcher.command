#!/bin/bash

# Navigate to the Git repository
cd ~/Documents/Git/teams-scribe

# Make sure we are on the `master` branch
git checkout master

# Update the branch
git pull

# Run the app
pipenv run python source/teams_scribe.py

