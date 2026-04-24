import base64
import mygeotab

# GEOTAB CONFIG
GEOTAB_USER = "lmanriqu@fmi.com"
GEOTAB_PASS = "Manmurluism.0304"
GEOTAB_DB = "cerroverde"
GEOTAB_USER_ID = "b12"
GEOTAB_DEVICE_ID = "b315"

# GEOTAB FUNCTIONS
def authenticate_geotab():
    api = mygeotab.API(
        username=GEOTAB_USER,
        password=GEOTAB_PASS,
        database=GEOTAB_DB
    )
    api.authenticate()
    return api

def encode_number_to_base64(number):
    b = number.to_bytes((number.bit_length() + 7) // 8 or 1, "big")
    return base64.b64encode(b).decode("utf-8")

def send_geotab_command(api, code):
    entity = {
        "user": {"id": GEOTAB_USER_ID},
        "device": {"id": GEOTAB_DEVICE_ID},
        "messageContent": {
            "mimeType": "text",
            "channelNumber": 1,
            "data": encode_number_to_base64(code),
            "contentType": "MimeContent"
        },
        "isDirectionToVehicle": True
    }
    api.call("Add", typeName="TextMessage", entity=entity)

def apagar_prender_luces(api, accion):
    codes = {
        "apagar": 200,
        "prender": 100,
        "luces": 250
    }
    send_geotab_command(api, codes[accion])