import os
from dotenv import load_dotenv
from whatsapp_flows import FlowsManager

load_dotenv()

WHATSAPP_BUSINESS_PHONE_NUMBER_ID = os.getenv("WHATSAPP_BUSINESS_PHONE_NUMBER_ID")
WHATSAPP_BUSINESS_ACCESS_TOKEN = os.getenv("WHATSAPP_BUSINESS_ACCESS_TOKEN")
WHATSAPP_BUSINESS_ACCOUNT_ID = os.getenv("WHATSAPP_BUSINESS_ACCOUNT_ID")


flows_manager = FlowsManager(
    whatsapp_access_token=WHATSAPP_BUSINESS_ACCESS_TOKEN,
    whatsapp_account_id=WHATSAPP_BUSINESS_ACCOUNT_ID,
    whatsapp_phone_number_id=WHATSAPP_BUSINESS_PHONE_NUMBER_ID,
)

try:
    response = flows_manager.send_unpublished_flow(
        flow_id="1234567890",
        flow_cta_header_text="Amazing Shop!!",
        flow_cta_body_text="Hello, welcome to our general shop!!",
        flow_cta_footer_text="Click the button to continue.",
        flow_cta_button_text="START SHOPPING",
        recipient_phone_number="255753456789",
    )
    print(response)
except Exception as e:
    print(e)
