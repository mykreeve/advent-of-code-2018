filename="input/day8input.txt"
file=open(filename,"r")
numbers=file.readlines()[0].strip().split(" ")

def new_object(position, object, parent):
	children_count=numbers[position]
	metadata_count=numbers[position+1]
	# print "position: " + str(position) + " --- item " + str(object) + ", with " + str(children_count) + " children, and " + str(metadata_count) + " metadata items."
	return ({'parent':parent, 'object':object, 'children_count':children_count, 'metadata_count':metadata_count, 'metadata':[]})

def add_child_to_object(parent,child):
	for o in structure:
		if o['object']==parent:
			o['children'].append(child)

def number_of_children(object):
	for o in structure:
		if o['object']==object:
			return int(o['children_count'])

def number_of_metadata(object):
	for o in structure:
		if o['object']==object:
			return int(o['metadata_count'])

def add_metadata_to_object(position,object):
	md=[]
	for o in structure:
		if o['object']==object:
			m=int(o['metadata_count'])
			for i in range(m):
				md.append(numbers[position+i])
			o['metadata']=md

def add_value_no_children(object):
	val=0
	for o in structure:
		if o['object']==object:
			for j in o['metadata']:
				val += int(j)
			o['value']=val
	# print "added value for object " + str(object) + ", value: " + str(val)

def not_all_objects_have_value():
	for o in structure:
		if not 'value' in o:
			return True
	return False

def object_has_value_already(object):
	for o in structure:
		if o['object']==object:
			if 'value' in o:
				return True
	return False

def all_children_have_values(object):
	targ=number_of_children(object)
	val=0
	for o in structure:
		if o['parent']==object:
			if 'value' in o:
				val += 1
	return val==targ

def add_value_with_children(object):
	targ=[]
	max_val=number_of_children(object)
	meta=[]
	for o in structure:
		if o['object']==object:
			meta=o['metadata']
	val=0
	for o in structure:
		if o['parent']==object:
			targ.append(o['value'])
	for a in meta:
		if int(a) <= max_val:
			val += targ[int(a)-1]
	for o in structure:
		if o['object']==object:
			o['value']=val
	# print "added value for object " + str(object) + ", value: " + str(val)

def add_metadata_for_parent(position,object):
	p = parent_of(object)
	add_metadata_to_object(position,p) 

def number_of_parent_metadata(object):
	p = parent_of(object)
	return number_of_metadata(p)

def parent_of(object):
	for o in structure:
                if o['object']==object:
                        return o['parent']

def all_children_present(object):
	n = number_of_children(object)
	ntest = 0
	for o in structure:
		if o['parent']==object:
			ntest += 1
	if ntest < n:
		return False
	return True

def next_available():
	return len(structure)

def current_object_exists(current_object):
	for o in structure:
		if o['object']==current_object:
			return True
	return False

position=0
structure=[]
parent="none"
current_object=0

while position<len(numbers):
	if current_object_exists(current_object):
		if all_children_present(current_object):
			add_metadata_to_object(position,current_object)
			position += number_of_metadata(current_object)
			current_object=parent_of(current_object)
		else:
			parent=current_object
			current_object=next_available()
	else:	
		structure.append(new_object(position,current_object,parent))
		position=position+2
# print structure


solution=0
for i in structure:
	for j in i['metadata']:
		solution += int(j)
print "First part:", solution

while not_all_objects_have_value():
	for obj in range(len(structure)):
		if not object_has_value_already(obj):
			if number_of_children(obj)==0:
				add_value_no_children(obj)
			elif all_children_have_values(obj):
				add_value_with_children(obj)

print "Second part:", structure[0]['value']
