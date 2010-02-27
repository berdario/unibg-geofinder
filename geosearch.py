#!/usr/bin/env jython

import sys
sys.path.append("/home/dario/geosearch.jar")
from geotag import GeoApplication
from java.util import Vector

class GeoSearch:
	def __init__(self):
		self.searcher=GeoApplication("/home/dario/.config/geosearch/config")
	def __call__(self,keywords,place,weigth):
		a = self.searcher.search(keywords,place,weigth)
		for i in range(10):
			a.add(a[i])
		return a

import simplejson
from geotag.words import GeoRefDoc


class DocEncoder(simplejson.JSONEncoder):
	def default(self,o):
		if isinstance(o,GeoRefDoc):
			if not o.docTitle:
				o.docTitle = "No Title"
			return {"name":o.nomeDoc, "title":o.docTitle, "description":o.docDescription, "snippet":o.htmlSnippet, "text score":o.textScore, "sort score":o.sortScore, "distance score":o.distanceScore, "keywords":o.docKeyWords, "dateline":o.docDateLine}
		if isinstance(o,Vector):
			return [element for element in o]
		return simplejson.JSONEncoder.default(self,o)
