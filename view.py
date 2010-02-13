from  django.http import HttpResponse
from django.shortcuts import render_to_response
from django import forms
from geosearch import GeoSearch,DocEncoder
import simplejson

search=GeoSearch()

class SearchForm(forms.Form):
	keyword=forms.CharField()
	place=forms.CharField()
	#weigth=forms.FloatField()
	#weigth.widget.input_type='range'
	
def searchform(request):
	form=SearchForm(initial={
		"keyword":"SQL",
		"place":"Milano",
	})
	return render_to_response("search",locals())
	
def jsonsearch(request):
	try:
		keyword,place,weigth = request.GET['keyword'], request.GET['place'], request.GET['weigth']
	except (KeyError):
		return
	form=SearchForm({"keyword":keyword,"place":place,})
	if form.is_valid():
		try:
			result=search(keyword,place,float(weigth))
		except(ValueError):
			return
	return HttpResponse(simplejson.dumps(result,cls=DocEncoder), mimetype='application/json')
