from django.shortcuts import redirect

def sign_inrequired(fn):
    def wrapper(request,*args,**kwargs):
        if request.user.is_authenticated:
            return fn(request,*args,**kwargs)
        else:
            return redirect('sign-in')
    return wrapper