import os, slackclient, time
import random

# delay in seconds before checking for new events
SOCKET_DELAY = 1
# slackbot environment variables
COUPON_BOT_SLACK_NAME = os.environ.get('COUPON_BOT_SLACK_NAME')
COUPON_BOT_SLACK_TOKEN = os.environ.get('COUPON_BOT_SLACK_TOKEN')
COUPON_BOT_SLACK_ID = os.environ.get('COUPON_BOT_SLACK_ID')
coupon_bot_slack_client = slackclient.SlackClient('COUPON_BOT_SLACK_TOKEN')

# how the bot is mentioned on slack
def get_mention(user):
    return '<@{user}>'.format(user=user)

coupon_bot_slack_mention = get_mention(COUPON_BOT_SLACK_ID)

def is_for_me(event):
    # TODO Implement later
    return True

def handle_message(message, user, channel):
    # TODO Implement later
    post_message(message='Hello', channel=channel)

def is_private(event):
    """Checks if private slack channel"""
    return event.get('channel').startswith('D')

def post_message(message, channel):
    coupon_bot_slack_client.api_call('chat.postMessage', channel=channel,
                          text=message, as_user=True)

def run():
    if coupon_bot_slack_client.rtm_connect():
        print('[.] Coupon Bot is ON...')
        while True:
            event_list = coupon_bot_slack_client.rtm_read()
            if len(event_list) > 0:
                for event in event_list:
                    print(event)
                    if is_for_me(event):
                        handle_message(message=event.get('text'), user=event.get('user'), channel=event.get('channel'))
            time.sleep(SOCKET_DELAY)
    else:
        print('[!] Connection to Slack failed.')

if __name__=='__main__':
    run()