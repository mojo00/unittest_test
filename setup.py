from setuptools import setup, find_packages
import sys
version = 0.1

setup(name='unittest_test',
      version=version,
      description='Hello World for unittest',
      author='J K',
      author_email='',
      url='https://github.com/berkeleyapplied/baa_messages',
      packages=find_packages(exclude='test'),
      license='MIT License',
      test_suite='test',
      install_requires=[
          'thrift',
          'pre-commit',
          'AWSIoTPythonSDK',
          'Enum',
          'pypubsub',
          'lz4tools'
      ],
      tests_require=[
	'thrift',
        'AWSIoTPythonSDK',
        'Enum',
        'pypubsub',
        'mock'
      ],
      platforms=['any'],
      classifiers=['Development Status :: 1 - Alpha',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: MIT License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Programming Language :: Python :: 2.7',
                   'Topic :: Software Development',
                   'Topic :: Software Development :: Libraries',
                   'Topic :: Software Development :: Libraries :: Python Modules']
    )