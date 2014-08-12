from distutils.core import setup


setup(
    name='pyenvsettings',
    version='1.0.0',
    author='Hugo Osvaldo Barrera',
    author_email='hugo@barrera.io',
    packages=['envsettings'],
    package_data={'': ['logging.json']},
    url='https://github.com/hobarrera/envsettings',
    license='ISC',
    description="Read settings from environment variables."
)
