from core.sql.sql import *
from datetime import datetime
def get_waiter_detail(restaurantId):
    try:
        s = sql()
        query = f"SELECT * FROM restaurant_waiter WHERE restaurant_id = '{restaurantId}' "
        result = s.Query(query)
        return result
    except Exception as e:
        # Handle the exception here, such as logging or returning an error message
        print(f"An error occurred: {e}")
        return None

def get_menu_items(restaurant_id):
    s = sql()
    try:
        query = f"SELECT * FROM menu WHERE restaurant_id = {restaurant_id}"
        result = s.Query(query)

        # Create a dictionary to store menu items categorized by their category_name
        menu_data = {
            "id": restaurant_id,
            "menus": []
        }

        # Create a dictionary to store category information
        categories = {}

        for row in result:
            category_name = row[2]  # Category name from the database

            # Check if the category is already in the categories dictionary
            if category_name not in categories:
                # If the category is not already in the dictionary, create it
                categories[category_name] = {
                    "id": "unique_category_id",  # Replace with a category ID
                    "title": category_name,
                    "menus": []
                }

            # Create a menu item
            menu_item = {
                "id": row[0],  # You may want to use a unique identifier for the menu item
                "title": row[3],  # Name of the food item
                "type": row[6],  # Type (e.g., veg or non-veg)
                "price": row[4],  # Price
                "url": row[9]  # URL to the image
            }

            # Append the menu item to the corresponding category
            categories[category_name]["menus"].append(menu_item)

        # Convert the categories dictionary into a list
        menu_data["menus"] = list(categories.values())

        return menu_data

    except Exception as e:
        # Handle the exception here, such as logging or returning an error message
        print(f"An error occurred: {e}")
        return None



def set_order(total, restaurant_id, food_ids, quantities, order_id, table_id):
    s = sql()
    flag = 0

    try:
        current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Get the current date and time
        status = 'pending'

        for i in range(len(food_ids)):
            food_id = food_ids[i]
            quantity = quantities[i]

            query = f"INSERT INTO `order` (food_id, quantity, restaurant_id, order_id, table_id, total, status, date_time) VALUES ('{food_id}', {quantity}, '{restaurant_id}', '{order_id}', '{table_id}', {total}, '{status}', '{current_datetime}')"
            s.Query(query)

            flag += 1
        query2 = f"INSERT INTO billing_history (restaurant_id, order_id, total,date_time,table_id) VALUES ( '{restaurant_id}','{order_id}','{total}','{current_datetime}','{table_id}')"
        s.Query(query2)
        s.connection.commit()
        if flag == 0:
            return "No items to add to the order."

        return "Order added successfully."

    except Exception as e:
        # Handle the exception here, such as logging or returning an error message
        print(f"An error occurred: {e}")
        return None