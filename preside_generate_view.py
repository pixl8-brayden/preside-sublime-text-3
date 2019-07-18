import re
import os
from os.path import dirname, basename, splitext
import sublime
import sublime_plugin

def Window():
	return sublime.active_window()

def View():
	return Window().active_view()

class PresideGenerateViewCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		window = Window()
		view   = View()

		file_name = self.view.file_name()
		view_file = generateViewFile( path = file_name )
		window.open_file( view_file )

def generateViewFile( path):
	if not os.path.exists( path ) and not os.path.isfile( path ):
		exit()

	filename   = list(splitext( basename( path ) ) )
	objectname = filename[0]
	directory  = []

	view_path = path
	while basename( view_path ) != 'application':
		directory.insert( 0, basename(view_path) )
		view_path = dirname( view_path )

	view_directory    = directory
	view_directory[0] = 'views'
	filename[1]       = '.cfm'

	file_index = len(view_directory) - 1
	if file_index == 1:
		exit()
	else:
		view_directory[file_index] = filename[0]

	for index in range( len( view_directory ) ):
		view_path = os.path.join( view_path, view_directory[index] )
		if not os.path.exists( view_path ) and splitext( view_path )[1] == '':
			os.makedirs( view_path )

	view_path = os.path.join( view_path, 'index.cfm' )

	file            = open( path, 'r' )
	file_lines      = file.read()
	object_property = re.findall( 'name="(.*?)"', file_lines )

	for index in range( len( object_property ) ):
		object_property[index] = '<cf_presideparam name="args.' + object_property[index] + '" editable="false" />'

	object_property.insert( 0, '' )
	object_property.insert( 0, '<cf_presideparam name="args.main_content" field="page.main_content" editable="true" />' )
	object_property.insert( 0, '<cf_presideparam name="args.title"        field="page.title"        editable="true" />' )

	object_property.append( '' )
	object_property.append( '<cfoutput>' )
	object_property.append( '\t<h1>#args.title#</h1>' )
	object_property.append( '\t#args.main_content#' )
	object_property.append( '</cfoutput>' )

	with open( view_path, 'a' ) as f:
		for item in object_property:
			f.write( "%s\n" % item )
		f.close()

	file.close()

	return view_path
