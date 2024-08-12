from ..forms import genderaddForm
from ..models import gender_info
from django.shortcuts import render, redirect


def gender_add(request,registration_id=0):
    if request.method == "GET":
        if registration_id == 0:
            form = genderaddForm()
        else:
            reg=gender_info.objects.get(pk=registration_id)
            form = genderaddForm(instance=reg)

        context={
                'form':form,
                }
        return render(request, "tt_html/gender.html",context)
    else:
        if registration_id == 0:
            form = genderaddForm(request.POST)
        else:
            reg = gender_info.objects.get(pk=registration_id)
            form = genderaddForm(request.POST,instance=reg)

        if form.is_valid():
            form.save()
        return redirect('/tt_project/gender_add')