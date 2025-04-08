from onesignal import send_onesignal_notification
from celery import shared_task
"""
This module contains a Celery task for sending notifications using OneSignal.
Functions:
    send_onesignal_notification_task(app_id, rest_api_key, message, player_id, data):
        A Celery task that sends a notification using the OneSignal API.
Dependencies:
    - onesignal: A module that provides the `send_onesignal_notification` function.
    - shared_task: A decorator from Celery to define asynchronous tasks.
"""


@shared_task(name='send_onesignal_notification_task')
def send_onesignal_notification_task(app_id, rest_api_key, message, player_id, data):
    send_onesignal_notification(app_id, rest_api_key, message, player_id, data)
    