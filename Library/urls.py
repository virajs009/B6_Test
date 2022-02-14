"""Library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from book import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.generic import TemplateView

urlpatterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + [
    path('admin/', admin.site.urls),
    path('home/', views.homepage, name = 'homepage'),                             # to access url using given name
    path('show-all-books/', views.show_all_books, name = 'show_all_books'),
    path('edit/<int:id>/', views.edit_data, name='edit'),
    path('delete/<int:id>/', views.delete_single_data, name='delete'),
    path('__debug__/', include('debug_toolbar.urls')),
    path('delete-all-books/', views.delete_all_data, name='delete_all_books'),
    path('soft-delete/<int:id>/', views.soft_delete_data, name='soft_delete'),
    path('soft-delete-all-books/', views.soft_delete_all_data, name='soft_delete_all_books'),
    path('show-soft-deleted-books,', views.show_soft_deleted_books, name='show_soft_deleted_books'),
    path('restore-soft-deleted-book/<int:id>/', views.restore_soft_deleted_book, name='restore_soft_deleted_book'),
    path('restore-all-soft-deleted-books/', views.restore_all_soft_deleted_books, name='restore_all_soft_deleted_books'),
    path('form-home/', views.form_home, name='form_home'),
    path('user/', views.index, name='user'),
    path('users/', views.UserListView.as_view(), name='users'),
    path('get-name/', views.get_name, name='get_name'),
    path('feedback/', views.responseform, name = 'feedback'),


    path('home-cbv/', views.HomePage.as_view(Name="ABZ"), name='home_cbv'),
    path('template-cbv/', views.CBVTemplateView.as_view(), name='template_cbv'),

    path('', include(('book.urls'), namespace='book'))
]

urlpatterns += [
    re_path(r'^aaa$', views.view_a, name='view_a'),
    re_path(r'^bbb$', views.view_b, name='view_b'),
    re_path(r'^ccc$', views.view_c, name='view_c'),
    re_path(r'^ddd$', views.view_d, name='view_d'),
]

