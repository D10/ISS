import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

CHANNEL_NAME = '#random'


class Client:

    def __init__(self):
        try:
            self.s_client = WebClient(token=os.environ.get('SLACK_BOT_TOKEN'))
        except KeyError:
            # logger.error('BOT TOKEN NOT FOUND!')
            print('BOT TOKEN NOT FOUND!')
        except SlackApiError:
            # logger.error('Invalid token!')
            print('Invalid token!')

    def post_message(self, message='Test message'):
        try:
            response = self.s_client.chat_postMessage(channel=CHANNEL_NAME, text=message)
        except SlackApiError as e:
            # logger.error(f'Message {message} not sent! Error {e.response["error"]}')
            print(f'Message "{message}" not sent! Error {e.response["error"]}')
        else:
            # logger.info(f'Successfully sent message {message}')
            print(f'Successfully sent message "{message}"')


if __name__ == '__main__':
    s_client = Client()
    s_client.post_message()
