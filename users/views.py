from django.shortcuts import render
from django.template import Context, Template
from django.template.loader import get_template
from django.http import HttpResponse
from django.views import View
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from users.forms import UserCreationForm
from users.forms import CsvForm
from users.models import CSVModel
from wsgiref.util import FileWrapper
import pdfkit
import os

class Registration(View):
    template_name = ''
    def get(self, request):
        return render(request, self.template_name, {'form': UserCreationForm()})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('layout')
        return render(request, self.template_name, {'form':form})

class CSV(View):
    template_name = ''
    def get(self, request):
        initial={'first_name': request.user.first_name,'last_name' : request.user.last_name,'email':request.user.email}
        if len(CSVModel.objects.filter(author=request.user)) != 0:
            result = CSVModel.objects.filter(author=request.user)
            previous_value = result[0]
            initial = {'first_name':previous_value.first_name,'last_name':previous_value.last_name,
            'email':previous_value.email,'phone_number':previous_value.phone_number,'education': previous_value.education,
            'experience':previous_value.experience,'skills':previous_value.skills,'additional':previous_value.additional}
        form = CsvForm(initial)
        t = get_template("form_for_pdf.html")
        temp = str(t.render({'form':form}))
        pdfkit.from_string(temp,'output.pdf')
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = CsvForm(request.POST)
        t = get_template("form_for_pdf.html")
        temp = str(t.render({'form':form}))
        pdfkit.from_string(temp,'output.pdf')
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            result = CSVModel.objects.filter(author=request.user)
            if len(result) == 0:
                instance.save()
            else:
                result.update(first_name = instance.first_name,last_name = instance.last_name,email = instance.email,
                phone_number = instance.phone_number,education = instance.education,experience = instance.experience,
                skills = instance.skills,additional = instance.additional)
            return render(request, self.template_name, {'form':form})
        return render(request, self.template_name, {'form':form})

def download_pdf(request):
    filename = 'output.pdf'
    file = open(filename,'rb')
    content = FileWrapper(file)
    response = HttpResponse(content=content, content_type='application/pdf')
    response['Content-Length'] = os.path.getsize(filename)
    response['Content-Disposition'] = 'attachment; filename= '+f"{request.user.first_name}_{request.user.last_name}_CV.pdf"
    return response
