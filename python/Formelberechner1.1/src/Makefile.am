## Process this file with automake to produce Makefile.in
## Created by Anjuta


uidir = $(pkgdatadir)/ui
ui_DATA = pygtk_foobar.ui


## The main script
bin_SCRIPTS = pygtk_foobar.py

## Directory where .class files will be installed
pygtk_foobardir = $(pythondir)/pygtk_foobar


pygtk_foobar_PYTHON = \
	pygtk_foobar.py


EXTRA_DIST = $(ui_DATA)


# Remove ui directory on uninstall
uninstall-local:

	-rm -r $(uidir)

	-rm -r $(pkgdatadir)
