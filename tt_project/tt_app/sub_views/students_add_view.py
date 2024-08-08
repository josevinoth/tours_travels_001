from django.contrib.auth.decorators import login_required
from ..forms import studentsaddForm
from ..models import students_info
from django.shortcuts import render, redirect

# @login_required(login_url='login_page')
def students_add(request,registration_id=0):
    if request.method == "GET":
        if registration_id == 0:
            form = studentsaddForm()
        else:
            reg=students_info.objects.get(pk=registration_id)
            form = studentsaddForm(instance=reg)

        context={
                'form':form,
                }
        return render(request, "tt_html/students_add.html",context)
    else:
        if registration_id == 0:
            form = studentsaddForm(request.POST)
        else:
            reg = students_info.objects.get(pk=registration_id)
            form = studentsaddForm(request.POST,instance=reg)

        if form.is_valid():
            form.save()
        return redirect(request.META['HTTP_REFERER'])
# # List bay
# @login_required(login_url='login_page')
# def bay_list(request):
#     first_name = request.session.get('first_name')
#     context = {'bay_list' : BayInfo.objects.all(),'first_name': first_name}
#     return render(request,"asset_mgt_app/bay_list.html",context)
#
# #Delete bay
# @login_required(login_url='login_page')
# def bay_delete(request,bay_id):
#     bay = BayInfo.objects.get(pk=bay_id)
#     bay.delete()
#     return redirect('/SMS/bay_list')