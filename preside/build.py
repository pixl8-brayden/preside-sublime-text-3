import re
import os
from os.path import dirname, basename, splitext, abspath, isdir, join

def generateSnippetFromFile( filepath, category, destinationDir ):
	count = 0;

	with open( filepath ) as content:
		for line in content:
			line = line.strip()
			if re.search( 'public .* function ((?!init).*)\((.*)\)', line ):
				# variables for generate file
				filename      = '';
				insertContent = [
					  '<snippet>'
					, '\t<content><![CDATA['
					, ']]></content>'
					, '\t<scope>embedding.cfml</scope>'
					, '</snippet>'
				];

				# process
				match    = re.match( 'public .* function ((?!init).*)\((.*)\)', line )
				filename = match.group(1).strip() + '.sublime-snippet'
				insertContent.insert( 3, '\t<tabTrigger>' + match.group(1).strip() + '</tabTrigger>' )
				insertContent.insert( 5, '\t<description>' + category + ': ' + match.group(1).strip() + '</description>' )
				insertContent.insert( 2, '){\n\t${99:// TODO code}\n}' )
				insertContent.insert( 2, match.group(1).strip() + '(' )

				variables = match.group(2).split(',')
				count     = len( variables )

				if len( variables ) == 1 and variables[0] == '':
					insertContent.remove( match.group(1).strip() + '(' )
					insertContent.remove( '){\n\t${99:// TODO code}\n}' )
					insertContent.insert( 2, match.group(1).strip() + '()' )
				else:
					if len( variables ) == 1 and variables[0].find('required') == -1:
						insertContent.remove( match.group(1).strip() + '(' )
						insertContent.remove( '){\n\t${99:// TODO code}\n}' )
						insertContent.insert( 2, match.group(1).strip() + '(){ ${99:// TODO code} }' )
					else:
						for variable in reversed( variables ):
							if variable.find('required') != -1:
								variable = variable.replace('required', '').strip()
								data     = variable.split()
								if count != 1:
									insertContent.insert( 3, '\t, ' + data[1] + ' = ${' + str(count) + ':' + data[0] + '}' )
								else:
									insertContent.insert( 3, '\t  ' + data[1] + ' = ${' + str(count) + ':' + data[0] + '}' )
							count -= 1

				destination = join( destinationDir, category )
				if isdir( destination ) == False:
					os.mkdir( destination )

				output = join( destination, filename )
				with open( output, 'w' ) as f:
					for item in insertContent:
						f.write( "%s\n" % item )
					f.close()

		content.close()

path = dirname( abspath(__file__) ) + '/cms/system/services'

if isdir('../PresideCMS/services') != True:
	os.mkdir( '../PresideCMS/services' )

for folders in os.listdir( path ):
	if isdir( join( path, folders ) ):
		for files in os.listdir( join( path, folders ) ):
			file = join( path, join( folders, files ) )
			if isdir( file ) == False:
				generateSnippetFromFile( file, folders, '../PresideCMS/services' )

# test = '/Users/brayden.tan/Library/Application Support/Sublime Text 3/Packages/preside-sublime-text-3/preside/cms/system/services/notifications/NotificationService.cfc'
# test2 = '/Users/brayden.tan/Library/Application Support/Sublime Text 3/Packages/preside-sublime-text-3/PresideCMS/services'
# generateSnippetFromFile( test, 'Notification Service', test2 )

