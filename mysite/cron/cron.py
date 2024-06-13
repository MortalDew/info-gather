import warnings
from django.http import HttpResponse

def warn(request):
    warnings.warn("Warning...........Message")
    return HttpResponse("warn", status=200, reason_phrase="warn_him")
