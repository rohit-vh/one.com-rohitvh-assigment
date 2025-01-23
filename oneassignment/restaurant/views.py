from django.shortcuts import redirect

def default_redirect(request):
    return redirect('placeorder/')