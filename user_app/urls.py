from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name='index_page'),
    path('compare',compare,name='compare'),
    path('login',login,name='login'),
    path('signup',signup,name='signup'),
    path('wishlist',wishlist,name='wishlist',)

]