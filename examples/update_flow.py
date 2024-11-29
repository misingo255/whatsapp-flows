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
    response = flows_manager.update_flow(flow_id="1234567890", new_flow_name="NEW FLOW NAME")
    print(response)
except Exception as e:
    print(e)
