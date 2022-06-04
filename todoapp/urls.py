from django.urls import path
from todoapp import views

urlpatterns=[
    path("add",views.TodoCreateView.as_view(),name="addtodo"),
    path('all',views.TodoListView.as_view(),name='alltodos'),
    path("find",views.TodoFindView.as_view(),name="findtodo"),
    path("details/<int:id>",views.TodoDetailView.as_view(),name="tododetail"),
    path("change/<int:id>",views.TodoEditView.as_view(),name="todoedit"),
    path("remove/<int:id>",views.TodoDeleteView.as_view(),name="removetodo"),
    path('accounts/signup',views.SignUpView.as_view(),name='signup'),
    path('',views.SignInView.as_view(),name="sign-in"),
    path('accounts/signout',views.signout,name='signout'),
    path('profile',views.ProfileCreateView.as_view(),name='profile'),
    path('view_pro/<int:id>',views.ViewProfile.as_view(),name='view-pro')
]