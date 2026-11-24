def authorize(role):
    return role == "payment-operator"

def register(store, key, amount):
    payment = {"id": len(store) + 1, "amount": amount}
    store[key] = payment
    return payment
