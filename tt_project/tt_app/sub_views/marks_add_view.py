from ..forms import marksaddForm
from ..models import marks_info
from django.shortcuts import render, redirect

#@login_required(login_url='login_page')

def home(request):
    return render(request,"tt_html/home.html")


def marks_add(request,registration_id=0):
    if request.method == "GET":
        if registration_id == 0:
            form = marksaddForm()
        else:
            reg=marks_info.objects.get(pk=registration_id)
            form = marksaddForm(instance=reg)

        context={
                'form':form,
                }
        return render(request, "tt_html/marks.html",context)
    else:
        if registration_id == 0:
            form = marksaddForm(request.POST)
        else:
            reg = marks_info.objects.get(pk=registration_id)
            form = marksaddForm(request.POST,instance=reg)

        if form.is_valid():
            form.save()
        return redirect('/tt_project/marks_list')
        #return redirect(request.META['HTTP_REFERER'])
def marks_list(request):
    #first_name = request.session.get('first_name')
    context = {
            'marks_list' : marks_info.objects.all(),
            #'first_name': first_name
        }
    return render(request,"tt_html/marks_list.html",context)
#Delete bay
# @login_required(login_url='login_page')
def marks_delete(request,registration_id):
    reg = marks_info.objects.get(pk=registration_id)
    reg.delete()
    return redirect('/tt_project/marks_list')