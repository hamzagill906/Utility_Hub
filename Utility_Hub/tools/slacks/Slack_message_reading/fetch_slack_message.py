import os
import logging
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import json

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

SLACK_TOKEN ='Enter the Copied APP token '
if not SLACK_TOKEN:
    logger.error("Missing SLACK_OAUTH_TOKEN environment variable")
    exit(1)
#create the client 
client = WebClient(token=SLACK_TOKEN)

# Usernames for the users
FIRST_USERNAME = "Profile Name"
SECOND_USERNAME = "Profile name"

# List of specific public/private channels to fetch messages from
SPECIFIED_CHANNELS = ["Channel_ID"]  # Add your channel IDs here

# Directory to store message files
MESSAGES_DIR = "messages"
# Function to Store messages in the Separate Files
def write_messages_to_file(messages, file_name):
    try:
        with open(os.path.join(MESSAGES_DIR, file_name), "a") as file:
            json.dump(messages, file, indent=4)
            file.write("\n")
        logger.info(f"Messages written to {file_name} successfully")
    except Exception as e:
        logger.error(f"Error writing messages to file {file_name}: {e}")

# Function to get user By their Profil name 
def get_user_id_by_name(username):
    try:
        result = client.users_list()
        users = result['members']
        for user in users:
            if user['profile']['real_name'] == username:
                return user['id']
        logger.error(f"User {username} not found")
        return None
    except SlackApiError as e:
        logger.error(f"Error fetching users list: {e.response['error']}")
        return None

#fetch all the channel messages using the Slack API client.
def fetch_messages(channel_id):
    try:
        result = client.conversations_history(channel=channel_id)
        messages = result['messages']
        message_content = []
        for message in messages:
            if 'text' in message and 'user' in message:
                user_id = message['user']
                user_info = client.users_info(user=user_id)
                username = user_info['user']['real_name']
                if username == FIRST_USERNAME or username == SECOND_USERNAME:
                    message_content.append({
                        "user": username,
                        "text": message['text']
                    })
        return message_content
    except SlackApiError as e:
        logger.error(f"Error fetching messages from channel {channel_id}: {e.response['error']}")
        return []

#Function to get the Channels Name in the Workspace 
def fetch_channel_name(channel_id, is_dm=False):
    try:
        if is_dm:
            result = client.conversations_info(channel=channel_id)
            user_id = result['channel']['user']
            user_info = client.users_info(user=user_id)
            user_name = user_info['user']['real_name']
            if user_name == FIRST_USERNAME or user_name == SECOND_USERNAME:
                return user_name
            else:
                return None
        else:
            result = client.conversations_info(channel=channel_id)
            return result['channel']['name']
    except SlackApiError as e:
        logger.error(f"Error fetching channel info for {channel_id}: {e.response['error']}")
        return "Unknown"

def main():
    # Create messages directory if it doesn't exist
    os.makedirs(MESSAGES_DIR, exist_ok=True)

    # Get user IDs for the users
    first_user_id = get_user_id_by_name(FIRST_USERNAME)
    second_user_id = get_user_id_by_name(SECOND_USERNAME)

    if not first_user_id or not second_user_id:
        logger.error("Unable to fetch user IDs")
        return

    total_messages = 0
    public_private_results = []
    direct_message_results = {}

    # Fetch messages from specified public/private channels
    for channel_id in SPECIFIED_CHANNELS:
        logger.info(f"Fetching messages from channel {channel_id}")
        messages = fetch_messages(channel_id)
        write_messages_to_file(messages, f"channel_{channel_id}.json")  # Write messages to channel file
        count = len(messages)
        total_messages += count
        channel_name = fetch_channel_name(channel_id)
        public_private_results.append({
            "channel_name": channel_name,
            "message_count": count
        })

    # Fetch list of direct message channels
    try:
        im_result = client.conversations_list(types="im")
        ims = im_result['channels']
    except SlackApiError as e:
        logger.error(f"Error fetching direct messages: {e.response['error']}")
        return

    # Iterate through direct message channels and count messages between the two users
    for im in ims:
        im_id = im['id']
        logger.info(f"Fetching messages from direct message channel {im_id}")
        channel_name = fetch_channel_name(im_id, is_dm=True)
        if channel_name:
            messages = fetch_messages(im_id)
            write_messages_to_file(messages, f"dm_{channel_name}.json")  # Write messages to DM file
            count = len(messages)
            total_messages += count
            if channel_name == FIRST_USERNAME:
                direct_message_results[f"{FIRST_USERNAME} - {SECOND_USERNAME}"] = count
            else:
                direct_message_results[f"{SECOND_USERNAME} - {FIRST_USERNAME}"] = count

    # Create the final result
    final_result = {
        "public_private_channels": public_private_results,
        "direct_message_channels": [{"channel_name": list(direct_message_results.keys())[0], "message_count": list(direct_message_results.values())[0]}],
        f"Total messages exchanged between {FIRST_USERNAME} and {SECOND_USERNAME}": total_messages,
    }

    # Print results in JSON format
    print(json.dumps(final_result, indent=4))

if __name__ == "__main__":
    main()
