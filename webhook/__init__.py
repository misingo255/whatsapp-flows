import os
from dotenv import load_dotenv
from whatsapp_flows import FlowsManager
from fastapi import Request, status, BackgroundTasks, Response, FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware


load_dotenv()

WHATSAPP_BUSINESS_PHONE_NUMBER_ID = os.getenv("WHATSAPP_BUSINESS_PHONE_NUMBER_ID")
WHATSAPP_BUSINESS_ACCESS_TOKEN = os.getenv("WHATSAPP_BUSINESS_ACCESS_TOKEN")
WHATSAPP_BUSINESS_ACCOUNT_ID = os.getenv("WHATSAPP_BUSINESS_ACCOUNT_ID")
WHATSAPP_BUSINESS_VERIFY_TOKEN = os.getenv("WHATSAPP_BUSINESS_VERIFY_TOKEN")


flows_manager = FlowsManager(
    whatsapp_access_token=WHATSAPP_BUSINESS_ACCESS_TOKEN,
    whatsapp_account_id=WHATSAPP_BUSINESS_ACCOUNT_ID,
    whatsapp_phone_number_id=WHATSAPP_BUSINESS_PHONE_NUMBER_ID,
)


app = FastAPI()


origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


FLOW_ID = "1234567890"



@app.get("/webhook")
async def wehbook_verification(request: Request):
    if (
        request.query_params.get("hub.verify_token") == WHATSAPP_BUSINESS_VERIFY_TOKEN
        and request.query_params.get("hub.mode") == "subscribe"
    ):
        contents = request.query_params.get("hub.challenge")
        return Response(
            content=contents, media_type="text/plain", status_code=status.HTTP_200_OK
        )
    else:
        return JSONResponse(
            content="Invalid request", status_code=status.HTTP_400_BAD_REQUEST
        )


@app.post("/webhook")
async def webhook_processing(request: Request, tasks: BackgroundTasks):
    body = await request.body()
    if not body:
        return JSONResponse(
            content="NO DATA OR REQUEST RECEIVED",
            status_code=status.HTTP_400_BAD_REQUEST,
        )
    data = await request.json()
    if not data:
        return JSONResponse(
            content="NO DATA OR REQUEST RECEIVED",
            status_code=status.HTTP_400_BAD_REQUEST,
        )
    messages = data["entry"][0]["changes"][0]["value"].get("messages")
    if messages:
        text = messages[0].get("text")
        user_phone_number = data["entry"][0]["changes"][0]["value"]["contacts"][0][
            "wa_id"
        ]

        if text:
            tasks.add_task(
                    FlowsManager.send_published_flow,
                    FLOW_ID,
                    user_phone_number,
                )
        else:
            tasks.add_task(
                    FlowsManager.send_unpublished_flow,
                    FLOW_ID,
                    user_phone_number,
                )
    else:
            tasks.add_task(FlowsManager.get_flows_response, data)
    return JSONResponse(
        content="CHAT MESSAGE PROCESSED SUCCESSFULL", status_code=status.HTTP_200_OK
    )

