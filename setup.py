import setuptools
with open('readme.md','r') as file:
	long_description = file.read()
	
setuptools.setup(
	name = 'preprocess_arjun',
	version = '0.0.1',
	author = 'Arjun',
	author_email = 'arjungupta0335@gmail.com',
	description = 'This is preprocessing python package',
	long_description = long_description,
	long_description_content_type = 'text/markdown',
	packages = setuptools.find_packages,
	classifiers = [
	'Programming Language :: Python :: 3',
	'License :: OSI Approved :: MIT License',
	'Operating System :: OS Independent'
	],
	python_requires = '>=3.5'

	)