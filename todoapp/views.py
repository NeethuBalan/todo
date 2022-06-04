from django.shortcuts import render,redirect
from todoapp.forms import TodoForm,UserRegistrationForm,LoginForm,TodoUpdateForm,UserProfileForm
from django.views.generic import View,ListView,DetailView,UpdateView,CreateView
from django.urls import reverse_lazy
from todoapp.models import Todos,UserProfile
from django.contrib.auth import authenticate,login,logout
from todoapp.decorators import sign_inrequired
from django.utils.decorators import method_decorator

@method_decorator(sign_inrequired,name="dispatch")
class TodoCreateView(CreateView):
    model = Todos
    form_class = TodoForm
    template_name = 'addtodo.html'
    success_url = reverse_lazy('alltodos')

    # def get(self,request,*args,**kwargs):
    #     if request.user.is_authenticated:
    #         form=TodoForm()
    #         return render(request,"addtodo.html",{"form":form})
    #     else:
    #         return redirect("sign-in")
    #
    # def post(self,request,*args,**kwargs):
    #     print(request.user.is_authenticated)
    #     form=TodoForm(request.POST)
    #     if form.is_valid():
    #
    #         form.instance.user=request.user
    #         # todo=form.save(commit=False)
    #         # todo.user=request.user
    #         # todo.save()
    #         form.save()
    #         return redirect("alltodos")
    #     else:
    #         return redirect('addtodo')
    # def save(self,commit=True):
    #     instance=super(TodoForm,self).save(commit=False)
    #     instance.user=self.request.user
    #     if commit:
    #         instance.save()
    #     return instance
    def form_valid(self, form):
          form.instance.user=self.request.user
          return super().form_valid(form)

@method_decorator(sign_inrequired,name="dispatch")
class TodoListView(ListView):
    # def get(self,request):
    #     all_todos=Todos.objects.filter(user=request.user)
    #     return render(request,'todolist.html',{'todos':all_todos})
    model = Todos
    template_name = 'todolist.html'
    context_object_name = 'todos'
    def get_queryset(self):
        return Todos.objects.filter(user=self.request.user,status=False)

class TodoFindView(View):
    def get(self,request):
        return render(request,"todo_detail.html")
    def post(self,request):
        id=int(request.POST.get("t_id"))
        todo=[todo for todo in Todos if todo["id"]==id][0]
        return render(request,"todo_detail.html",{"todo":todo})

@method_decorator(sign_inrequired,name="dispatch")
class TodoDetailView(View):
    # def get(self,request,*args,**kwargs):
    #     id=kwargs.get("id")
    #     #todo=[ todo for todo in Todos if todo["id"]==id][0]
    #     todo=Todos.objects.get(id=id)
    #     return render(request,"details.html",{"todo":todo})
    model = Todos
    template_name = 'details.html'
    context_object_name = 'todo'
    pk_url_kwarg = 'id'

class TodoEditView(View):
    def get(self,request,*args,**kwargs):
        id =kwargs.get("id")
        todo=[todo for todo in Todos if todo["id"]==id][0]
        form=TodoForm(initial={"task_name":todo["title"],
                               "user":todo["userId"],
                               "completed_status":todo["completed"]})
        return render(request,"todo_edit.html",{"form":form})

@method_decorator(sign_inrequired,name="dispatch")
class TodoDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        todo=Todos.objects.get(id=id)
        todo.delete()
        return redirect("alltodos")

@method_decorator(sign_inrequired,name="dispatch")
class TodoEditView(UpdateView):
    model = Todos
    template_name = 'todo_edit.html'
    form_class = TodoUpdateForm
    success_url = reverse_lazy('alltodos')
    pk_url_kwarg = 'id'
    # def get(self,request,*args,**kwargs):
    #     id=kwargs.get("id")
    #     todo=Todos.objects.get(id=id)
    #     form=TodoForm(instance=todo)
    #     return render(request,"todo_edit.html",{"form":form})
    # def post(self,request,*args,**kwargs):
    #     id=kwargs.get("id")
    #     todo=Todos.objects.get(id=id)
    #     form=TodoForm(request.POST,instance=todo)
    #     if form.is_valid():
    #         form.save()
    #         return redirect("alltodos")
class SignUpView(View):
    template_name='register.html'
    def get(self,request,*args,**kwargs):
        form=UserRegistrationForm()
        return render(request,self.template_name,{'form':form})
    def post(self,request,*args,**kwargs):
        form=UserRegistrationForm(request.POST)
        if not form.is_valid():
            return render(request,self.template_name,{'form':form})
        form.save()
        return redirect('sign-in')
class SignInView(View):
    def get(self,request,*args,**kwargs):
        form=LoginForm()
        return render(request,'login.html',{"form":form})
    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            user=authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                print("login success")
                return redirect("alltodos")
            else:
                print("login failed")
                return redirect("sign-in")
@sign_inrequired
def signout(request,*args,**kwargs):
    logout(request)
    return redirect('sign-in')

@method_decorator(sign_inrequired,name='dispatch')
class ProfileCreateView(CreateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = 'userprofile.html'
    success_url = reverse_lazy('alltodos')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ViewProfile(DetailView):
    model = UserProfile
    template_name = 'viewprofile.html'
    context_object_name = 'prof'
    pk_url_kwarg = 'id'