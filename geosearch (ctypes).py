#!/usr/bin/env python

from ctypes import *

class Documento(Structure):
	pass

Documento._fields_ = ("nome",c_char_p),("id",c_int),("distanceScore",c_double),("sortScore",c_double),("textScore",c_double),("next",POINTER(Documento))
	
class GeoSearch:	
	def __init__(self):
		self.geosearch=cdll.LoadLibrary("/home/dario/libgeosearch.so.1.0.1")
			
		self.geosearch.init()

		self.geosearch.search.argtypes = [c_char_p, c_char_p]
		self.geosearch.search.restype = POINTER(Documento)

	def search(self,keyword,place):
		doc=self.geosearch.search(keyword,place)

		documents=[]

		while doc:
			documents.append(doc.contents)
			doc=doc.contents.next

		return documents
		
import json

class DocEncoder(json.JSONEncoder):
	def default(self,o):
		if isinstance(o,Documento):
			return {"name":o.nome,"id":o.id,"text score":o.textScore,"sort score":o.sortScore,"distance score":o.distanceScore}
		return json.JSONEncoder.default(self,o)
