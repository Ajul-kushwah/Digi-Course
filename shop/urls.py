from django.urls import path
from shop.views import index
from shop.views.profile import ProfileView
from shop.views import payment
from shop.views.orders import my_orders
from shop.views.reset_password import ResetPasswordView,PasswordResetVerification,verifyResetPasswordCode
from shop.views.downloads import downloadFreeProduct ,downloadPaidProduct
from shop.views import LoginView,SignupView,\
    sendOtpView,verifyCodeView,productDetails

from shop.middlewares.login_required_middleware import login_required
from shop.middlewares.can_not_access_after_login import cantAccessAfterLogin

urlpatterns = [
    path('', index.index, name='index'),
    path('product/<int:product_id>', login_required(productDetails), name='product_details'),

    path('login', cantAccessAfterLogin(LoginView.as_view()),name='login'),
    path('signup/', cantAccessAfterLogin(SignupView.as_view()), name='signup'),
    path('profile', ProfileView.as_view(), name='profile'),

    path('reset-password', ResetPasswordView.as_view(), name='reset_password'),
    path('reset_password_verification', PasswordResetVerification.as_view(), name='reset_password_verification'),
    path('verify-reset-password-code', verifyResetPasswordCode, name='verify-reset-password-code'),

    path('logout', index.logout, name='logout'),

    path('send-otp/', cantAccessAfterLogin(sendOtpView.as_view()), name='send-otp'),
    path('verify/', cantAccessAfterLogin(verifyCodeView.as_view()), name='verify'),


    path('free-download/<int:product_id>', downloadFreeProduct, name='free-download'),
    path('create-payment/<int:product_id>', login_required(payment.createPayment), name='create-payment'),
    path('complete-payment', payment.verifyPayment, name='complete-payment'),

    path('download/paid-product/<int:product_id>', downloadPaidProduct, name='download-paid-product'),

    path('orders', login_required(my_orders), name='orders'),
    path('all_products', index.all_products, name='all_products'),
    path('update_user', index.update_user, name='update_user'),
    path('change_password', index.change_password, name='change_password'),

    path('check_email',index.check_email,name='check_email')
]
