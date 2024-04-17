from django.urls import path
from . import views

urlpatterns = [
    path('',views.dashboard,name='dashboard'),
    path('login/',views.log_in,name='login'),
    # path('register/',views.register,name='register'),
    path('logout/',views.log_out,name='logout'),
    # category CRUD
    path('create-category/',views.create_category,name='create-category'),
    path('list-category/',views.list_category,name='list-category'),
    path('edit-category/<int:id>/',views.edit_category,name='edit-category'),
    path('delete-category/<int:id>/',views.delete_category,name='delete-category'),
    # Region CRUD
    path('create-region/',views.create_region,name='create-region'),
    path('list-region/',views.list_region,name='list-region'),
    path('edit-region/<int:id>/',views.edit_region,name='edit-region'),
    path('delete-region/<int:id>/',views.delete_region,name='delete-region'),
    # Post CRUD
    path('create-post/',views.create_post,name='create-post'),
    path('list-post/',views.list_post,name='list-post'),
    path('edit-post/<int:id>/',views.edit_post,name='edit-post'),
    path('delete-post/<int:id>/',views.delete_post,name='delete-post'),
]
