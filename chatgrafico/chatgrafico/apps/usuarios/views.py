from django.shortcuts import render,render_to_response
from django.template import RequestContext
import datetime
# Create your views here.
def pagina_principal(request):
	fecha=datetime.datetime.now()
	return render_to_response("principal.html",{"fecha":fecha},RequestContext(request))