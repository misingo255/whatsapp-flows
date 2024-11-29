import uuid
import requests


class FlowsManager:
    def __init__(
        self,
        whatsapp_access_token: str,
        whatsapp_account_id: str,
        whatsapp_phone_number_id: str,
    ):
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
        flow_base_url = f"{self.base_url}/{self.whatsapp_account_id}/flows"
        flow_creation_payload = {"name": flow_name, "categories": '["OTHER"]'}
        flow_create_response = requests.post(
            flow_base_url, headers=self.auth_header, json=flow_creation_payload
        )
        created_flow_id = flow_create_response.json().get("id")
        return created_flow_id

    def upload_flow_json(self, flow_id: str, flow_file_path: str):
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
        update_url = f"{self.base_url}/{flow_id}"
        payload = {"name": new_flow_name}
        response = requests.post(update_url, headers=self.auth_header, json=payload)
        return response

    def update_flow_json(self, flow_id: str, flow_file_path: str):
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
        simulate_url = f"{self.base_url}/{flow_id}?fields=preview.invalidate(false)"
        response = requests.get(simulate_url, headers=self.auth_header)
        return response

    def delete_flow(self, flow_id: str):
        delete_url = f"{self.base_url}/{flow_id}"
        response = requests.delete(delete_url, headers=self.auth_header)
        return response

    def list_flows(self):
        list_url = f"{self.base_url}/{self.whatsapp_account_id}/flows"
        response = requests.get(list_url, headers=self.auth_header)
        return response

    def get_flow_details(self, flow_id: str):
        details_url = (
            f"{self.base_url}/{flow_id}"
            "?fields=id,name,categories,preview,status,validation_errors,"
            "json_version,data_api_version,endpoint_uri,whatsapp_business_account,"
            "application,health_status"
        )
        response = requests.get(details_url, headers=self.auth_header)
        return response

    def get_flow_assets(self, flow_id: str):
        assets_url = f"{self.base_url}/{flow_id}/assets"
        response = requests.get(assets_url, headers=self.auth_header)
        return response

    def deprecate_flow(self, flow_id: str):
        deprecate_url = f"{self.base_url}/{flow_id}/deprecate"
        response = requests.post(deprecate_url, headers=self.auth_header)
        return response
