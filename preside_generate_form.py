import re
import os
from os.path import dirname, basename, splitext
import sublime
import sublime_plugin

def Window():
	return sublime.active_window()

def View():
	return Window().active_view()

class PresideGenerateFormCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		window = Window()
		view   = View()

		file_name = self.view.file_name()
		form_file = generateFormFile( path = file_name )
		window.open_file( form_file )

def generateFormFile( path):
	if not os.path.exists( path ) and not os.path.isfile( path ):
		exit()

	filename   = list(splitext( basename( path ) ) )
	objectname = filename[0]
	directory  = []

	form_path = path
	while basename( form_path ) != 'application':
		directory.insert( 0, basename(form_path) )
		form_path = dirname( form_path )

	form_directory    = directory
	form_directory[0] = 'forms'
	filename[1]       = '.xml'

	file_index = len(form_directory) - 1
	if file_index == 1:
		form_directory.insert( 1, 'preside-objects' )
		form_directory[file_index + 1] = ''.join( filename )
	else:
		form_directory[file_index] = ''.join( filename )

	for index in range( len( form_directory ) ):
		form_path = os.path.join( form_path, form_directory[index] )
		if not os.path.exists( form_path ) and splitext( form_path )[1] == '':
			os.makedirs( form_path )

	file            = open( path, 'r' )
	file_lines      = file.read()
	object_property = re.findall( 'name="(.*?)"', file_lines )

	for index in range( len( object_property ) ):
		object_property[index] = '\t\t\t<field binding="' + objectname + '.' + object_property[index] + '" />'

	object_property.insert( 0, '\t\t<fieldset id="' + objectname + '">' )
	object_property.insert( 0, '\t<tab id="' + objectname + '">' )
	object_property.insert( 0, '<form i18nBaseUri="' + form_directory[1] + '.' + objectname + ':">' )
	object_property.insert( 0, '<?xml version="1.0" encoding="UTF-8"?>' )
	object_property.append( '\t\t</fieldset>' )
	object_property.append( '\t</tab>' )
	object_property.append( '</form>' )

	for line in object_property:
		print(line)

	with open( form_path, 'a' ) as f:
		for item in object_property:
			f.write( "%s\n" % item )
		f.close()

	file.close()

	return form_path
