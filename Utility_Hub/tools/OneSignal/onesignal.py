# Import necessary modules from the OneSignal SDK
import onesignal
from onesignal.api import default_api
from onesignal.model.notification import Notification
from onesignal.model.player import Player

# Function to send a push notification using OneSignal
def send_onesignal_notification(app_id, rest_api_key, message, player_id, data):
    # Configure the OneSignal API client with the REST API key
    configuration = onesignal.Configuration(
        app_key=rest_api_key
    )
    # Create an API client instance
    with onesignal.ApiClient(configuration) as api_client:
        api_instance = default_api.DefaultApi(api_client)
        # Create a notification object with the required parameters
        notification = Notification(
            app_id=app_id,  # OneSignal app ID
            contents={'en': message},  # Notification message in English
            include_player_ids=[player_id],  # Target player ID
            data=data  # Additional data payload
        )
        try:
            # Send the notification using the OneSignal API
            response = api_instance.create_notification(notification)
            return response
        except onesignal.ApiException as e:
            # Handle API exceptions and return an error message
            error_message = "Failed to send push notification. OneSignal API error."
            return {"error": error_message, "exception": str(e)}

# Function to create a new player (device) in OneSignal
def create_onesignal_player(app_id, rest_api_key, fcm_token, device_type):
    # Configure the OneSignal API client with the REST API key
    configuration = onesignal.Configuration(
        app_key=rest_api_key,
        user_key=rest_api_key
    )
    # Create an API client instance
    with onesignal.ApiClient(configuration) as api_client:
        api_instance = default_api.DefaultApi(api_client)
        # Create a player object with the required parameters
        player = Player(
            app_id=app_id,  # OneSignal app ID
            device_type=device_type,  # Device type (e.g., Android, iOS)
            identifier=fcm_token,  # FCM token for the device
            session_count=1,  # Initial session count
            last_active=1,  # Last active timestamp
            created_at=1  # Creation timestamp
        )
        try:
            # Create the player using the OneSignal API
            api_response = api_instance.create_player(player)
            return api_response.id  # Return the player ID
        except onesignal.ApiException as e:
            # Handle API exceptions and return an error message
            error_message = "Failed to Create the Player. OneSignal API error."
            return {"error": error_message, "exception": str(e)}

# Function to send a push notification with a title using OneSignal
def send_onesignal_notification_with_title(app_id, rest_api_key, title, message, player_id, data):
    # Configure the OneSignal API client with the REST API key
    configuration = onesignal.Configuration(
        app_key=rest_api_key
    )
    # Create an API client instance
    with onesignal.ApiClient(configuration) as api_client:
        api_instance = default_api.DefaultApi(api_client)
        # Create a notification object with the required parameters
        notification = Notification(
            app_id=app_id,  # OneSignal app ID
            headings={'en': title},  # Notification title in English
            contents={'en': message},  # Notification message in English
            include_player_ids=[player_id],  # Target player ID
            data=data  # Additional data payload
        )
        try:
            # Send the notification using the OneSignal API
            response = api_instance.create_notification(notification)
            return response
        except onesignal.ApiException as e:
            # Handle API exceptions and return an error message
            error_message = "Failed to send push notification with title. OneSignal API error."
            return {"error": error_message, "exception": str(e)}