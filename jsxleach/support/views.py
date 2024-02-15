from django.shortcuts import render

# Create your views here.


def support(request):
    """
        Handles support functionality for the app
    """

    template = 'support.html'

    context = {

    }

    return render(request, template, context)
