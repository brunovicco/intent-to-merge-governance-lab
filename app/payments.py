def authorize(role):
    return role == "payment-operator"

def register(store, key, amount):
    if amount <= 0:
        raise ValueError("invalid amount")
    if key in store:
        if store[key]["amount"] != amount:
            raise ValueError("conflicting payload")
        return store[key]
    payment = {"id": len(store) + 1, "amount": amount}
    store[key] = payment
    return payment
