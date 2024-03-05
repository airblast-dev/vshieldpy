from flask import Blueprint

system_bp = Blueprint("system", "system_bp")


@system_bp.get("/getPlans")
def system_get_plans():
    return {
        "result": {
            "VDS": {
                "Netherlands": {
                    "1": {"status": 1},
                    "2": {"status": 1},
                    "3": {"status": 0},
                },
                "US": {"1": {"status": 1}, "2": {"status": 1}, "3": {"status": 1}},
            },
            "VDSPRO": {
                "Europe": {
                    "4": {"status": 1},
                    "5": {"status": 1},
                    "6": {"status": 1},
                    "7": {"status": 1},
                    "8": {"status": 1},
                },
                "US": {
                    "4": {"status": 1},
                    "5": {"status": 1},
                    "6": {"status": 1},
                    "7": {"status": 1},
                    "8": {"status": 1},
                },
                "Singapore": {
                    "4": {"status": 1},
                    "5": {"status": 1},
                    "6": {"status": 1},
                    "7": {"status": 1},
                    "8": {"status": 1},
                },
            },
            "VPS": {
                "UK": {
                    "9": {"status": 1},
                    "10": {"status": 1},
                    "11": {"status": 1},
                    "12": {"status": 1},
                },
                "Canada": {
                    "9": {"status": 1},
                    "10": {"status": 1},
                    "11": {"status": 1},
                    "12": {"status": 1},
                },
                "US": {
                    "9": {"status": 1},
                    "10": {"status": 1},
                    "11": {"status": 1},
                    "12": {"status": 1},
                },
            },
        },
        "requestStatus": 1,
    }


@system_bp.get("/getPendingOrders")
def pending_orders():
    return {
        "result": [
            {
                "id": 1,
                "hostname": "example",
                "plan": "VPS-XL",
                "location": "fr",
                "datePaid": 1659402270,
            },
            {
                "id": 2,
                "hostname": "example",
                "plan": "VPS-S",
                "location": "fr",
                "datePaid": 1659402270,
            },
        ],
        "requestStatus": 1,
    }


@system_bp.get("/getTaskInfo/<task_id>")
def get_task_info(task_id: int):
    return {
        "result": {
            "type": "start",
            "status": 1,
            "date": 1658528357,
            "dateCompleted": 1658528385,
        },
        "requestStatus": 1,
    }
