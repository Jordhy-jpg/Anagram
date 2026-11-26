from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .forms import AnagramForm
from .utils import is_anagram

# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    """Render the anagram checker form and evaluate submitted pairs."""
    result = None
    if request.method == "POST":
        form = AnagramForm(request.POST)
        if form.is_valid():
            first = form.cleaned_data["first"]
            second = form.cleaned_data["second"]
            result = {
                "first": first,
                "second": second,
                "is_anagram": is_anagram(first, second),
            }
    else:
        form = AnagramForm()

    return render(request, "index.html", {"form": form, "result": result})
