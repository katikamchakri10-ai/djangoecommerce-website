from django.http import HttpResponse
from django.shortcuts import render,redirect
from.models import products
from.models import rec
from.models import pics
from.models import gusto
from.models import ment
from.models import recent
from.models import contactforms
from django.contrib import messages

def home(request):
    productsdata=products.objects.all()
    blogdata=rec.objects.all()
   
    context={
        'products':productsdata,
        'blog':blogdata,
       
    }
    return render(request,'index.html',context)

def blog(request):
    picsdata=pics.objects.all()[0]
    gustodata=gusto.objects.all()
    mentdata=ment.objects.all()
    context={
        'pics':picsdata,
        'gusto':gustodata,
        'ment':mentdata,
    }
    return render(request,'blog.html',context)

def blogpost(request):
    recentdata=recent.objects.all()
    context={
        'recent':recentdata,
    }
    return render(request,'blog-detail.html',context)

def contact(request):
    print("CONTACT VIEW FILE:", __file__)
    if request.method=="POST":
        name=request.POST.get("cf_name","").strip()
        email=request.POST.get("cf_email","").strip()
        subject=request.POST.get("cf_subject","").strip()
        message_text=request.POST.get("cf_message","").strip()
        if name and email and subject and message_text:
            contactforms.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message_text,
            )
            messages.success(request,"Thank you!,your message has been successfully submitted")
            return redirect("/#contact")
        messages.error(
            request,
            "please fill in all contact fields"

        )
    return render(request,'contact.html')