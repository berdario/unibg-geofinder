#!/usr/bin/env jython

import sys
sys.path.append("/home/dario/geosearch.jar")
from geotag import GeoApplication
from java.util import Vector

class GeoSearch:
	def __init__(self):
		self.searcher=GeoApplication("/home/dario/.config/geosearch/config")
	def __call__(self,keywords,place,weigth):
		return self.searcher.search(keywords,place,weigth)
		#for i in range(10):
		#	a.add(a[i])
		#return a
	def __call__(self,keywords,lat,lon,weigth):
		return self.searcher.search(keywords,lat,lon,weigth)

import simplejson
from geotag.words import GeoRefDoc


class DocEncoder(simplejson.JSONEncoder):
	def default(self,o):
		if isinstance(o,GeoRefDoc):
			if not o.title:
				o.title = "No Title"
			return {"id":o.id, "title":o.title, "description":o.description, "snippet":o.htmlSnippet, "text score":o.textScore, "sort score":o.sortScore, "distance score":o.distanceScore, "keywords":o.keywords, "dateline":o.dateline, "url":o.url, "extension":o.extension}
		if isinstance(o,Vector):
			return [element for element in o]
		return simplejson.JSONEncoder.default(self,o)
