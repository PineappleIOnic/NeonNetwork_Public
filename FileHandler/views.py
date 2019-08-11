from django.shortcuts import render

from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.urls import reverse

from users.models import CustomUser as Document
from FileHandler.forms import DocumentForm
from django.contrib.auth.decorators import login_required

@login_required(login_url='/accounts/login/')
def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            p = request.user.pk
            newdoc = Document.objects.get(id=p)
            newdoc = Document(docfile = request.FILES['docfile'])
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('list'))
    else:
        form = DocumentForm() # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()
    current_user = request.user


    # Render list page with the documents and the form
    return render(request, 'list.html', {'documents': documents, 'form': form,'id':current_user.id,'pk':current_user.pk})
