from django.contrib.auth.decorators import login_required
from ..forms import registrationaddForm
from ..models import registration_info
from django.shortcuts import render, redirect

# @login_required(login_url='login_page')
def registrion_add(request,registration_id=0):
    if request.method == "GET":
        if registration_id == 0:
            form = registrationaddForm()
        else:
            reg=registration_info.objects.get(pk=registration_id)
            form = registrationaddForm(instance=reg)

        context={
                'form':form,
                }
        return render(request, "tt_html/registration_add.html",context)
    else:
        if registration_id == 0:
            form = registrationaddForm(request.POST)
        else:
            reg = registration_info.objects.get(pk=registration_id)
            form = registrationaddForm(request.POST,instance=reg)

        if form.is_valid():
            form.save()
        # return redirect('/SMS/bay_list')
        return redirect(request.META['HTTP_REFERER'])
# List bay
# @login_required(login_url='login_page')
#def registration_list(request):
    # first_name = request.session.get('first_name')
   #context = {
        #'resgistration_list' : registration_info.objects.all(),
        # 'first_name': first_name
       # }
    #return render(request,"tt_html/registration_list.html",context)

# #Delete bay
# @login_required(login_url='login_page')
# def bay_delete(request,bay_id):
#     bay = BayInfo.objects.get(pk=bay_id)
#     bay.delete()
#     return redirect('/SMS/bay_list')