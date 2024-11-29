
# WhatsApp Flows Guide

This guide outlines the steps to create and manage WhatsApp flows using the Meta Developers platform. There are two types of WhatsApp flows:

1. **Flows with Endpoints:** These flows interact with external APIs to fetch or send dynamic data.
2. **Flows without Endpoints:** These flows operate independently and do not require external API interactions.

In this guide, we'll focus on creating a WhatsApp flow app **without endpoints**. Follow the steps below to set up your flow and deploy it successfully.

---

## Steps to Create a WhatsApp Flow App Without Endpoints

### 1. Create an App on Meta Developers Account
To begin, create an app on the [Meta Developers](https://developers.facebook.com/) platform. This app will serve as the foundation for managing your WhatsApp flows.

---

### 2. Add a Phone Number
Add a phone number to your app. This number will be associated with your WhatsApp Business account and used for sending and receiving messages.

---

### 3. Enable Messaging Permissions
Ensure your app has the necessary messaging permissions enabled for interacting with WhatsApp messaging features.

---

### 4. Create a Business on Meta Business Account
Create a business account on [Meta Business](https://business.facebook.com/). This links your WhatsApp Business with your Meta Developers app.

---

### 5. Verify Your Business
Complete the verification process for your business to gain access to additional features and permissions.

---

### 6. Request Advanced Permissions
Request the following advanced permissions for your Meta Developers app:

- **`whatsapp_business_management`**: Manage WhatsApp Business accounts, including creating flows.
- **`whatsapp_business_messaging`**: Send and receive messages via the WhatsApp Business API.
- **`whatsapp_business_phone_number`**: Access WhatsApp Business phone numbers.
- **`business_management`**: Manage business assets like ad accounts and pages.
- **`pages_messaging`**: Optional if flows interact with Facebook Pages for messaging.

---

### 7. Obtain Necessary Credentials
Gather the following credentials from your Meta Developers account. These will configure your WhatsApp flows:

```plaintext
WHATSAPP_BUSINESS_VERIFY_TOKEN
WHATSAPP_BUSINESS_PHONE_NUMBER_ID
WHATSAPP_BUSINESS_ACCESS_TOKEN
WHATSAPP_BUSINESS_ACCOUNT_ID
```

---

### 8. Create a Flow on Flow Development Playground
Design your WhatsApp flow using the [Flow Development Playground](https://developers.facebook.com/docs/whatsapp/flows/playground/).

To create a flow programmatically:

```python
from whatsapp_flows import FlowsManager
import os
from dotenv import load_dotenv

load_dotenv()

flows_manager = FlowsManager(
    whatsapp_access_token=os.getenv("WHATSAPP_BUSINESS_ACCESS_TOKEN"),
    whatsapp_account_id=os.getenv("WHATSAPP_BUSINESS_ACCOUNT_ID"),
    whatsapp_phone_number_id=os.getenv("WHATSAPP_BUSINESS_PHONE_NUMBER_ID"),
)

try:
    response = flows_manager.create_flow(flow_name="TEST FLOW")
    print(response)
except Exception as e:
    print(e)
```

---

### 9. Deploy the Middleware/Webhook
Deploy the middleware or webhook to handle flow execution.

---

### 10. Configure the Webhook URL
Configure the webhook URL in your Meta Developers account. This links your flow to WhatsApp messaging.

---

### 11. Create and Manage Flows

#### Listing Flows:
```python
try:
    response = flows_manager.list_flows()
    print(response)
except Exception as e:
    print(e)
```

#### Getting Flow Details:
```python
try:
    response = flows_manager.get_flow_details(flow_id="1234567890")
    print(response)
except Exception as e:
    print(e)
```

---

### 12. Upload Your Flow JSON
Upload your flow JSON using the Flow Development Playground or programmatically:

```python
SYSTEM_PATH = os.getcwd()
FLOW_JSON_FILE_PATH = os.path.join(SYSTEM_PATH, "data/flow.json")

try:
    response = flows_manager.upload_flow_json(
        flow_id="1234567890", flow_file_path=FLOW_JSON_FILE_PATH
    )
    print(response)
except Exception as e:
    print(e)
```

---

### 13. Test Your Flow
Test your flow programmatically:

```python
try:
    response = flows_manager.simulate_flow(flow_id="1234567890")
    print(response)
except Exception as e:
    print(e)
```

---

### 14. Publish Your Flow
Publish your flow:

```python
try:
    response = flows_manager.publish_flow(flow_id="1234567890")
    print(response)
except Exception as e:
    print(e)
```

---

### 15. Sending Published and Unpublished Flows

#### Send a Published Flow:
```python
try:
    response = flows_manager.send_published_flow(
        flow_id="1234567890",
        flow_cta_header_text="Amazing Shop!!",
        flow_cta_body_text="Hello, welcome to our general shop!!",
        flow_cta_footer_text="Click the button to continue.",
        flow_cta_button_text="START SHOPPING",
        recipient_phone_number="255753456789"
    )
    print(response)
except Exception as e:
    print(e)
```

#### Send an Unpublished Flow:
```python
try:
    response = flows_manager.send_unpublished_flow(
        flow_id="1234567890",
        flow_cta_header_text="Amazing Shop!!",
        flow_cta_body_text="Hello, welcome to our general shop!!",
        flow_cta_footer_text="Click the button to continue.",
        flow_cta_button_text="START SHOPPING",
        recipient_phone_number="255753456789"
    )
    print(response)
except Exception as e:
    print(e)
```

---

### 16. Update or Delete Flows

#### Update Flow JSON:
```python
try:
    response = flows_manager.update_flow_json(
        flow_id="1234567890", flow_file_path=FLOW_JSON_FILE_PATH
    )
    print(response)
except Exception as e:
    print(e)
```

#### Delete a Flow:
```python
try:
    response = flows_manager.delete_flow(flow_id="1234567890")
    print(response)
except Exception as e:
    print(e)
```

---

For additional details, check the ```examples``` folder in this libary or refer to the official [WhatsApp Flows Documentation](https://developers.facebook.com/docs/whatsapp/flows/gettingstarted) or [Meta Developers Documentation](https://developers.facebook.com/docs/whatsapp).