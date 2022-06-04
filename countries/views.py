from django.shortcuts import render
from django.views.generic import View
# Create your views here.
countries=[

]

class ListAllCountryNamesView(View):
    def get(self,request):
        data=countries
        return render(request,"list.html",{"countries":data})
class CountryDetailView(View):
    def get(self,request,*args,**kwargs):
        cname=kwargs.get("cname")
        country=[country for country in countries if country["name"]==cname][0]
        return render(request,"country_details.html",{"country":country})
