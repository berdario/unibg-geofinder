from  django.http import HttpResponse
from django.shortcuts import render_to_response
from django import forms
from geosearch import GeoSearch,DocEncoder
import simplejson
import datetime

searcher=GeoSearch()

class SearchForm(forms.Form):
	keyword=forms.CharField()
	place=forms.CharField()
	
def searchform(request):
	form=SearchForm(initial={
		"keyword":"SQL",
		"place":"Milano",
	})
	return render_to_response("searchbase",locals())
	
def search(request,place,keyword):
	form=SearchForm({"keyword":keyword,"place":place,})
	if form.is_valid():
		result=searcher.search(keyword,place)
		numrisultati=len(result)
	
	#try:
	#	keyword=request.GET['keyword']
	#	place=request.GET['place']
	#except (KeyError): pass
	return render_to_response("search",locals())
	
def searchjson(request):
	keyword,place = request.GET['keyword'], request.GET['place']
	form=SearchForm({"keyword":keyword,"place":place,})
	if form.is_valid():
		result=searcher.search(keyword,place)
	return HttpResponse(simplejson.dumps(result,cls=DocEncoder), mimetype='application/json')
