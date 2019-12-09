import os
import sys

from flask import Flask, jsonify, request, abort, send_file
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

from fsm import TocMachine
from utils import send_text_message

load_dotenv()


machine = TocMachine(
    states=["user", "base", "flavor", "rondom", "base0", "base1", "base2", "base3", "base4", "base5", "flavor00", "flavor01", "flavor02",
            "flavor03", "flavor04", "flavor05", "flavor06", "flavor07", "flavor08", "flavor09", "flavor10", "flavor11", "flavor12"],
    transitions=[
        {
            "trigger": "advance",
            "source": "user",
            "dest": "base",
            "conditions": "is_going_to_base",
        },
        {
            "trigger": "advance",
            "source": "user",
            "dest": "flavor",
            "conditions": "is_going_to_flavor",
        },
        {
            "trigger": "advance",
            "source": "user",
            "dest": "random",
            "conditions": "is_going_to_random",
        },
        {
            "trigger": "advance",
            "source": "base",
            "dest": "base0",
            "conditions": "is_going_to_base0",
        },
        {
            "trigger": "advance",
            "source": "base",
            "dest": "base1",
            "conditions": "is_going_to_base1",
        },
        {
            "trigger": "advance",
            "source": "base",
            "dest": "base2",
            "conditions": "is_going_to_base2",
        },
        {
            "trigger": "advance",
            "source": "base",
            "dest": "base3",
            "conditions": "is_going_to_base3",
        },
        {
            "trigger": "advance",
            "source": "base",
            "dest": "base4",
            "conditions": "is_going_to_base4",
        },
        {
            "trigger": "advance",
            "source": "base",
            "dest": "base5",
            "conditions": "is_going_to_base5",
        },
        {
            "trigger": "advance",
            "source": "flavor",
            "dest": "flavor00",
            "conditions": "is_going_to_flavor00",
        },
        {
            "trigger": "advance",
            "source": "flavor",
            "dest": "flavor01",
            "conditions": "is_going_to_flavor01",
        },
        {
            "trigger": "advance",
            "source": "flavor",
            "dest": "flavor02",
            "conditions": "is_going_to_flavor02",
        },
        {
            "trigger": "advance",
            "source": "flavor",
            "dest": "flavor03",
            "conditions": "is_going_to_flavor03",
        },
        {
            "trigger": "advance",
            "source": "flavor",
            "dest": "flavor04",
            "conditions": "is_going_to_flavor04",
        },
        {
            "trigger": "advance",
            "source": "flavor",
            "dest": "flavor05",
            "conditions": "is_going_to_flavor05",
        },
        {
            "trigger": "advance",
            "source": "flavor",
            "dest": "flavor06",
            "conditions": "is_going_to_flavor06",
        },
        {
            "trigger": "advance",
            "source": "flavor",
            "dest": "flavor07",
            "conditions": "is_going_to_flavor07",
        },
        {
            "trigger": "advance",
            "source": "flavor",
            "dest": "flavor08",
            "conditions": "is_going_to_flavor08",
        },
        {
            "trigger": "advance",
            "source": "flavor",
            "dest": "flavor09",
            "conditions": "is_going_to_flavor09",
        },
        {
            "trigger": "advance",
            "source": "flavor",
            "dest": "flavor10",
            "conditions": "is_going_to_flavor10",
        },
        {
            "trigger": "advance",
            "source": "flavor",
            "dest": "flavor11",
            "conditions": "is_going_to_flavor11",
        },
        {
            "trigger": "advance",
            "source": "flavor",
            "dest": "flavor12",
            "conditions": "is_going_to_flavor12",
        },
        {
            "trigger": "go_back",
            "source": [
                "base0", "base1", "base2", "base3", "base4", "base5",
                "flavor00", "flavor01", "flavor02", "flavor03", "flavor04",
                "flavor05", "flavor06", "flavor07", "flavor08", "flavor09",
                "flavor10", "flavor11", "flavor12", "random"
            ],
            "dest": "user"
        },
    ],
    initial="user",
    auto_transitions=False,
    show_conditions=True,
)

app = Flask(__name__, static_url_path="")


# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv("LINE_CHANNEL_SECRET", None)
channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
if channel_secret is None:
    print("Specify LINE_CHANNEL_SECRET as environment variable.")
    sys.exit(1)
if channel_access_token is None:
    print("Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.")
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)


@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue

        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text=event.message.text)
        )

    return "OK"


@app.route("/webhook", methods=["POST"])
def webhook_handler():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info(f"Request body: {body}")

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue
        if not isinstance(event.message.text, str):
            continue
        print(f"\nFSM STATE: {machine.state}")
        print(f"REQUEST BODY: \n{body}")
        response = machine.advance(event)
        if response == False:
            send_text_message(event.reply_token,
                              "Recommend cocktail by base, flavor or random.")

    return "OK"


@app.route("/show-fsm", methods=["GET"])
def show_fsm():
    machine.get_graph().draw("fsm.png", prog="dot", format="png")
    return send_file("fsm.png", mimetype="image/png")


if __name__ == "__main__":
    port = os.environ.get("PORT", 8000)
    app.run(host="0.0.0.0", port=port, debug=True)
