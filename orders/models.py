from main_app.models import *


class Affiliate(models.Model):
    pass


Discount_Type_Choices = (('fixed amount discount', 'Fixed Amount Discount'), ('percentage discount',
                                                                              'Percentage Discount'))
User_Type_Choices = (('unlimited time for all users', 'Unlimited time for all users'),
                     ('once for new user for first order', 'Once for new user for first order'),
                     ('once per user', 'Once per user'),
                     ('define custom limit per user', 'Define custom limit per user'))


class Coupon(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, null=True, blank=True)
    # affiliate = models.ForeignKey(Affiliate, on_delete=models.CASCADE, null=True, blank=True)
    # menu = models.ForeignKey(Menu, on_delete=models.CASCADE, null=True, blank=True)
    menu = ArrayField(models.IntegerField(), default=list, null=True, blank=False)
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=100, null=True, blank=True)
    code = models.CharField(max_length=100, null=True, blank=True)
    discount_type = models.CharField(max_length=100, choices=Discount_Type_Choices, null=True, blank=True)
    max_discount = models.IntegerField(null=True, blank=True)
    discount_amount = models.IntegerField(null=True, blank=True)
    expiry_date = models.DateTimeField(null=True, blank=True)
    max_usage = models.IntegerField(null=True, blank=True)
    min_subtotal = models.IntegerField(null=True, blank=True)
    subtext = models.TextField(max_length=300, null=True, blank=True)
    user_type = models.CharField(max_length=100, choices=User_Type_Choices, null=True, blank=True)
    max_use_per_user = models.IntegerField(default=1, null=True, blank=True)
    is_active = models.BooleanField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)


class Order(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, null=True, blank=True)
    coupon = models.ForeignKey(Coupon, on_delete=models.CASCADE, null=True, blank=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True, blank=True)
    guest = models.ForeignKey(Guests, on_delete=models.CASCADE, null=True, blank=True)
    is_accepted = models.BooleanField(default=False)
    is_partially_accepted = models.BooleanField(default=False)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    accepted_at = models.DateTimeField(null=True, blank=True)
    completed_at = models.DateTimeField(null=True, blank=True)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True)
    item = models.ForeignKey(Items, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.IntegerField()
    is_accepted = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)


class Promotions(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    position = models.CharField(max_length=255, null=True, blank=True)
    size = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)


class Slider(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, null=True, blank=True)
    promotion = models.ForeignKey(Promotions, on_delete=models.CASCADE, null=True, blank=True)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, null=True, blank=True)
    items = models.ForeignKey(Items, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    image = models.CharField(max_length=255, null=True, blank=True)
    url = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)


