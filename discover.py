import os, slackclient

COUPON_BOT_SLACK_NAME = os.environ.get('COUPON_BOT_SLACK_NAME')
COUPON_BOT_SLACK_TOKEN = os.environ.get('COUPON_BOT_SLACK_TOKEN')
# initialize slack client
coupon_bot_slack_client = slackclient.SlackClient(COUPON_BOT_SLACK_TOKEN)
# check if everything is alright
print(COUPON_BOT_SLACK_NAME)
print(COUPON_BOT_SLACK_TOKEN)
is_ok = coupon_bot_slack_client.api_call("users.list").get('ok')
print(is_ok)

# find the id of our slack bot
if(is_ok):
    for user in coupon_bot_slack_client.api_call("users.list").get('members'):
        if user.get('name') == COUPON_BOT_SLACK_NAME:
            print(user.get('id'))