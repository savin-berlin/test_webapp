from setuptools import setup,find_packages

setup(name='test_webapp',
      version='0.1',
      description='This is an test task from computacenter',
      url='https://github.com/savin-berlin/test_webapp',
      git_url='https://github.com/savin-berlin/test_webapp.git',
      author='Egor Savin',
      author_email='science@savin.berlin',
      license='MIT',
      #packages=find_packages('zas_rep_tools/'),
      packages=['zas_rep_tools_data','zas_rep_tools'],
      install_requires=[ "django","nose","django-tables2", "django-crispy-forms", "django-crequest", "django-session-csrf"],
      include_package_data=True,    # include everything in source control
      zip_safe=False,
      test_suite='nose.collector', # test by installationls
      tests_require=['nose'], #test by installation
      #entry_points={
      #    'console_scripts': [
      #        'zas-rep-tools=zas_rep_tools.cli.main:main',
      #    ],
      #},
      classifiers=[
          'Development Status :: 1 - Planning',
          'License :: OSI Approved :: MIT License',
          "Programming Language :: Python :: 3",

                    ]
)
