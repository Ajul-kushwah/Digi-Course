from django.contrib import admin
from shop.models import Products,ProductImage ,User,Payment
from django.utils.html import format_html
##########################
from instamojo_wrapper import Instamojo
from download_products.settings import PAYMENT_API_KEY, PAYMENT_API_AUTH_TOKEN

api = Instamojo(api_key=PAYMENT_API_KEY,
                auth_token=PAYMENT_API_AUTH_TOKEN,
                endpoint='https://test.instamojo.com/api/1.1/')

class ProductImageModel(admin.StackedInline):
    model = ProductImage

class ProductModel(admin.ModelAdmin):
    list_display = ['id','name','get_description','get_price','get_discount','sale_price','get_thumbnail']
    inlines = [ProductImageModel]

    def get_thumbnail(self,obj):
        return format_html(f'''
        <img src='{obj.thumbnail.url }' width='100px',height='100px' >
        ''')

    def sale_price(self,obj):
        return (obj.price)-(obj.price)*(obj.discount/100)

    def get_description(self,obj):
        return format_html(f'<span title="{obj.description}"><p>{obj.description[0:50]}</br>{obj.description[50:]}...</p></span>')

    def get_price(self,obj):
        return '₹ '+ str(obj.price)

    def get_discount(self,obj):
        return str(obj.discount)+' %'

    sale_price.short_description = 'Original Price'
    get_price.short_description = 'Price'
    get_discount.short_description = 'Discount'

class UserModel(admin.ModelAdmin):
    list_display = ['id','name','email','phone','active']
    sortable_by = ['id','name']
    list_editable = ['name','active']

class PaymentModel(admin.ModelAdmin):
    list_display = ['id','get_user',
                    'get_product',
                    'get_status',
                    'get_amount']

    def get_status(self,obj):
        response = api.payment_request_payment_status(
            obj.payment_request_id,
            obj.payment_id)
        print(response)
        obj.paymentDetails = response
        if obj.payment_status !='Failed':
            return True
        else:
            return False

    def get_amount(self,obj):
        return obj.product.price#paymentDetails['payment_request']['amount']

    def get_user(self,obj):
        return format_html(f'''
                <a target="_blank" href="/admin/shop/user/{obj.user.id}" >{obj.user}</a>
                ''' )

    def get_product(self,obj):
        return format_html(f'''
                <a target="_blank" href="/admin/shop/products/{obj.product.id}" >{obj.product}</a>
                ''' )

    get_product.short_description = 'Product'
    get_user.short_description = 'User'
    get_status.short_description = 'Status'
    get_status.boolean = True

admin.site.register(Products,ProductModel)
admin.site.register(ProductImage)
admin.site.register(User,UserModel)
admin.site.register(Payment,PaymentModel)