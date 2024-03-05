from flask import Blueprint

billing_bp = Blueprint("billing", "billing_bp")


@billing_bp.get("/getBalance")
def billing_get_balance():
    return {"result": {"userBalance": "0.00"}, "requestStatus": 1}


@billing_bp.get("/getTransactions")
def billing_get_transactions():
    return {
        "result": [
            {
                "id": 1,
                "amount": -12.99,
                "invoice": 999,
                "type": "New server",
                "paymentmethod": "credits",
                "date": 1658215220,
            }
        ],
        "requestStatus": 1,
    }


@billing_bp.get("/getInvoices")
def billing_get_invoices():
    return {
        "result": [
            {
                "id": 1,
                "status": 1,
                "amount": 12.99,
                "amountdue": 0,
                "type": "create",
                "service": 999,
                "paymentmethod": "credits",
                "datepaid": 1658443734,
                "date": 1658443734,
                "duedate": 1658443734,
            }
        ],
        "requestStatus": 1,
    }


@billing_bp.get("/getInvoiceInfo/<int:invoice_id>")
def billing_get_invoice_info(invoice_id: int):
    return {
        "result": {
            "id": 1,
            "status": 1,
            "amount": 12.99,
            "amountdue": 0,
            "type": "create",
            "service": 999,
            "paymentmethod": "credits",
            "datepaid": 1658443734,
            "date": 1658443734,
            "duedate": 1658443734,
        },
        "requestStatus": 1,
    }
