import uuid
import requests
from typing import Dict, Any
import json


class FlowsManager:
    def __init__(
        self,
        whatsapp_access_token: str,
        whatsapp_account_id: str,
        whatsapp_phone_number_id: str,
    ):
        """
        Initialize the FlowsManager with WhatsApp API credentials.

        Args:
            whatsapp_access_token (str): Access token for WhatsApp API authentication
            whatsapp_account_id (str): WhatsApp Business Account ID
            whatsapp_phone_number_id (str): WhatsApp Phone Number ID

        Examples:
        >>> flows_manager = FlowsManager(
        ...     whatsapp_access_token='your_access_token',
        ...     whatsapp_account_id='your_account_id',
        ...     whatsapp_phone_number_id='your_phone_number_id'
        ... )
        """
        self.whatsapp_access_token = whatsapp_access_token
        self.whatsapp_account_id = whatsapp_account_id
        self.whatsapp_phone_number_id = whatsapp_phone_number_id
        self.auth_header = {"Authorization": f"Bearer {self.whatsapp_access_token}"}
        self.messaging_headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.whatsapp_access_token}",
        }
        self.base_url = "https://graph.facebook.com/v20.0"

    def create_flow(self, flow_name: str):
        """
        Create a new flow in WhatsApp.

        Args:
            flow_name (str): Name of the flow to be created

        Returns:
            str: ID of the created flow

        Examples:
        >>> flows_manager = FlowsManager(...)
        >>> flow_id = flows_manager.create_flow('My New Flow')
        >>> print(flow_id)  # Prints the ID of the newly created flow
        """
        flow_base_url = f"{self.base_url}/{self.whatsapp_account_id}/flows"
        flow_creation_payload = {"name": flow_name, "categories": '["OTHER"]'}
        flow_create_response = requests.post(
            flow_base_url, headers=self.auth_header, json=flow_creation_payload
        )
        created_flow_id = flow_create_response.json().get("id")
        return created_flow_id

    def upload_flow_json(self, flow_id: str, flow_file_path: str):
        """
        Upload a JSON file for a specific flow.

        Args:
            flow_id (str): ID of the flow to upload JSON for
            flow_file_path (str): Path to the JSON file to be uploaded

        Returns:
            requests.Response: Response from the upload request

        Examples:
        >>> flows_manager = FlowsManager(...)
        >>> flow_id = flows_manager.create_flow('My Flow')
        >>> response = flows_manager.upload_flow_json(flow_id, 'path/to/flow.json')
        >>> print(response.status_code)  # Checks the upload status
        """
        graph_assets_url = f"{self.base_url}/{flow_id}/assets"
        flow_asset_payload = {"name": flow_file_path, "asset_type": "FLOW_JSON"}
        files = {
            "file": (flow_file_path, open(flow_file_path, "rb"), "application/json")
        }
        response = requests.post(
            graph_assets_url,
            headers=self.auth_header,
            data=flow_asset_payload,
            files=files,
        )
        return response

    def publish_flow(self, flow_id: str):
        """
        Publish a specific flow.

        Args:
            flow_id (str): ID of the flow to publish

        Returns:
            requests.Response: Response from the publish request

        Examples:
        >>> flows_manager = FlowsManager(...)
        >>> flow_id = flows_manager.create_flow('My Flow')
        >>> flows_manager.upload_flow_json(flow_id, 'path/to/flow.json')
        >>> response = flows_manager.publish_flow(flow_id)
        >>> print(response.status_code)  # Checks the publish status
        """
        flow_publish_url = f"{self.base_url}/{flow_id}/publish"
        response = requests.post(flow_publish_url, headers=self.auth_header)
        return response

    def send_published_flow(
        self,
        flow_id: str,
        flow_cta_header_text: str,
        flow_cta_body_text: str,
        flow_cta_footer_text: str,
        flow_cta_button_text: str,
        flow_first_screen_name: str,
        recipient_phone_number: str,
    ):
        """
        Send a published flow message to a recipient.

        Args:
            flow_id (str): ID of the published flow
            flow_cta_header_text (str): Header text for the flow message
            flow_cta_body_text (str): Body text for the flow message
            flow_cta_footer_text (str): Footer text for the flow message
            flow_cta_button_text (str): Text for the flow action button
            flow_first_screen_name (str): Name of the first screen in the flow
            recipient_phone_number (str): Phone number of the recipient

        Returns:
            requests.Response: Response from sending the flow message

        Examples:
        >>> flows_manager = FlowsManager(...)
        >>> flow_id = flows_manager.create_flow('My Flow')
        >>> flows_manager.upload_flow_json(flow_id, 'path/to/flow.json')
        >>> flows_manager.publish_flow(flow_id)
        >>> response = flows_manager.send_published_flow(
        ...     flow_id=flow_id,
        ...     flow_cta_header_text='Welcome',
        ...     flow_cta_body_text='Start your journey',
        ...     flow_cta_footer_text='Tap to begin',
        ...     flow_cta_button_text='Start',
        ...     flow_first_screen_name='welcome_screen',
        ...     recipient_phone_number='1234567890'
        ... )
        >>> print(response.status_code)  # Checks the message send status
        """
        flow_token = str(uuid.uuid4())
        flow_payload = {
            "type": "flow",
            "header": {"type": "text", "text": flow_cta_header_text},
            "body": {
                "text": flow_cta_body_text,
            },
            "footer": {"text": flow_cta_footer_text},
            "action": {
                "name": "flow",
                "parameters": {
                    "flow_message_version": "3",
                    "flow_token": flow_token,
                    "flow_id": flow_id,
                    "flow_cta": flow_cta_button_text,
                    "flow_action": "navigate",
                    "flow_action_payload": {"screen": flow_first_screen_name},
                },
            },
        }

        payload = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": str(recipient_phone_number),
            "type": "interactive",
            "interactive": flow_payload,
        }

        messaging_url = f"{self.base_url}/{self.whatsapp_phone_number_id}/messages"
        response = requests.post(
            messaging_url, headers=self.messaging_headers, json=payload
        )
        return response

    def send_unpublished_flow(
        self,
        flow_id: str,
        flow_cta_header_text: str,
        flow_cta_body_text: str,
        flow_cta_footer_text: str,
        flow_cta_button_text: str,
        flow_first_screen_name: str,
        recipient_phone_number: str,
    ):
        """
        Send an unpublished (draft) flow message to a recipient.

        Args:
            flow_id (str): ID of the unpublished flow
            flow_cta_header_text (str): Header text for the flow message
            flow_cta_body_text (str): Body text for the flow message
            flow_cta_footer_text (str): Footer text for the flow message
            flow_cta_button_text (str): Text for the flow action button
            flow_first_screen_name (str): Name of the first screen in the flow
            recipient_phone_number (str): Phone number of the recipient

        Returns:
            requests.Response: Response from sending the flow message

        Examples:
        >>> flows_manager = FlowsManager(...)
        >>> flow_id = flows_manager.create_flow('My Flow')
        >>> flows_manager.upload_flow_json(flow_id, 'path/to/flow.json')
        >>> response = flows_manager.send_unpublished_flow(
        ...     flow_id=flow_id,
        ...     flow_cta_header_text='Draft Flow',
        ...     flow_cta_body_text='Testing draft flow',
        ...     flow_cta_footer_text='Draft version',
        ...     flow_cta_button_text='Try Draft',
        ...     flow_first_screen_name='draft_screen',
        ...     recipient_phone_number='1234567890'
        ... )
        >>> print(response.status_code)  # Checks the message send status
        """
        flow_token = str(uuid.uuid4())
        flow_payload = {
            "type": "flow",
            "header": {"type": "text", "text": flow_cta_header_text},
            "body": {
                "text": flow_cta_body_text,
            },
            "footer": {"text": flow_cta_footer_text},
            "action": {
                "name": "flow",
                "parameters": {
                    "flow_message_version": "3",
                    "flow_token": flow_token,
                    "flow_id": flow_id,
                    "flow_cta": flow_cta_button_text,
                    "flow_action": "navigate",
                    "mode": "draft",
                    "flow_action_payload": {"screen": flow_first_screen_name},
                },
            },
        }

        payload = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": str(recipient_phone_number),
            "type": "interactive",
            "interactive": flow_payload,
        }

        messaging_url = f"{self.base_url}/{self.whatsapp_phone_number_id}/messages"
        response = requests.post(
            messaging_url, headers=self.messaging_headers, json=payload
        )
        return response

    def update_flow(self, flow_id: str, new_flow_name: str):
        """
        Update the name of an existing flow.

        Args:
            flow_id (str): ID of the flow to update
            new_flow_name (str): New name for the flow

        Returns:
            requests.Response: Response from the update request

        Examples:
        >>> flows_manager = FlowsManager(...)
        >>> response = flows_manager.update_flow(flow_id='123', new_flow_name='Updated Flow')
        >>> print(response.status_code)  # Checks the update status
        """
        update_url = f"{self.base_url}/{flow_id}"
        payload = {"name": new_flow_name}
        response = requests.post(update_url, headers=self.auth_header, json=payload)
        return response

    def update_flow_json(self, flow_id: str, flow_file_path: str):
        """
        Update the JSON file for an existing flow.

        Args:
            flow_id (str): ID of the flow to update
            flow_file_path (str): Path to the new JSON file

        Returns:
            requests.Response: Response from the update request

        Examples:
        >>> flows_manager = FlowsManager(...)
        >>> response = flows_manager.update_flow_json(
        ...     flow_id='123',
        ...     flow_file_path='path/to/updated_flow.json'
        ... )
        >>> print(response.status_code)  # Checks the update status
        """
        update_assets_url = f"{self.base_url}/{flow_id}/assets"
        files = {
            "file": (flow_file_path, open(flow_file_path, "rb"), "application/json")
        }
        payload = {"name": "flow.json", "asset_type": "FLOW_JSON"}
        response = requests.post(
            update_assets_url,
            headers=self.auth_header,
            files=files,
            data=payload,
        )
        return response

    def simulate_flow(self, flow_id: str):
        """
        Simulate a flow to preview its behavior.

        Args:
            flow_id (str): ID of the flow to simulate

        Returns:
            requests.Response: Response containing flow preview details

        Examples:
        >>> flows_manager = FlowsManager(...)
        >>> response = flows_manager.simulate_flow(flow_id='123')
        >>> print(response.json())  # Prints flow simulation details
        """
        simulate_url = f"{self.base_url}/{flow_id}?fields=preview.invalidate(false)"
        response = requests.get(simulate_url, headers=self.auth_header)
        return response

    def delete_flow(self, flow_id: str):
        """
        Delete a specific flow.

        Args:
            flow_id (str): ID of the flow to delete

        Returns:
            requests.Response: Response from the delete request

        Examples:
        >>> flows_manager = FlowsManager(...)
        >>> response = flows_manager.delete_flow(flow_id='123')
        >>> print(response.status_code)  # Checks the delete status
        """
        delete_url = f"{self.base_url}/{flow_id}"
        response = requests.delete(delete_url, headers=self.auth_header)
        return response

    def list_flows(self):
        """
        List all flows for the WhatsApp Business Account.

        Returns:
            requests.Response: Response containing list of flows

        Examples:
        >>> flows_manager = FlowsManager(...)
        >>> response = flows_manager.list_flows()
        >>> flows = response.json()
        >>> for flow in flows['data']:
        ...     print(flow['name'])  # Prints names of all flows
        """
        list_url = f"{self.base_url}/{self.whatsapp_account_id}/flows"
        response = requests.get(list_url, headers=self.auth_header)
        return response

    def get_flow_details(self, flow_id: str):
        """
        Get detailed information about a specific flow.

        Args:
            flow_id (str): ID of the flow to retrieve details for

        Returns:
            requests.Response: Response containing flow details

        Examples:
        >>> flows_manager = FlowsManager(...)
        >>> response = flows_manager.get_flow_details(flow_id='123')
        >>> details = response.json()
        >>> print(details['name'])  # Prints flow name
        >>> print(details['status'])  # Prints flow status
        """
        details_url = (
            f"{self.base_url}/{flow_id}"
            "?fields=id,name,categories,preview,status,validation_errors,"
            "json_version,data_api_version,endpoint_uri,whatsapp_business_account,"
            "application,health_status"
        )
        response = requests.get(details_url, headers=self.auth_header)
        return response

    def get_flow_assets(self, flow_id: str):
        """
        Retrieve assets associated with a specific flow.

        Args:
            flow_id (str): ID of the flow to retrieve assets for

        Returns:
            requests.Response: Response containing flow assets

        Examples:
        >>> flows_manager = FlowsManager(...)
        >>> response = flows_manager.get_flow_assets(flow_id='123')
        >>> assets = response.json()
        >>> for asset in assets['data']:
        ...     print(asset['name'])  # Prints names of flow assets
        """
        assets_url = f"{self.base_url}/{flow_id}/assets"
        response = requests.get(assets_url, headers=self.auth_header)
        return response

    def deprecate_flow(self, flow_id: str):
        """
        Deprecate a specific flow, marking it as no longer in active use.

        Args:
            flow_id (str): ID of the flow to deprecate

        Returns:
            requests.Response: Response from the deprecation request

        Examples:
        >>> flows_manager = FlowsManager(...)
        >>> response = flows_manager.deprecate_flow(flow_id='123')
        >>> print(response.status_code)  # Checks the deprecation status
        >>> print(response.json())  # Prints deprecation details
        """
        deprecate_url = f"{self.base_url}/{flow_id}/deprecate"
        response = requests.post(deprecate_url, headers=self.auth_header)
        return response

    def get_flows_response(self, data: Dict[Any, Any]):
        flow_response = ["entry"][0]["changes"][0]["value"]["messages"][0][
            "interactive"
        ]["nfm_reply"]["response_json"]
        flow_data = json.loads(flow_response)
        print(flow_data)
