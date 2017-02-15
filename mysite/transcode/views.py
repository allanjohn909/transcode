from django.shortcuts import render
from django.views.generic import TemplateView
from transcode.forms import ListForm
import os



# Create your views here.    
def start(request):
    form_class = ListForm
    return render(request, 'start.html', {'form' : form_class,})

def list(request):
    listings=request.POST['list_path']
    dir_path=os.listdir(listings)
    list_dict = {'names': dir_path}
    return render(request, 'list.html', list_dict)

class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'home.html', context=None)

