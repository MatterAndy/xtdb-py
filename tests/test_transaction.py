import json

from xtdb.session import Operation, OperationType, Transaction


def test_transaction_json(valid_time):
    transaction = Transaction()
    transaction.add(Operation(type=OperationType.FN, value={"xt/id": "value"}, valid_time=valid_time))
    transaction.add(Operation(type=OperationType.MATCH, value={"xt/id": "value"}, valid_time=valid_time))
    transaction.add(Operation(type=OperationType.DELETE, value={"xt/id": "value"}, valid_time=valid_time))
    transaction.add(Operation(type=OperationType.PUT, value={"xt/id": "value"}, valid_time=valid_time))
    transaction.add(Operation(type=OperationType.EVICT, value={"xt/id": "value"}, valid_time=valid_time))

    assert json.loads(transaction.json()) == json.loads(
        f"""{{"tx-ops": [
        ["fn", {{"xt/id": "value"}}, "{valid_time.isoformat()}"],
        ["match", "value", {{"xt/id": "value"}}, "{valid_time.isoformat()}"],
        ["delete", {{"xt/id": "value"}}, "{valid_time.isoformat()}"],
        ["put", {{"xt/id": "value"}}, "{valid_time.isoformat()}"],
        ["evict", {{"xt/id": "value"}}, "{valid_time.isoformat()}"]
]}}"""
    )