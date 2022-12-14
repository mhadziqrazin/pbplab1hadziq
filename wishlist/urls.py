from unicodedata import name
from django.urls import path
from wishlist.views import get_wishlist_ajax, show_wishlist, show_wishlist_xml, show_wishlist_json, show_xml_by_id, show_json_by_id, register, login_user, logout_user, wishlist_ajax, add_wishlist, get_wishlist_ajax

app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
    path('xml/', show_wishlist_xml, name='show_wishlist_xml'),
    path('json/', show_wishlist_json, name='show_wishlist_json'),
    path('xml/<int:id>', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('ajax/', wishlist_ajax, name='wishlist_ajax'),
    path('add_wishlist/', add_wishlist, name='add_wishlist'),
    path('get_wishlist_ajax', get_wishlist_ajax, name='get_wishlist_ajax')
]