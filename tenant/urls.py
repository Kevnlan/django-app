from django.urls import path

from .views import tenantsignup, ownersignup, index, create_building, edit_building, building_tenants, add_tenant, edit_building_tenants


urlpatterns = [
    path('', index, name='home'),
    path('accounts/signup/tenant/', tenantsignup, name='tenantsignup'),
    path('accounts/signup/owner/', ownersignup, name='ownersignup'),
    path('create-building', create_building, name='create_building'),
    path('add-tenant', add_tenant, name='add_tenant'),
    path('edit-building/<int:id>', edit_building, name='edit_building'),
    path('edit-building-tenants/<int:id>', edit_building_tenants, name='edit_building_tenants'),
    
    path('building-tenants/<int:building_id>', building_tenants, name='building_tenants'),
]
