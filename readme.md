
# WhatsApp Flows Guide

This guide outlines the steps to create and manage WhatsApp flows using the Meta Developers platform. There are two types of WhatsApp flows:

1. **Flows with Endpoints:** These flows interact with external APIs to fetch or send dynamic data.
2. **Flows without Endpoints:** These flows operate independently and do not require external API interactions.

In this guide, we'll focus on creating a WhatsApp flow app **without endpoints**. Follow the steps below to set up your flow and deploy it successfully.

## Steps to Create a WhatsApp Flow App Without Endpoints

### 1. Create an App on Meta Developers Account
To begin, you'll need to create an app on the [Meta Developers](https://developers.facebook.com/) platform. This app will serve as the foundation for managing your WhatsApp flows.

### 2. Add a Phone Number
Add a phone number to your app. This number will be associated with your WhatsApp Business account and will be used for sending and receiving messages.

### 3. Enable Messaging Permissions
Ensure that your app has the necessary messaging permissions enabled. This is crucial for your app to interact with WhatsApp messaging features.

### 4. Create a Business on Meta Business Account
Create a business account on [Meta Business](https://business.facebook.com/). This account will link your WhatsApp Business with your Meta Developers app.

### 5. Verify Your Business
Complete the verification process for your business. This step is essential for gaining access to additional features and permissions on the Meta platform.

### 6. Request Extra/Advanced Permissions
In your Meta Developers app, request the advanced permissions required for managing WhatsApp flows. These permissions will allow your app to handle complex flow operations.

To manage WhatsApp flows via the API, you'll need the following permissions for your Meta Developers app:

1. **`whatsapp_business_management`**: This permission allows your app to manage WhatsApp Business accounts, including creating and managing flows.

2. **`whatsapp_business_messaging`**: This permission is necessary for sending and receiving messages via the WhatsApp Business API, which is crucial for flow execution.

3. **`whatsapp_business_phone_number`**: This permission allows access to the phone numbers associated with your WhatsApp Business account, which is needed for managing flows linked to specific numbers.

4. **`business_management`**: This broader permission grants access to manage business assets such as ad accounts, pages, and WhatsApp accounts.

5. **`pages_messaging`**: While not directly related to flows, this permission might be necessary if your flows interact with Facebook Pages for messaging purposes.

Ensure that your app is reviewed and approved for these permissions, as some require a business verification process. You can request these permissions through your app's settings on the [Meta Developers dashboard](https://developers.facebook.com/apps/).

### 7. Obtain Necessary Credentials
You'll need to gather the following credentials from your Meta Developers account. These will be used to configure your WhatsApp flows:

- `WHATSAPP_BUSINESS_VERIFY_TOKEN`
- `WHATSAPP_BUSINESS_PHONE_NUMBER_ID`
- `WHATSAPP_BUSINESS_ACCESS_TOKEN`
- `WHATSAPP_BUSINESS_ACCOUNT_ID`

### 8. Create a Flow on Flow Development Playground
Use the [Flow Development Playground](https://developers.facebook.com/docs/whatsapp/flows/playground/) to design your WhatsApp flow. For reference, a sample flow for the **AZAM MARINES FERRIES TICKETING** use case is provided in the `assets` folder of this project.

### 9. Deploy the Middleware/Webhook
Deploy the middleware or webhook that will handle the flow execution. This is a crucial step to ensure that your flow operates correctly with WhatsApp.

### 10. Configure the Webhook URL
Once the webhook is deployed, obtain the webhook URL and configure it in your Meta Developers account. This will link your flow with the WhatsApp messaging system.

### 11. Create a Flow with a Desired Name
Return to the Flow Development Playground and create a new flow by providing a unique name. This name will identify your flow in the system.

### 12. Upload Your Flow JSON
Upload the JSON file that defines your flow. You can use the provided sample JSON in the `assets` folder or create your own. Make sure to include the flow ID generated during the flow creation process.

### 13. Test Your Flow
Send your flow for testing. This will allow you to see how it behaves in a real-world scenario and make any necessary adjustments.

### 14. Publish Your Flow
If you're satisfied with the testing results, publish your flow. This makes it live and accessible to users.

### 15. Final Testing
After publishing, conduct a final round of testing to ensure everything is functioning as expected. This is the last step before your flow goes live for end-users.

---

For additional details on each step, refer to the official [Whatsapp Flows Documentation](https://developers.facebook.com/docs/whatsapp/flows/gettingstarted) or [Meta Developers Documentation](https://developers.facebook.com/docs/whatsapp) and the [Meta Business Help Center](https://www.facebook.com/business/help).