from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from home.models import Rabtaguzari, blogpost, Subjects,blogcomment
from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from home.templatetags import extras
# Create your views here.


class homeveiw(ListView):
    model = blogpost
    template_name = 'index.html'


class coldwar(ListView):
    model = blogpost
    template_name = 'coldwar.html'


def detail(request, slug):
    q = blogpost.objects.filter(slug=slug).last()
    comments= blogcomment.objects.filter(post=q, parent=None)
    replies= blogcomment.objects.filter(post=q).exclude(parent=None)
    replydict={}
    for reply in replies:
        if reply.parent.sno not in replydict.keys():
            replydict[reply.parent.sno]=[reply]
        else:
            replydict[reply.parent.sno].append(reply)
 

    all_subjects = Subjects.objects.all()
   
    context = {
         'comments': comments,
        'post': q,
        'subjects': all_subjects,
        'user':request.user,
        'replydict':replydict
    }
    return render(request, 'detail.html', context )


def about(request):
    return render(request, 'about.html')


def contact(request):
    allpost = Rabtaguzari.objects.all()
    
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Rabtaguzari(name=name, email=email, phone=phone, desc=desc,)
        contact.save()
    return render(request, 'contact.html')


def handlesignup(request):
    if request.method=='POST':
        #get parameters
      username = request.POST['username']  
      fname = request.POST['fname']
      lname = request.POST['lname']
      email = request.POST['email']
      pass1 = request.POST['pass1']
      pass2 = request.POST['pass2']

     #create user
      myuser= User.objects.create_user(username,email,pass1)
      myuser.first_name=fname
      myuser.last_name=lname
      myuser.save()
      messages.success(request,"Your Account has been Activated")   
      return redirect('coldwar')
    else:
       return HttpResponse('404-NOT FOUND')


def handlelogin(request):
      if request.method=="POST":
         loginuser= request.POST['loginuser']
         loginpass = request.POST['loginpass']

         user=authenticate(username=loginuser,password=loginpass) 

         if user is not None:
             login(request,user)
             messages.success(request,"Successfully Logged In")
             return redirect('coldwar')
         else:
            messages.error(request, "invalid Credentials Please try again!")
            return redirect('coldwar')     

      return HttpResponse('handlelogin')            


def handlelogout(request):

    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('coldwar')
    return HttpResponse('handlelogout')  

def postcomment(request):
    if request.method == "POST":
        comment=request.POST.get('comment')
        user=request.user
        postSno =request.POST.get('postSno')
        post= blogpost.objects.get(sno=postSno)
        parentSno= request.POST.get('parentSno')
        if parentSno=="":
            comment=blogcomment(comment= comment, user=user, post=post)
            comment.save()
         
        else:
            parent= blogcomment.objects.get(sno=parentSno)
            comment=blogcomment(comment= comment, user=user, post=post , parent=parent)
            comment.save()
         
    return redirect(f"/{post.slug}")