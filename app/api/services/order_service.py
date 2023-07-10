
def create_order(gateway, order):
    try:
        response = gateway.put_new_order(order)
        return response

    except Exception as e:
        return str(e)
