
![Whatsapp Flows](assets/flows.jpg)

# WhatsApp Flows: Simplify WhatsApp Automation

## Introduction

**WhatsApp Flows** is a Python library designed to streamline the creation, management, and deployment of automated workflows for WhatsApp. Whether you're building interactive chatbots, managing business messaging, or orchestrating complex message flows, this library provides a developer-friendly toolkit for efficient WhatsApp automation.

## Why Use WhatsApp Flows?

- **Ease of Use**: Simplifies WhatsApp Business API interactions with a high-level abstraction.
- **Flexibility**: Supports creating both endpoint-based and non-endpoint flows for various use cases.
- **Scalability**: Seamlessly handles complex workflows for businesses of all sizes.
- **Integration Ready**: Works effortlessly with popular frameworks like FastAPI and Flask.

## Installation

You can install the library using `pip`:

```bash
pip install whatsapp-flows
```


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



## Full Examples WhatsApp Flows Management Guide

## Prerequisite Setup

Before performing any actions, each script follows a similar setup:
- Import necessary libraries (`os`, `dotenv`, `whatsapp_flows`)
- Load environment variables using `load_dotenv()`
- Set up environment variables for:
  - `WHATSAPP_BUSINESS_PHONE_NUMBER_ID`
  - `WHATSAPP_BUSINESS_ACCESS_TOKEN`
  - `WHATSAPP_BUSINESS_ACCOUNT_ID`
- Initialize `FlowsManager` with these credentials

```python

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

```

## Flow Management Actions

### 1. Creating a Flow
```python
flows_manager.create_flow(flow_name="TEST FLOW")
```
- Initiates a new WhatsApp flow with a specified name
- Returns flow creation response
- Useful for starting a new conversational flow or interaction

### 2. Getting Flow Details
```python
flows_manager.get_flow_details(flow_id="1234567890")
```
- Retrieves comprehensive information about a specific flow
- Requires a valid flow ID
- Helpful for checking flow configuration and status

### 3. Listing All Flows
```python
flows_manager.list_flows()
```
- Fetches a list of all existing flows
- Provides an overview of current flows in the WhatsApp Business account
- Useful for management and tracking

### 4. Updating Flow Name
```python
flows_manager.update_flow(
    flow_id="1234567890", 
    new_flow_name="NEW FLOW NAME"
)
```
- Allows renaming an existing flow
- Requires flow ID and new name
- Helpful for organizing and clarifying flow purposes

### 5. Uploading Flow JSON
```python
flows_manager.upload_flow_json(
    flow_id="1234567890", 
    flow_file_path="data/flow.json"
)
```
- Uploads a JSON configuration for a specific flow
- Requires flow ID and path to JSON file
- Used to define or modify flow structure and logic

### 6. Getting Flow Assets
```python
flows_manager.get_flow_assets(flow_id="1234567890")
```
- Retrieves all assets associated with a flow
- Includes JSON configurations and related resources
- Useful for auditing or backing up flow configurations

### 7. Publishing Flow
```python
flows_manager.publish_flow(flow_id="1234567890")
```
- Makes a flow live and ready for use
- Finalizes flow configuration
- **Important**: Once published, flow cannot be directly updated or deleted

### 8. Simulating Flow on Web
```python
flows_manager.simulate_flow(flow_id="1234567890")
```
- Provides a web-based simulation of the flow
- Helps test and preview flow behavior before actual deployment
- Useful for debugging and validation

### 9. Sending Unpublished Flow
```python
flows_manager.send_unpublished_flow(
    flow_id="1234567890",
    flow_cta_header_text="Amazing Shop!!",
    flow_cta_body_text="Welcome to our shop!",
    flow_cta_footer_text="Click to continue",
    flow_cta_button_text="START SHOPPING",
    recipient_phone_number="255753456789"
)
```
- Sends a flow that hasn't been published
- Allows testing flows with specific messaging parameters
- Requires detailed call-to-action (CTA) texts and recipient number

### 10. Sending Published Flow
```python
flows_manager.send_published_flow(
    flow_id="1234567890",
    # Similar parameters to unpublished flow
)
```
- Sends a flow that has been officially published
- Similar to unpublished flow sending, but for live flows

### 11. Updating Flow JSON
```python
flows_manager.update_flow_json(
    flow_id="1234567890", 
    flow_file_path="data/flow.json"
)
```
- Modifies the JSON configuration of a flow
- Requires flow ID and updated JSON file path
- Used to make configuration changes

### 12. Deprecating Flow
```python
flows_manager.deprecate_flow(flow_id="1234567890")
```
- Marks a published flow as deprecated
- Prevents further use without deleting historical data
- Recommended method for retiring published flows

### 13. Deleting Flow
```python
flows_manager.delete_flow(flow_id="1234567890")
```
- Removes an unpublished flow
- Cannot be used on published flows
- Permanently deletes flow configuration

## Key Considerations
- Always use environment variables for sensitive credentials
- Handle exceptions to manage potential errors
- Published flows have limited modification options
- Use simulation and careful testing before publishing



For additional details, check the ```examples``` folder in this libary or refer to the official [WhatsApp Flows Documentation](https://developers.facebook.com/docs/whatsapp/flows/gettingstarted) or [Meta Developers Documentation](https://developers.facebook.com/docs/whatsapp).