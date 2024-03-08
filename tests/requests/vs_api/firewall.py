from flask import Blueprint

firewall_bp = Blueprint("firewall", "firewall_bp")


@firewall_bp.get("/getInfo/<int:service_id>")
def firewall_get_info(service_id: int):
    return {
        "result": {
            "underAttack": 0,
            "allowedReqPerSec": 0,
            "blockedReqPerSec": 0,
            "attackHistory": [
                {
                    "id": 1644557335,
                    "averagepersec": 2129,
                    "peak": 3835,
                    "percentblocked": 100,
                    "status": 1,
                    "date": 1657692270,
                    "dateEnd": 1657692324,
                },
                {
                    "id": 450431455,
                    "averagepersec": 921,
                    "peak": 2411,
                    "percentblocked": 99,
                    "status": 1,
                    "date": 1657692206,
                    "dateEnd": 1657692269,
                },
            ],
            "subdomains": [
                {
                    "id": 144,
                    "info": "example.com",
                    "uam": 1,
                    "ratelimit": 0,
                    "backend": "",
                    "date": 1649818440,
                },
                {
                    "id": 179,
                    "info": "test.example.com",
                    "uam": 0,
                    "ratelimit": 5,
                    "backend": "",
                    "date": 1650675670,
                },
            ],
        },
        "requestStatus": 1,
    }
