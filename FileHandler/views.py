from django.shortcuts import render

from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.urls import reverse

from users.models import CustomUser
from FileHandler.forms import DocumentForm
from django.contrib.auth.decorators import login_required
import os


def _delete_file(path):
   if os.path.isfile(path):
       os.remove(path)
   else:
       print("path", path, "Does not exist!")

@login_required(login_url='/accounts/login/')
def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            p = request.user.pk
            newdoc = CustomUser.objects.get(id=p)
            print("OLDDIR=", newdoc.docfile)
            _delete_file(str(newdoc.docfile))
            newdoc.docfile = (request.FILES['docfile'])
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect("../")
    else:
        form = DocumentForm() # A empty, unbound form

    # Render list page with the documents and the form
    return render(request, 'list.html', {'form': form})
