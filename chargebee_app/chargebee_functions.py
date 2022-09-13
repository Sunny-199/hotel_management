import chargebee
from decouple import config

chargebee.configure(config('API_KEY_TEST'), config('SITE_TEST'))


def get_names(names):
    name = names.split(' ')
    print(name)
    if len(name) > 1:
        first_name = name[0]
        last_name = " ".join(name[1:])
    else:
        first_name = name
        last_name = None

    return first_name, last_name


def create_customer(name, email):
    first_name, last_name = get_names(name)
    result = chargebee.Customer.create({
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
    })
    customer = result.customer
    return customer.values

# print(create_customer('19august','19august@gmail.com'))

def get_item_price(limit=2):
    list_item_price = []
    entries = chargebee.ItemPrice.list({"limit": limit})
    for entry in entries:
        item_price = entry.item_price.values
        list_item_price.append(item_price)
    return list_item_price


# print(get_item_price())


def get_item_lists(limit=2):
    entries = chargebee.Item.list({
        "limit": limit
    })
    list_items = []
    for entry in entries:
        item = entry.item.values
        list_items.append(item)
    return list_items


def get_item():
    """
    output: {'id': 'Qricle-Fixed-Subscription', 'name': 'Qricle Fixed Subscription', 'external_name': 'Qricle Fixed Subscription', 'status': 'active', 'resource_version': 1658817964546, 'updated_at': 1658817964, 'item_family_id': 'Qricle-Fixed-Pricing', 'type': 'plan', 'is_shippable': False, 'is_giftable': False, 'enabled_for_checkout': True, 'enabled_in_portal': True, 'item_applicability': 'all', 'metered': False, 'channel': 'web', 'object': 'item'}
    """
    items_list = get_item_lists(limit=4)
    # print("items_list", items_list)
    result = chargebee.Item.retrieve(items_list[0]['id'])  # TODO: get relevant item_id
    item = result.item.values
    return item


# print(get_item())


def hosted_checkout(item_price_id, quantity):
    result = chargebee.HostedPage.checkout_new_for_items({
        "subscription_items": [
            {
                "item_price_id": item_price_id,
                "quantity": quantity
            }]
    })
    hosted_page = result.hosted_page
    return hosted_page.values

# print(create_customer('testCustiomer', 'testCustomer@gmaoil.custo'))
# AzyzjDTEqLgUS8TD

def new_subscription(customer_id, item_price_id, quantity=None):
    result = chargebee.HostedPage.checkout_one_time_for_items({
        # "shipping_address": {
        #     "first_name": "John",
        #     "last_name": "Mathew",
        #     "city": "Walnut",
        #     "state": "California",
        #     "zip": "91789",
        #     "country": "US"
        # },
        "customer": {
            "id": customer_id
        },
        "item_prices": [
            {
                "item_price_id": item_price_id,
                "unit_price": 99
            }]
    })
    hosted_page = result.hosted_page
    return hosted_page

# print(new_subscription('AzyzjDTEqLgUS8TD', 'Qricle-Fixed-Subscription-INR-Monthly'))


# def portal_session():
#     result = chargebee.PortalSession.create({
#         # "redirect_url": "", # get it from hosted checkout
#         "redirect_url": "https://qricle.chargebee.com/pages/v3/I4fhfcuVEGzYEgiBorbltuFAXthLi5Y69/",
#         "customer": {
#             "id": "169lr2TDu46C4RbD"
#         }
#     })
#     portal_session = result.portal_session
#     print('this is --------->portal session',portal_session)
#     return portal_session


# print(portal_session())

# "id": "portal_AzqSMkTDtNb8TIFOM",
#     "token": "mHAUpFpvcdEyu7e6rTOwLFl8PtmGAUOLn",
#     "access_url": "https://qricle.chargebee.com/portal/v2/authenticate?token=mHAUpFpvcdEyu7e6rTOwLFl8PtmGAUOLn",
#     "status": "created",
#     "created_at": 1659934881,
#     "expires_at": 1659938481,
#     "object": "portal_session",
#     "customer_id": "AzydeKTDtJr2MRe6B",
#     "redirect_url": "https://qricle.chargebee.com/pages/v3/I4fhfcuVEGzYEgiBorbltuFAXthLi5Y69/",
#     "linked_customers": [
#         {
#             "object": "linked_customer",
#             "customer_id": "16A05hTDdONP77g7N",
#             "email": "john@test.com",
#             "has_billing_address": true,
#             "has_payment_method": false,
#             "has_active_subscription": false
#         },
#         {
#             "object": "linked_customer",
#             "customer_id": "16A05hTDdOg797gP2",
#             "email": "john@test.com",
#             "has_billing_address": true,
#             "has_payment_method": false,
#             "has_active_subscription": false
#         },
#         {
#             "object": "linked_customer",
#             "customer_id": "16A05hTDdj0BT81Ll",
#             "email": "john@test.com",
#             "has_billing_address": true,
#             "has_payment_method": false,
#             "has_active_subscription": false
#         },
#         {
#             "object": "linked_customer",
#             "customer_id": "16Bj3lTDd6onD7Xj8",
#             "email": "john@test.com",
#             "has_billing_address": true,
#             "has_payment_method": false,
#             "has_active_subscription": false
#         },
#         {
#             "object": "linked_customer",
#             "customer_id": "16Bj3lTDd6rv57Xnm",
#             "email": "john@test.com",
#             "has_billing_address": true,
#             "has_payment_method": false,
#             "has_active_subscription": false
#         }
#     ]
# }


# def get_subscription():
#     data = []
#     entries = chargebee.Subscription.list({
#         "limit": 2,
#         "item_id[in]": "['basic']"
#         })
#     for entry in entries:
#         result = {"subscription": entry.subscription, "customer": entry.customer, "card": entry.card}
#         data.append(result)

# def list_subscription():
#     entries = chargebee.Subscription.list({
#         "limit": 2    })
#     for entry in entries:
#         subscription = entry.subscription
#         customer = entry.customer
#         card = entry.card
#
#     return entries.values

# print(list_subscription())


def create_subscription(quantity=150):
    try:
        # item_obj = get_item()
        # item_id = item_obj.get('id')
        # customer_obj = create_customer()
        item_price_obj = get_item_price()
        item_price_id = item_price_obj[0].get('id')  # TODO: get relevant item_price_id
        result = chargebee.Subscription.create_with_items('169lr2TDu1qMDQP8', {
            "subscription_items": [
                {
                    "item_price_id": "Qricle-Fixed-Subscription-INR-Monthly",  # get it from the request
                    # "item_price_id": 'cbdemo_sample_plan-usd-monthly',
                    "quantity": quantity  # get from request
                }]
        })
        subscription = result.subscription
        customer = result.customer
        card = result.card
        invoice = result.invoice
        unbilled_charges = result.unbilled_charges
        print(result)
    except Exception as error:
        print(error)


# create_subscription(quantity=10)


# def get_customer_card():
#     result = chargebee.Card.retrieve("169lr2TDu46C4RbD")
#     card = result.card
#     print(card)

# print(get_customer_card())
# customer_obj = create_customer()
#
# result = chargebee.Card.retrieve('AzqKt0TDtxJxRHwE')
# card = result.card
# print(card)


# hosted page id ->  Kaitdhvcu8T3595bzjTSco6WdACTQUcdk5

# def check_status():
#     result = chargebee.HostedPage.retrieve("Kaitdhvcu8T3595bzjTSco6WdACTQUcdk5")
#     hosted_page = result.hosted_page
#     return hosted_page
#
# print(check_status())


def get_subscription():
    result = chargebee.Subscription.retrieve("169lk2TEquwvGYDc")
    # subscription = result.subscription
    # customer = result.customer
    # card = result.card
    return result
# print(get_subscription())


def hosted_page_2():
    result = chargebee.HostedPage.checkout_one_time_for_items({
        "customer": {
            "id": "169lk2TEqypwTa68"
        },
        "item_prices": [
            {
                "item_price_id": "Qricle-Fixed-Subscription-INR-Monthly",
                "unit_price": 99
            }]
    })
    hosted_page = result.hosted_page
    return hosted_page

# print(hosted_page_2())


# customer_id  169lk2TEqypwTa68
def chargebee_invoice():
    result = chargebee.Invoice.create_for_charge_items_and_charges({
        "customer_id": "169lk2TEqypwTa68",
        "item_prices": [
            {
                "item_price_id": "Qricle-Fixed-Subscription-INR-Monthly",
                "unit_price": 99
            }]
        })
    invoice = result.invoice
    return invoice


# print(chargebee_invoice())


def retrieve_hosted_page(hosted_page_id):
    result = chargebee.HostedPage.retrieve(hosted_page_id)
    hosted_page = result.hosted_page
    return hosted_page

# print(retrieve_hosted_page())