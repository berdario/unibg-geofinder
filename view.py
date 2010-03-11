from  django.http import HttpResponse
from django.shortcuts import render_to_response
from django import forms
from geosearch import GeoSearch,DocEncoder
import simplejson

search=GeoSearch()

class SearchForm(forms.Form):
	keyword=forms.CharField(widget=forms.TextInput(attrs={'class':'push_1','placeholder':'keyword'}))
	place=forms.CharField(required=False,widget=forms.TextInput(attrs={'class':'push_3','placeholder':'place'}))
	weigth=forms.FloatField(widget=forms.TextInput(attrs={'min':'0','max':'1','value':'0.5','step':'0.02'}))
	weigth.widget.input_type='range'
	#TODO: creare custom widget per range, vedi: http://joshourisman.com/2008/11/19/custom-fields-and-widgets-django-forms/ http://www.mail-archive.com/django-users@googlegroups.com/msg76148.html http://stackoverflow.com/questions/110378/change-the-width-of-form-elements-created-with-modelform-in-django
	
def searchform(request):
	form=SearchForm()
	return render_to_response("search",locals())
	

def jsonsearch(request):
	try:
		keyword,place,weigth = request.GET['keyword'], request.GET['place'], request.GET['weigth']
	except (KeyError):
		return
	form=SearchForm({"keyword":keyword,"place":place,"weigth":weigth})
	if form.is_valid():
		try:
			result=search(keyword,place,float(weigth))
		except(ValueError):
			return
	return HttpResponse(simplejson.dumps(result,cls=DocEncoder), mimetype='application/json')
	
def icbmsearch(request):
	try:
		keyword,weigth = request.GET['keyword'], request.GET['weigth']
		icbm = request.GET['lat'], request.GET['lon']
	except (KeyError):
		return
	form=SearchForm({"keyword":keyword,"place":None,"weigth":weigth})
	if form.is_valid():
		try:
			result=search(keyword,float(icbm[0]),float(icbm[1]),float(weigth))
		except(ValueError):
			return
	return HttpResponse(simplejson.dumps(result,cls=DocEncoder), mimetype='application/json')

