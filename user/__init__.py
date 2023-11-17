from core.sql.user_sql.user_sql import *

# creating order
def create_order(data , restaurant_id , table_id):
    order_id = data.get("orderId")
    total = data.get("Total")
    items = data.get("Items")
    print(items)
    # Extract 'Id' and 'qty' from each item
    item_ids = [item.get("Id") for item in items]
    quantities = [item.get("qty") for item in items]

    # You can now use the retrieved data in your view logic
    # 'set_order' function to process the order

    result = set_order(total, restaurant_id, item_ids, quantities, order_id, table_id)
    return result