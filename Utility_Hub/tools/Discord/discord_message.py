# import requests

# url = "https://discord.com/api/v9/channels/1255429620614828144/messages"

# payload ={
#     "content": "Test Message"
# }

# headers ={
#     "Authorization": "EJhX6juGAoHkTe6mnY0pjRz4Y0tKJQQaHmRb6lJQ-qt52f-OPQk_uddvak6BN_Jwovul"

# }

# res = requests.post(url,payload,headers)

import requests

def send_discord_message_via_webhook(webhook_url, message):
    payload = {
        "content": message
    }
    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(webhook_url, json=payload, headers=headers)

    if response.status_code == 204:
        print(f"Message sent successfully: {message}")
    else:
        print(f"Failed to send message: {response.status_code} - {response.text}")

# Example usage
if __name__ == "__main__":
    # Replace with your bot token and channel ID
    webhook_url = 'https://discord.com/api/webhooks/1255429620614828144/EJhX6juGAoHkTe6mnY0pjRz4Y0tKJQQaHmRb6lJQ-qt52f-OPQk_uddvak6BN_Jwovul'
    message = 'Hello, Discord! the Test Message- Task Completed'
    
    send_discord_message_via_webhook(webhook_url, message)