from rest_framework.views import APIView
from .chargebee_functions import create_customer, get_item_price, hosted_checkout, retrieve_hosted_page
from rest_framework import status
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated


def custom_response(status, data=[], message=""):
    if status == 404:
        if not message:
            message = "Data not found."
        context = {
            "status": status,
            "message": message,
            "data": data
        }
    elif status == 400 or status == 202:
        error_list = list()
        if isinstance(data, str):
            message = data
            context = {
                "status": status,
                "message": message,
                "data": []
            }
        else:
            for i, j in data.items():
                j = "".join(j)
                message = f"{i}: {j}"
                error_list.append(message)

            context = {
                "status": status,
                "message": ", ".join(error_list),
                "data": []
            }
    elif status == 409:
        context = {
            "status": status,
            "message": "Already exists",
            "data": []
        }
    else:
        context = {
            "status": status,
            "message": message,
            "data": data
        }
    return context


class CreateCustomer(APIView):
    permission_classes = [IsAuthenticated, ]

    def post(self, request):
        try:
            name = request.data.get("name")
            email = request.data.get("email")
            customer = create_customer(name, email)
            context = custom_response(status.HTTP_201_CREATED, customer, message="Customer created successfully.")
        except Exception as error:
            context = custom_response(status.HTTP_400_BAD_REQUEST, data=str(error))

        return JsonResponse(context, safe=False, status=context.get("status"))


class GetItemPrice(APIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, request):
        try:
            item_price = get_item_price()
            context = custom_response(status.HTTP_201_CREATED, item_price, message="Items price fetched successfully.")
        except Exception as error:
            context = custom_response(status.HTTP_400_BAD_REQUEST, data=str(error))
        return JsonResponse(context, safe=False, status=context.get("status"))


class Checkout(APIView):
    permission_classes = [IsAuthenticated, ]

    def post(self, request):
        try:
            item_price_id = request.data.get("item_price_id")
            quantity = request.data.get("quantity")
            checkout = hosted_checkout(item_price_id, quantity)
            context = custom_response(status.HTTP_201_CREATED, checkout, message="Checkout url generated successfully.")
        except Exception as error:
            context = custom_response(status.HTTP_400_BAD_REQUEST, data=str(error))
        return JsonResponse(context, safe=False, status=context.get("status"))


# class RetrieveHostedPage(APIView): This feature is Handled from chargebee UI
#
#     def get(self, request):
#         try:
#             hosted_page_id = request.data.get('hosted_page_id')
#             data = retrieve_hosted_page(hosted_page_id)
#             if data.values.get("content"):
#                 payment_status = data.values.get("content").get("invoice").get("status")
#                 subscription_id = data.values.get("content").get("subscription").get("id")
#                 return_data = {"payment_status": payment_status, "subscription_id": subscription_id}
#                 context = custom_response(status.HTTP_201_CREATED, return_data,
#                                           message="Payment status generated successfully.")
#             else:
#                 context = custom_response(status.HTTP_201_CREATED, message="Payment incomplete.")
#         except Exception as error:
#             context = custom_response(status.HTTP_400_BAD_REQUEST, data=str(error))
#         return JsonResponse(context, safe=False)




