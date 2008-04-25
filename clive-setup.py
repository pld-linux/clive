#!/usr/bin/env python
# -*- coding: ascii -*-

###########################################################################
# clive, video extraction utility
# Copyright (C) 2007-2008 Toni Gundogdu
#
# clive is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 0.1.2-1307 USA
###########################################################################

import sys
import re
import os
import gzip

from distutils.core import setup

import clive as _clive

if sys.platform == 'win32':
	try:
		import py2exe
		_py2exe_avail = 1
	except ImportError:
		_py2exe_avail = 0

desc = 'Video extraction tool'

ldesc = 'Video extraction tool for Youtube, Google ' \
	'video and other video websites'

author = _clive.__author__.rsplit(' ', 1)[0]

author_email = re.sub('(^<)|(>)', '',
	_clive.__author__.rsplit(' ',1)[1])

classifiers = [
  'Environment :: Console',
  'Intended Audience :: End Users/Desktop',
  'Operating System :: POSIX',
  'Programming Language :: Python',
  'License :: OSI Approved :: GNU General Public License (GPL)',
  'Natural Language :: English',
  'Topic :: Internet',
  'Topic :: Utilities'
]

manpage = 'man/clive.1'
manpage_gz = manpage + '.gz'
data_files = [ ('share/man/man1', [manpage_gz]) ]

setup_args = dict(
	name = 'clive',
	version = _clive.__version__,
	description = desc,
	long_description = ldesc,
	maintainer = author,
	maintainer_email = author_email,
	url = _clive.__url__,
	license = 'GPL',
	scripts = ['scripts/clive'],
	packages = ['clive'],
	package_dir = {'clive':'clive'},
	data_files = data_files,
	classifiers = classifiers,
	platforms = ['Any']
)

if sys.platform == 'win32' and _py2exe_avail:
	setup_args['console'] = ['scripts/clive']
	setup_args['data_files'] = []

# gzip clive.1; otherwise bdist_rpm will fail
gzip.GzipFile(manpage_gz, 'w').write(open(manpage).read())

setup(**setup_args)

try: # cleanup
	os.remove(manpage_gz)
except:
	pass

