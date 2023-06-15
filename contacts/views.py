from django.shortcuts import render
from .forms import FeedBackForm
# Create your views here.


def contact(request):
    if request.method == 'POST':
        form = FeedBackForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'contact/success.html')
    else:
        form = FeedBackForm()
    return render(request, 'contacts.html', {'form': form})
