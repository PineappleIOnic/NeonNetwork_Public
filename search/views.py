from django.shortcuts import render, HttpResponseRedirect
from search.forms import SearchForm
from users.models import CustomUser
from friendship.models import Block

# Create your views here.

def search_index(request):

        if request.method == 'POST':
            form = SearchForm(request.POST)
            if form.is_valid():
                searchquery = form.cleaned_data['searchquery']
                try:
                    user = (CustomUser.objects.filter(username__icontains=searchquery))
                    # Redirect to the document list after POST
                    if not user:
                        return render(request, 'error.html', {"reason":"We searched far and wide, but we found no-one with that name."})
                    return render(request, 'search_found.html', {'users':user})
                except Exception as e:
                    print(e)
        else:
            form = SearchForm() # A empty, unbound form

        return render(request, 'search_index.html', {'form':form})
