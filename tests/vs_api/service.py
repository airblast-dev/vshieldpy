from flask import Blueprint, request

service_bp = Blueprint("services", "service_bp")


@service_bp.get("/getList")
def get_list():
    return {
        "result": [
            {  # Hosting
                "id": 1,
                "info": "example.com",
                "status": 1,
                "expiration": 1703386437,
            },
            {  # Dedicated Server
                "id": 2,
                "info": "1.2.3.4",
                "status": 1,
                "expiration": 1764893132,
            },
        ],
        "requestStatus": 1,
    }


@service_bp.get("/getInfo/<int:service_id>")
def get_info(service_id: int):
    return {
        "result": {
            "id": 1,
            "info": "example.com",
            "status": 1,
            "expiration": 1703386437,
        },
        "requestStatus": 1,
    }


@service_bp.post("/createTask/<int:service_id>")
def create_task(service_id: int):
    return {"result": {"taskCreated": True}, "requestStatus": 1}


@service_bp.post("/manageAutoRenew/<int:service_id>")
def manage_auto_renew(service_id: int):
    status = request.form["status"]
    return {"result": {"newStatus": status}, "requestStatus": 1}


@service_bp.post("/renew/<int:service_id>")
def renew(service_id: int):
    return {
        "result": {
            "transactionPrice": "14.99",
            "newBalance": "0.00",
            "newExpiration": 1711421637,
        },
        "requestStatus": 1,
    }
