import os


API_TOKEN = os.environ.get('COUPON_BOT_SLACK_NAME')
DEFAULT_REPLY = "Sorry but I didn't understand you"
ERRORS_TO = 'loc'

PLUGINS = [
    'slackbot.plugins',
    'mybot.plugins',
]