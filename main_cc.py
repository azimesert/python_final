from order_func import order_func
from order import Order

result = order_func()

if isinstance(result, list):
    order = Order(result)
    print('*' * 50)
    print(f"Your order id is: {order.order_id}")
    print(f"Your order was made on: {order.date}")
    print(f"Your order contains: {order.items}")
    print(f"Your order has {order.calories} calories")

    if order.order_accepted:
        print("Your order has been accepted!")
        print(f"Your order costs {order.price} euros")
    else:
        print("Your order has been refused!")
        print(f"Reason: {order.order_refused_reason}")
else:
    print(result)
