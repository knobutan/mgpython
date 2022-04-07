import os
import requests
from slack_bolt import App
import logging

# Initializes your app with your bot token and signing secret
app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)

# The echo command simply echoes on command
@app.command("/mgb")
def mg(ack, command, respond):
    # Acknowledge command request
    ack()
    #Dialog
    respond(
        blocks=[
            {
                "type": "section",
                "text": {"type": "mrkdwn", "text": ":mag: *Mustgather bot: Select CI*"}
            },
            {
                "type": "actions",
                "block_id": "actionsblock1",
                "elements": [
                    {
                        "type": "static_select",
                        "placeholder": {
                            "type": "plain_text",
                            "text": "Select CI"
                        },
                        "action_id": "selectci",
                        # This option has a list of CIs
                        "options": [
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": "APIC"
                                },
                                "value": "apic"
                            },
                            {
                                "text": {
                                    "type": "plain_text",
                                	"text": "App Connect"
                                },
                                "value": "appconnect"
                            },
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": "Blockchain"
                                },
                                "value": "ibp"
                            },
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": "CF"
                                },
                                "value": "cf"
                            },
                            {
                                "text": {
                                    "type": "plain_text",
                                	"text": "Code Engine"
                                },
                                "value": "codeengine"
                            },
                            {
                                "text": {
                                    "type": "plain_text",
                                	"text": "Continuous Delivery"
                                },
                                "value": "cd"
                            },
                            {
                                "text": {
                                    "type": "plain_text",
                                	"text": "logDNA"
                                },
                                "value": "logdna"
                            },
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": "Kubernetes"
                                },
                                "value": "iks"
                            },
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": "Sysdig"
                                },
                                "value": "sysdig"
                            },
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": "Openshift"
                                },
                                "value": "ocp"
                            }
                                #,
                                #
                                # Append the same block to add a new CI
                                # Add CI ID and create the same file in the git.
                                # https://github.com/knobutan/mgrepo/tree/main
                                #
                                #{
                                #	"text": {
                                #        "type": "plain_text",
                                #		"text": "CI NAME IN THE DROPLIST"
                                #	},
                                #	"value": "XXX"
                                #}
                                #
                        ]
                    },
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": "GET"
                        },
                        "value": "getmg",
                        "action_id": "button_click"
                    }
                ]
            },
            {
                "type": "divider"
            }    
        ]
    )

# Action when you click GET button
@app.action("button_click")
def action_button_click(body, ack, respond):
    # Acknowledge the action
    ack()
    # Get the value and text
    ciname = body['state']['values']['actionsblock1']['selectci']['selected_option']['text']['text']
    ci = body['state']['values']['actionsblock1']['selectci']['selected_option']['value']
    #
    # Get MG information by REST
    # Create a new file with the same 'value' in the new CI section. 
    # It has to be the exact match
    # https://github.com/knobutan/mgrepo/tree/main
    # apic
    # ibp
    # iks
    # cf
    # repo = os.environ.get("txt_repo") + ci
    response = requests.get("https://raw.githubusercontent.com/knobutan/mgrepo/main/" + ci)
    respond(":small_blue_diamond: * MG for " + ciname + "*\n" + response.text)

@app.action("selectci")
def action_button_click(ack):
    # Acknowledge the action
    ack()

# Start your app
if __name__ == "__main__":
 app.start(port=int(os.environ.get("PORT", 8080)))
