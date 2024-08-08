from django.contrib.auth.decorators import login_required
from ..forms import registrationaddForm
from ..models import registration_info
from django.shortcuts import render, redirect

# @login_required(login_url='login_page')
def registrion_add(request,registration_id=0):
    if request.method == "GET":
        if registration_id == 0:
            print("I am inside get add")
            reg_form = registrationaddForm()
        else:
            print("I am inside get edit")
            reg=registration_info.objects.get(pk=registration_id)
            reg_form = registrationaddForm(instance=reg)

        context={
                'reg_form':reg_form,
                }
        return render(request, "tt_html/registration_add.html",context)
    else:
        if registration_id == 0:
            print("I am inside post add")
            reg_form = registrationaddForm(request.POST)
        else:
            print("I am inside post edit")
            reg = registration_info.objects.get(pk=registration_id)
            reg_form = registrationaddForm(request.POST,instance=reg)

        if reg_form.is_valid():
            reg_form.save()
        return redirect('/tt_project/registration_list')
        # return redirect(request.META['HTTP_REFERER'])
# List bay
# @login_required(login_url='login_page')
def registration_list(request):
    # first_name = request.session.get('first_name')
    context = {
        'resgistration_list' : registration_info.objects.all(),
        # 'first_name': first_name
        }
    return render(request,"tt_html/registration_list.html",context)

#Delete bay
# @login_required(login_url='login_page')
def registration_delete(request,registration_id):
    reg = registration_info.objects.get(pk=registration_id)
    reg.delete()
    return redirect('/tt_project/registration_list')