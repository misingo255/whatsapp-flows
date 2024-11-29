import os
from dotenv import load_dotenv
from whatsapp_flows import FlowsManager

load_dotenv()

WHATSAPP_BUSINESS_PHONE_NUMBER_ID = os.getenv("WHATSAPP_BUSINESS_PHONE_NUMBER_ID")
WHATSAPP_BUSINESS_ACCESS_TOKEN = os.getenv("WHATSAPP_BUSINESS_ACCESS_TOKEN")
WHATSAPP_BUSINESS_ACCOUNT_ID = os.getenv("WHATSAPP_BUSINESS_ACCOUNT_ID")

SYSTEM_PATH = os.getcwd()
FLOW_JSON_FILE_PATH = os.path.join(SYSTEM_PATH, "data/flow.json")


flows_manager = FlowsManager(
    whatsapp_access_token=WHATSAPP_BUSINESS_ACCESS_TOKEN,
    whatsapp_account_id=WHATSAPP_BUSINESS_ACCOUNT_ID,
    whatsapp_phone_number_id=WHATSAPP_BUSINESS_PHONE_NUMBER_ID,
)

try:
    response = flows_manager.update_flow_json(
        flow_id="1234567890", flow_file_path=FLOW_JSON_FILE_PATH
    )
    print(response)
except Exception as e:
    print(e)
