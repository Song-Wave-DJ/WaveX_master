from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from core.encrpyt.cipher import *
from core.sql.user_sql.user_sql import *
from user import create_order


@api_view(['GET'])
def get_items(request):
    restaurant_id = request.query_params.get('restaurantId')
    table_id = request.query_params.get('tableId')
    result = get_menu_items(restaurant_id)
    return Response(result["menus"])


@api_view(['POST'])
def do_order(request):
    # Get 'restaurantId' and 'tableId' from query parameters
    restaurant_id = request.query_params.get('restaurantId')
    table_id = request.query_params.get('tableId')

    # Get JSON data from the request
    data = request.data

    # Assuming create_order returns a result
    result = create_order(data, restaurant_id, table_id)

    if result:
        return Response({"message": "Order created successfully"}, status=status.HTTP_201_CREATED)
    else:
        return Response({"message": "Order creation failed"}, status=status.HTTP_400_BAD_REQUEST)

