import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

from common.base import CHANNEL_NAME
from common.base import logger

token='xoxb-4359767954757-4362646293603-gVUJZj3QHklQMZZlynd2Ephi'


print(os.environ.get('SLACK_BOT_TOKEN'))

class Client:

    def __init__(self):
        try:
            self.s_client = WebClient(token=token)#os.environ.get('SLACK_BOT_TOKEN'))
        except KeyError:
            logger.error('BOT TOKEN NOT FOUND!')
        except SlackApiError:
            logger.error('Invalid token!')

    def send_message(self, message='Test message'):
        try:
            logger.info(f'Request to slack')
            response = self.s_client.chat_postMessage(channel=CHANNEL_NAME, text=message)
        except SlackApiError as e:
            logger.error(f'Slack request error! {e.response["error"]}')
        else:
            logger.info(f'Successfully sent message "{message}"')


if __name__ == '__main__':
    s_client = Client()
    s_client.send_message()
