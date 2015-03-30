from wagtail.wagtailsearch.backends.base import BaseSearch, BaseSearchQuery, BaseSearchResults
import watson
from django.db import models

import logging

logger = logging.getLogger(__name__)


class WatsonSearchQuery(BaseSearchQuery):
	def _process_lookup(self, field, lookup, value):
		return models.Q(**{field.get_attname(self.queryset.model) + '__' + lookup: value})

	def _connect_filters(self, filters, connector, negated):

		if connector == 'AND':
			q = models.Q(*filters)
		elif connector == 'OR':
			q = models.Q(filters[0])
			for fil in filters[1:]:
				q |= fil
		else:
			return
		
		if negated:
			q = ~q
		return q


	def get_q(self):
		# Get filters as a q object
		q = self._get_filters_from_queryset()
		model = self.queryset.model

		if self.query_string is not None:
			could_search = False
			
			for m in watson.get_registered_models():
				if issubclass(m, model):
					could_search = True
			
			if could_search:
				
				query_subset = ()
				
				for m in watson.get_registered_models():
					query_subset += (m.objects.filter(q),)
				
				return watson.search(self.query_string, models=query_subset)
				#return watson.search(self.query_string)
		return model.objects.none()


class WatsonSearchResults(BaseSearchResults):
	def get_queryset(self):
		q = self.query.get_q()
		return q.distinct()[self.start:self.stop]
	def _do_search(self):
		return self.get_queryset()
	def _do_count(self):
		return self.get_queryset().count()


class WatsonSearch(BaseSearch):
	def __init__(self, params):
		super(WatsonSearch, self).__init__(params)

	def reset_index(self):
	 	pass
	def add_type(self, model):
		pass # Not needed
	def refresh_index(self):
		pass # Not needed
	def add(self, obj):
		pass # Not needed
	def add_bulk(self, model, obj_list):
		return # Not needed
	def delete(self, obj):
		pass # Not needed
	def _search(self, queryset, query_string, fields=None):
		watson_results = WatsonSearchResults(self, WatsonSearchQuery(queryset, query_string, fields=fields))
		results = []
		for r in watson_results :
			results.append(r.object)
		return results 
