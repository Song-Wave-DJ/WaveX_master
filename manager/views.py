from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view

from core.encrpyt.cipher import *
from core.sql.user_sql.user_sql import *

@api_view(['GET'])
def getWaiter(request):
    authorization_header = request.headers.get('Authorization')
    if authorization_header:
        user_id = authorization_header.split(' ')[1].strip()
        key = generate_key()
        id = decrypt_message(encode(user_id), key)
        if id:
            result = get_waiter_detail(id)
            dicts = []
            for item in result:
                dicts.append({
                    'id': item[1],
                    'name': item[2],
                    'email': item[3],
                    'password': item[4],
                    'date': item[5],
                    'phone': item[6]
                })
            return Response(dicts)
        else:
            return Response({"message": "Check access token"}, status=403)  # 403 indicates Forbidden
    else:
        return Response({"message": "Missing or invalid access token"}, status=401)  # 401 indicates Unauthorized


