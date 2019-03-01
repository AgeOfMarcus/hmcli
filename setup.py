import setuptools
import os

hm_ver = "0.10.18"

def read(fname):
	return open(os.path.join(os.path.dirname(__file__), fname)).read()

setuptools.setup(name='hmcli',
	version=hm_ver,
	description='A command-line interface for the hackerman library.',
	long_description=read("README.md"),
	url='https://github.com/AgeOfMarcus/hmcli',
	author='Marcus Weinberger',
	author_email='marcus@marcusweinberger.com',
	license='GPL',
	packages=setuptools.find_packages(),
	keywords=['hackerman','cli'],
	zip_safe=False,
	install_requires=[
		"hackerman>="+hm_ver,
	])
