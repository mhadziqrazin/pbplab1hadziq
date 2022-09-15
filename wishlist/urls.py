from unicodedata import name
from django.urls import path
from wishlist.views import show_wishlist, show_wishlist_xml, show_wishlist_json, show_xml_by_id, show_json_by_id

app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
    path('xml/', show_wishlist_xml, name='show_wishlist_xml'),
    path('json/', show_wishlist_json, name='show_wishlist_json'),
    path('xml/<int:id>', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>', show_json_by_id, name='show_json_by_id'),

]