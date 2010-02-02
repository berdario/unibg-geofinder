#!/usr/bin/env jython

import sys
sys.path.append("/home/dario/geosearch.jar")
from geotag import GeoApplication

class GeoSearch:
	def __init__(self):
		self.searcher=GeoApplication("/home/dario/geosearch/config")
	def search(self,keywords,place):
		return self.searcher.search(keywords,place)

import simplejson
from geotag.words import GeoRefDoc

class DocEncoder(simplejson.JSONEncoder):
	def default(self,o):
		if isinstance(o,GeoRefDoc):
			return {"name":o.nomeDoc,"text score":o.textScore,"sort score":o.sortScore,"distance score":o.distanceScore}
		return json.JSONEncoder.default(self,o)
