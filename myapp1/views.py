from django.shortcuts import render

from myapp1.forms import EmpSignInForm


def emphome(request):
    if request.method=="POST":
        form=EmpSignInForm(request.POST)
        if form.is_valid():
            print('Form Validation is done')
            print('Your full name is :',form.cleaned_data['fullname'])
            print('Your age is :',form.cleaned_data['age'])
            print('Your city is :',form.cleaned_data['city'])
            print('Your email is : ',form.cleaned_data['email'])
            print('Your password is: ', form.cleaned_data['password'])
            print('Your address is :',form.cleaned_data['address'])
    form=EmpSignInForm()
    return render (request,'empsignin.html',{'form':form})

