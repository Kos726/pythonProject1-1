from pprint import pprint
from inspect import getmodule


methods = []


def introspection_info(obj):
	return {'type': type(obj).__name__,
			'attributes': obj.__dict__,
			'methods': dir(obj),
			'module': getmodule(obj)}


class ItsClass:
	pass


obj_ = ItsClass()

dict_info = introspection_info(obj_)

pprint(dict_info)
