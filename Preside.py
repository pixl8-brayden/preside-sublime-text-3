import re
import os
from os.path import dirname, basename, splitext
import sublime
import sublime_plugin

def Window():
	return sublime.active_window()

def View():
	return Window().active_view()

class PresideGenerateI18nCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		window = Window()
		view   = View()

		file_name = self.view.file_name()
		i18n_file = generateI18NFile( path = file_name )
		window.open_file( i18n_file )


def generateI18NFile( path):
	if not os.path.exists( path ) and not os.path.isfile( path ):
		exit()

	filename   = list(splitext( basename( path ) ) )
	objectname = filename[0]
	directory  = []

	i18n_path = path
	while basename( i18n_path ) != 'application':
		directory.insert( 0, basename(i18n_path) )
		i18n_path = dirname( i18n_path )

	i18n_directory    = directory
	i18n_directory[0] = 'i18n'
	filename[1]       = '.properties'

	file_index = len(i18n_directory) - 1
	if file_index == 1:
		i18n_directory.insert( 1, 'preside-objects' )
		i18n_directory[file_index + 1] = ''.join( filename )
	else:
		i18n_directory[file_index] = ''.join( filename )

	for index in range( len( i18n_directory ) ):
		i18n_path = os.path.join( i18n_path, i18n_directory[index] )

	file            = open( path, 'r' )
	file_lines      = file.read()
	object_property = re.findall( 'name="(.*?)"', file_lines )

	for index in range( len( object_property ) ):
		object_property[index] = 'field.' + object_property[index] + '.title=' + object_property[index][0].upper() + object_property[index].replace( '_', ' ' )[1:]

	if 'page-types' in directory:
		object_property.insert( 0, 'fieldset.' + objectname + '.title=' + objectname[0].upper() + objectname.replace( '_', ' ' )[1:] )
		object_property.insert( 0, 'tab.'      + objectname + '.title=' + objectname[0].upper() + objectname.replace( '_', ' ' )[1:] )
		object_property.insert( 0, '' )
		object_property.insert( 0, 'iconclass=' )
		object_property.insert( 0, 'description=A ' + objectname.replace( '_', ' ' ) + ' object' )
		object_property.insert( 0, 'name='          + objectname[0].upper() + objectname.replace( '_', ' ' )[1:] )
	else:
		object_property.insert( 0, '' )
		object_property.insert( 0, 'description=A '  + objectname.replace( '_', ' ' ) + ' object' )
		object_property.insert( 0, 'title='          + objectname[0].upper() + objectname.replace( '_', ' ' )[1:] + 's' )
		object_property.insert( 0, 'title.singular=' + objectname[0].upper() + objectname.replace( '_', ' ' )[1:] )

	with open( i18n_path, 'a' ) as f:
		for item in object_property:
			f.write( "%s\n" % item )
		f.close()

	file.close()

	return i18n_path
