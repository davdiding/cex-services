import json


def response_helper(code: int, msg: str, data: any = None):
    return {"code": code, "msg": msg, "data": data}


def get_auth_data(exchange: str, name: str) -> dict:
    auth = load_auth()
    target_auth = [i for i in auth[exchange] if i["name"] == name][0]
    del target_auth["name"]
    return target_auth


def load_auth():
    with open("auth.json", "r") as f:
        return json.load(f)
