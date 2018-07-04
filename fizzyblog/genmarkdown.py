import collections


def ul(l: list):
	return __indented_ul(l, 0) + "\n"


def ol(l: list):
	return __indented_ol(l, 0) + "\n"


def __indented_ul(l, level):
	s = "\n"
	for elem in l:
		if isinstance(elem, collections.Iterable):
			s += __indented_ul(l, level + 1)
		else:
			s += "\n%s%s" % ("  " * level, str(elem))
	return s


def __indented_ol(l, level):
	s = "\n"
	for i, elem in enumerate(l):
		if isinstance(elem, collections.Iterable):
			s += __indented_ol(elem, level + 1)
		else:
			s += "\n%s%d. %s" % ("  " * level, i, str(elem))
	return s


def img(url, alt):
	return "<img src=\"%s\" alt=\"%s\">" % (url, alt)


def link(url, text):
	return "<a href=\"%s\">%s</a>" % (url, text)
