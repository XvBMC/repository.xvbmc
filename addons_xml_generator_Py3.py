""" addons.xml generator """

import os
import re

#import md5
import hashlib

class Generator:
    """
        Generates a new addons.xml file from each addons addon.xml file
        and a new addons.xml.md5 hash file. Must be run from the root of
        the checked-out repo. Only handles single depth folder structure.
    """
    def __init__( self ):
    ####Comment out this line if you have .pyc or .pyo files you need to keep
        self._remove_binaries()
        # generate files
        self._generate_addons_file()
        self._generate_md5_file()
        # notify user
        print("Finished updating addons xml and md5 files")

# Remove any instances of pyc or pyo files
    def _remove_binaries(self):
        for parent, dirnames, filenames in os.walk('.'):
            for fn in filenames:
                if fn.lower().endswith('pyo') or fn.lower().endswith('pyc'):
                    compiled = os.path.join(parent, fn)
                    py_file = compiled.replace('.pyo', '.py').replace('.pyc', '.py')
                    if os.path.exists(py_file):
                        try:
                            os.remove(compiled)
                            print("Removed compiled python file:")
                            print(compiled)
                            print('-----------------------------')
                        except:
                            print("Failed to remove compiled python file:")
                            print(compiled)
                            print('-----------------------------')
                    else:
                        print("Compiled python file found but no matching .py file exists:")
                        print(compiled)
                        print('-----------------------------')

    def _generate_addons_file( self ):
        # addon list
        addons = os.listdir( "." )
        # final addons text
        addons_xml = u"<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>\n<addons>\n"
    ####addons_xml = u"<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<addons>\n" ####ALTERNATIEF???
        # loop thru and add each addons addon.xml file
        for addon in addons:
            try:
                # skip any file or .svn folder
                if ( not os.path.isdir( addon ) or addon == ".svn" ): continue
                # create path
                _path = os.path.join( addon, "addon.xml" )
                # split lines for stripping
            ####xml_lines = open( _path, "r" ).read().splitlines()
                xml_lines = open(_path, "r", encoding='utf-8').read().splitlines()
                # new addon
                addon_xml = ""

                # loop thru cleaning each line
                ver_found = False
                for line in xml_lines:
                    # skip encoding format line
                    if ( line.find( "<?xml" ) >= 0 ): continue

                    if 'version="' in line and not ver_found:
                        version = re.compile('version="(.+?)"').findall(line)[0]
                        ver_found = True

                    # add line
                ####addon_xml += unicode( line.rstrip() + "\n", "UTF-8" )
                    addon_xml += line.rstrip() + "\n"
                # we succeeded so add to our final addons.xml text
                addons_xml += addon_xml.rstrip() + "\n\n"
            except Exception as e:
                # missing or poorly formatted addon.xml
            ####print("Excluding %s for %s" % ( _path, e, ))
                print("Excluding {0} for {1}".format(_path, e))

        # clean and add closing tag
        addons_xml = addons_xml.strip() + u"\n</addons>\n"
        # save file
    ####self._save_file( addons_xml.encode( "UTF-8" ), file="xvbmc-addons.xml" )
        self._save_file(addons_xml.encode('utf-8'), file="xvbmc-addons.xml", decode=True)

#   def _generate_md5_file( self ):
#       try:
#           # create a new md5 hash
#           m = md5.new( open( "xvbmc-addons.xml" ).read() ).hexdigest()
#           # save file
#           self._save_file( m, file="xvbmc-addons.xml.md5" )
#       except Exception as e:
#           # oops
#           print("An error occurred creating addons.xml.md5 file!\n%s" % ( e, ))
    def _generate_md5_file(self):
        try:
        ####m = hashlib.md5( open(os.path.join('zips', 'addons.xml'), 'r', encoding='utf-8').read().encode('utf-8') ).hexdigest()
            m = hashlib.md5( open("xvbmc-addons.xml", 'r', encoding='utf-8').read().encode('utf-8') ).hexdigest()
        ####self._save_file(m, file=os.path.join('zips', 'addons.xml.md5'))
            self._save_file(m, file="xvbmc-addons.xml.md5")
        except Exception as e:
            print("An error occurred creating addons.xml.md5 file!\n{0}".format(e))

    def _save_file(self, data, file, decode=False):
#       try:
#           # write data to the file
#           open( file, "w" ).write( data )
#       except Exception as e:
#           # oops
#           print("An error occurred saving %s file!\n%s" % ( file, e, ))
        try:
            if decode:
                open(file, 'w', encoding='utf-8').write(data.decode('utf-8'))
            else:
                open(file, 'w').write(data)
        except Exception as e:
            print("An error occurred saving {0} file!\n{1}".format(file, e))

if ( __name__ == "__main__" ):
    # start
    Generator()