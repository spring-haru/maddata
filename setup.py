from setuptools import setup, find_packages

setup(name='maddata',
      packages=find_packages(),
      package_dir={'maddata': './maddata'},
      version='0.1.0',
      description='Python package for downloading the Maddison dataset.',
      author='Tetsu HARUYAMA',
      author_email='haruyama@econ.kobe-u.ac.jp',
      url='https://github.com/spring-haru/maddata',
      license='LICENSE.rst',
      install_requires=['pandas'],
      classifiers=['Intended Audience :: Education',
                   'Intended Audience :: Science/Research',
                   'License :: OSI Approved :: MIT License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   ]
      )
