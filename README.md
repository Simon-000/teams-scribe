TODO: test the instructions in README work as expected.


# Purpose

To provide utility app that takes vtt transcripts of project interviews and turns them into case studies. It was developed based on Microsoft Teams' vtt transcripts that are automatically generated as a part of the meeting recording.


# First Time User Setup

1. [Create OpenAI account and subscribe to any paid plan](https://auth0.openai.com/u/signup/identifier?state=hKFo2SB6S19WUHZVLS1VYnlUZzc4bmkzbHpnYzJfMXVDdDNIaqFur3VuaXZlcnNhbC1sb2dpbqN0aWTZIHFtRzRPNm4wTnN1dGswQUJKWGFDaVpWZUloQ1A1dnFno2NpZNkgOGNLeU9saDhJZmFnVjlIUjA4UkZSSVhRZVRCSUZteUM).

2. Set up OpenAI API key using default way described [in the Step 2](https://platform.openai.com/docs/quickstart/step-2-set-up-your-api-key).

3. Install required software by opening terminal and executing below in order:
   
 a. Brew: /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

 b. Git: brew install git

 c. Pipenv: brew install pipenv

4. Clone our GitHub repository (if using SSH you need to setup SSH keys first) into following directory: "~/Documents/Git/".

5. Setup the environment by opening the terminal and executing below:

 a. cd ~/Documents/Git/teams-scribe/

 b. pipenv install

6. Navigate to Git repository and double click on "app_launcher.command" to launch the app.
