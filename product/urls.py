from django.urls import path
from .views import ProductListView , ProductDetailView , ProductCreateView ,ProductUpdate,ProductDelete
urlpatterns = [
    path('', ProductListView.as_view() ,name='home'),
    path('detail/<int:pk>', ProductDetailView.as_view(), name='detail'),
    path('update/<int:pk>', ProductUpdate.as_view(), name='update'),
    path('delete/<int:pk>', ProductDelete.as_view(), name='delete'),
    path('create/', ProductCreateView.as_view(), name='create'),
]