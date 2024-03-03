from flask import Blueprint, request

server_bp = Blueprint("servers", "server_bp")


@server_bp.get("/getList")
def server_get_list():
    return {
        "result": [
            {
                "id": 1,
                "ip": "1.2.3.4",
                "hostname": "example",
                "os": "winserv22",
                "plan": 11,
                "autorenew": 0,
                "status": 1,
                "node": "cadc1",
                "expiration": 1659402270,
                "creationdate": 1610336187,
            },
            {
                "id": 2,
                "ip": "5.6.7.8",
                "hostname": "example2",
                "os": "winserv22",
                "plan": 11,
                "autorenew": 0,
                "status": 1,
                "node": "cadc1",
                "expiration": 1659402270,
                "creationdate": 1610336187,
            },
        ],
        "requestStatus": 1,
    }


@server_bp.get("/getInfo/<int:server_id>")
def server_get_info(server_id: int):
    return {
        "result": {
            "id": 1,
            "ip": "1.2.3.4",
            "hostname": "example",
            "os": "winserv22",
            "plan": 11,
            "autorenew": 0,
            "status": 1,
            "password": "secret",
            "node": "cadc1",
            "expiration": 1659402270,
            "creationdate": 1610336187,
            "tasks": [
                {
                    "id": 1,
                    "type": "restart",
                    "status": 1,
                    "date": 1612025611,
                    "datecompleted": 1612025637,
                },
                {
                    "id": 2,
                    "type": "start",
                    "status": 1,
                    "date": 1635103639,
                    "datecompleted": 1635103661,
                },
            ],
        },
        "requestStatus": 1,
    }


@server_bp.get("/getGraphs/<int:server_id>")
def server_get_graph(server_id: int):
    return {
        "result": {
            "cpu_last_1hr": [
                {"date": 1660478550, "cpu": 1},
                {"date": 1660478612, "cpu": 1},
                {"date": 1660478671, "cpu": 1},
            ],
            "ram_last_1hr": [
                {"date": 1660478550, "ram": 4.76},
                {"date": 1660478612, "ram": 4.77},
                {"date": 1660478671, "ram": 4.76},
            ],
            "network_last_1hr": [
                {"date": 1660478550, "in": 0, "out": 0},
                {"date": 1660478612, "in": 0.16, "out": 0.11},
                {"date": 1660478671, "in": 0.15, "out": 0.09},
            ],
            "cpu_last_24hrs": [
                {"date": 1660478550, "cpu": 1},
                {"date": 1660478612, "cpu": 1},
                {"date": 1660478671, "cpu": 1},
            ],
            "ram_last_24hrs": [
                {"date": 1660478550, "ram": 4.76},
                {"date": 1660478612, "ram": 4.77},
                {"date": 1660478671, "ram": 4.76},
            ],
            "network_last_24hrs": [
                {"date": 1660478550, "in": 0, "out": 0},
                {"date": 1660478612, "in": 0.16, "out": 0.11},
                {"date": 1660478671, "in": 0.15, "out": 0.09},
            ],
        },
        "requestStatus": 1,
    }


@server_bp.get("/console/<int:server_id>")
def server_console(server_id: int):
    return {"result": {"sessionUrl": ""}, "requestStatus": 1}


# TODO: Use helper functions once implemented.
@server_bp.post("/createTask/<int:server_id>")
def server_create_task(server_id: int):
    if request.form["action"] == "reinstall":
        assert request.form["os"] in (
            "winserv22",
            "winserv20",
            "debian10",
            "ubuntu20",
            "centos9",
        )

    assert request.form["action"] in (
        "stop",
        "start",
        "restart",
        "fixnetwork",
        "changepass",
        "renewlicense",
        "reinstall",
    )
    return {"result": {"taskId": "1"}, "requestStatus": 1}


@server_bp.post("/manageAutoRenew/<int:server_id>")
def server_manage_auto_renew(server_id: int):
    assert request.form["status"] in ("0", "1")
    return {"result": {"newStatus": request.form["status"]}, "requestStatus": 1}


@server_bp.post("/updateHostname/<int:server_id>")
def server_update_hostname(server_id: int):
    assert len(request.form["hostname"]) <= 16
    return {"result": {"newHostname": request.form["hostname"]}, "requestStatus": 1}


@server_bp.post("/upgrade/<int:server_id>")
def server_upgrade(server_id: int):
    assert int(request.form["plan"]) in range(0, 13)
    return {
        "result": {"transactionPrice": "12.99", "newBalance": "0.00"},
        "requestStatus": 1,
    }


@server_bp.post("/changeIp/<int:server_id>")
def server_change_ip(server_id: int):
    return {
        "result": {"transactionPrice": "12.99", "newBalance": "0.00"},
        "requestStatus": 1,
    }


@server_bp.post("/renew/<int:server_id>")
def server_renew(server_id: int):
    assert int(request.form["time"]) <= 365
    assert int(request.form["time"]) >= 1
    return {
        "result": {
            "transactionPrice": "12.99",
            "newBalance": "0.00",
            "newExpiration": 1662014278,
        },
        "requestStatus": 1,
    }


@server_bp.post("/delete/<int:server_id>")
def server_delete(server_id: int):
    return {"result": {"taskId": "1"}, "requestStatus": 1}


# TODO: Add order parameter checking after implementing helper functions.
@server_bp.post("/order")
def server_order():
    return {
        "result": {
            "transactionPrice": "12.99",
            "newBalance": "0.00",
            "generatedInvoice": 35922,
        },
        "requestStatus": 1,
    }
