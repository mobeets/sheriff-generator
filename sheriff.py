# -*- coding: UTF-8 -*-
import string
import emoji
import urbandictionary_api as ud
ALL_ALIASES = list(emoji.unicode_codes.UNICODE_EMOJI_ALIAS_ENGLISH.values())

def fill_pattern(a):
	head = ['   :cop:'] # no sheriff emoji yet :(
	torso1 = ['  ', a[0], a[1], a[2]]
	torso2 = [' ', a[3], ' ', a[4], ' ', a[5]]
	crotch = [':point_down:', '  ', a[6], '', a[7], ' ', ':point_down:']
	leg1 = ['  ', a[8], '  ', a[9]]
	leg2 = ['  ', a[10], '  ', a[11]]
	shoes = ['  :boot:  :boot:  ']
	body = [head, torso1, torso2, crotch, leg1, leg2, shoes]
	return '\n'.join([''.join(x) for x in body])

def get_pattern(ems):
	if len(ems) >= 12:
		return fill_pattern(ems)
	elif len(ems) == 1:
		return fill_pattern([ems[0]]*12)
	elif len(ems) == 2:
		return fill_pattern([ems[0]]*6 + [ems[1]]*6)
	elif len(ems) == 3:
		return fill_pattern([ems[0]]*3 + [ems[1], ems[0], ems[1]] + [ems[2]]*6)
	elif len(ems) >= 4:
		return fill_pattern([ems[0]]*3 + [ems[1], ems[0], ems[1]] + [ems[2], ems[3]]*3)

def is_emoji(x):
	# return x.startswith(':') and x.endswith(':')
	return x in ALL_ALIASES

def get_emojis_from_query(args):
	ems = [x for x in args.split(' ') if is_emoji(x)]
	if not ems:
		x = args.split(' ')[0]
		ems = [y for y in ALL_ALIASES if x.lower() in y.lower()]
	return ems

def clean_defn(defn):
	defn  =defn.split('\n')[0].strip()
	ignores = [str(x) for x in range(10)] + [x for x in string.punctuation]
	while any([defn.startswith(x) for x in ignores]):
		defn = defn[1:].strip()
	return defn
	
def get_definition(title):
	# defns = [clean_defn(x.definition) for x in ud.define(title)]
	# ind = random.choice(xrange(len(defns)))
	defn = clean_defn(ud.define(title)[0].definition)
	defn = defn.capitalize().strip()
	if not defn.endswith('.'):
		defn += '.'
	return defn

def main(args):
	ems = get_emojis_from_query(args)
	if not ems:
		return
	pattern = get_pattern(ems)
	title = args
	defn = get_definition(title)
	msg = "Howdy, I'm the sheriff of {}. {}".format(title, defn)
	print(emoji.emojize(pattern, use_aliases=True))
	print(msg)

if __name__ == '__main__':
	import sys
	main(' '.join(sys.argv[1:]))