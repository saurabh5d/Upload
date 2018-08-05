from django.shortcuts import render
from django.http import HttpResponse

def Form(request):
    return render(request,"index/forms.html",{})
def Upload(request):
    for count,x in enumerate(request.FILES.getlist("files")):
        def process(f):
            with open('C:\Users\Saurabh_Dube\PycharmProjects\FileUpload\media'+'\\file_'+str(count), 'wb+') as destination:
                for chunk in f.chunks():
                    destination.write(chunk)
        process(x)
    return HttpResponse("Files Uploaded ")

# Create your views here.
