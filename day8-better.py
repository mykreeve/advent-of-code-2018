filename="input/day8input.txt"
file=open(filename,"r")
numbers=file.readlines()[0].strip().split(" ")

def new_object(position, object, parent):
	children_count=numbers[position]
	metadata_count=numbers[position+1]
	print "position: " + str(position) + " --- item " + str(object) + ", with " + str(children_count) + " children, and " + str(metadata_count) + " metadata items."
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
	p = parent_of(object)
	n = number_of_children(p)
	ntest = 0
	for o in structure:
		if o['parent']==p:
			ntest += 1
	if ntest < n:
		return False
	return True

def next_available():
	return len(structure)

position=0
structure=[]
parent="none"
current_object=0

while position<50:
	structure.append(new_object(position,current_object,parent))
	print structure
	if number_of_children(current_object)==0:
		add_metadata_to_object(position+2,current_object)
		position += 2 + number_of_metadata(current_object)
		if all_children_present(current_object):
			add_metadata_for_parent(position, current_object)
			position += number_of_parent_metadata(current_object)
			current_object = next_available()
		else:
			current_object = next_available()
	if number_of_children(current_object)>0:
		position += 2
		parent = current_object
		current_object = next_available()

