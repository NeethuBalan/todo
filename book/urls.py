from django.urls import path
from book import views

urlpatterns=[
    path('add',views.BookCreateView.as_view(),name='add-book'),
    path('list',views.BookListView.as_view(),name='list-book'),
    path("detail/<int:id>",views.BookDetailView.as_view(),name="detail-book"),
    path('change/<int:id>',views.BookEditView.as_view(),name='change-book'),
    path('remove/<int:id>',views.bookdelete,name='delete-book')
]