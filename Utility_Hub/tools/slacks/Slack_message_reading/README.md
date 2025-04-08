# Slack Message Analyzer Setup Guide

This guide provides step-by-step instructions for setting up the Slack Messages to analyze messages exchanged between users on Slack.


## **First Steps To create App and Get OAuth token in Slack**
-  [Reference Link](https://docs.celigo.com/hc/en-us/articles/7140655476507-How-to-create-an-app-and-retrieve-OAuth-token-in-Slack#:~:text=Retrieve%20Slack%20OAuth%20token,-Sign%20in%20to&text=your%20Slack%20account.-,Navigate%20to%20Slack%20API.,or%20Bot%20user%20OAuth%20token) 


## 1. Create an App

- **Sign Up/Sign In to your Slack account.** [Slack Sign In](https://slack.com/intl/en-in/)
- **Navigate to Slack API:** [Slack API](https://api.slack.com/apps)
- Click **Create new app.**
- Choose **"From scratch"** Option and provide the **App Name.** 
- Select your **workspace**s from the **drop-down list.**
- **Click Create app.** The Basic information page appears.

## 2. Generate App-level Token

- Navigate to **App-level tokens.**
- Click **Generate tokens and scopes.** The Generate an app-level token window appears.
- **Provide the Token name.**
- **Add required scopes.**
- **Click Generate.**

## 3. Configure Features

- Toggle on **"Incoming webhooks"** under 
    ```
    Features > Incoming webhooks.
    ```
- Toggle on **"Interactivity & Shortcuts"**
    ```
     Features > Interactivity & shortcuts.
     ```
- **Provide necessary information and save changes.**

## 4. Install App to Workspace

- **Navigate** 
    ```
     Settings > Basic information > Install your app.
    ```
- **Click Install to workspace.**
- **Navigate**
    ```
     Features > OAuth & permissions > OAuth Tokens for Your Workspace.
    ```
- **Click Install to workspace.**

## 5. Configure OAuth & Permissions [OPTIONAL STEP]

- **Add a new redirect URL (https://integrator.io/connection/oauth2callback).**
- **Save the redirect URL.**
- **Add OAuth scopes for both bot and user tokens.**

## 6. Manage Distribution
- **Add OAuth scopes for both bot and user tokens.**
   ### Required Scopes

    Make sure to add the following scopes to your app:

    - ``channels:history`` - View messages and other content in a user’s public channels
    - ``channels:read`` - View basic information about public channels in a workspace
    - ``groups:history`` - View messages and other content in a user’s private channels
    - ``groups:read`` - View basic information about a user’s private channels
    - ``im:history`` - View messages and other content in a user’s direct messages
    - ``im:read`` - View basic information about a user’s direct messages
    - ``mpim:history`` - View messages and other content in a user’s group direct messages
    - ``mpim:read`` - View basic information about a user’s group direct messages
    - ``users:read`` - View people in a workspace 

    Scroll back to the top of this page and look for the button that says ``Install App to Workspace`` (or ``Reinstall App`` if you've done this before). Click it. You'll now see a permission request screen to **install your app to its original workspace.**
- **Navigate**
    ```
     Settings > Manage distribution.
     ```
- **Verify all fields in Share Your App with Other Workspaces.**
- **Click Activate public distribution.**

## 7. Retrieve Slack OAuth Token

- **Navigate to Slack API:** [Slack API](https://api.slack.com/apps)
- **Click Your apps in the top right corner and select the application.**
- **Navigate**
    ```
    Features > OAuth & permissions > OAuth Tokens for Your Workspace.
    ```
- **Copy the required token (User ``OAuth token`` or ``Bot user OAuth token``).**

Now, the Slack Message  app is set up and ready to analyze messages exchanged between users on Slack.


## 1. Install Dependencies

Ensure you have Python and pip installed.
If you don't have Python installed, you can download it from [python.org](https://www.python.org/).

## 2. SETUP the environment 
- We set Up the ``pipenv`` environment 
- ``cd ``moved to Specified Location.where the project exist in the  > **TERMINAL/CMD**
- RUN the Command 
    ```
        pipenv install 
    ```
    - - Environment is Created 

- RUN the Command to activate the Environment.

    ```
        pipenv shell
    ```
## 3. Configure the Script
Python script is created Now configure it with your Slack app token and user details:

- Replace ``Enter the Copied APP token`` with your actual Slack OAuth token.
    ```
    SLACK_TOKEN ='Enter the Copied APP token '
    ```
- Replace ``Profile Name`` with the real names of the users you want to track.
    ```
    # Usernames for the users
    FIRST_USERNAME = "Profile Name"
    SECOND_USERNAME = "Profile name"
    ```
- Replace ["Channel_ID"] with the actual channel IDs from which you want to fetch messages.
    ```
    SPECIFIED_CHANNELS = ["Channel_ID"]  # Add your channel IDs here
    ```
    ``You can add more than one Channel ID's`` Separated By Comma

## 4. RUN THE SCRIPT
- Simply Run the Command 
- - Execute your Python script to start fetching messages
    ```
    python your_script_name.py
    ```
## 5. Response
- You will get The response in the ``Terminal / CMD `` 
- the ``Related Channel Messages`` Saved in the folder name ``messages/``with separate files Accordingly