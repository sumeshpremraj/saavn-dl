from setuptools import setup

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

with open('README.md') as f:
    long_description = f.read()

setup(name='saavn-dl',
      version='0.1',
      description='CLI tool to download Saavn playlists',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='http://github.com/sumeshpremraj/saavn-dl',
      author='Sumesh P',
      author_email='me@sumeshp.com',
      license='MIT',
      python_requires='>=3',
      scripts=['saavn-dl'],
      install_requires=requirements,
      classifiers=[
            'Development Status :: 3 - Alpha',
            'Operating System :: POSIX',
            'Natural Language :: English',
            'Operating System :: OS Independent',
            'Topic :: Internet',
            'Topic :: Software Development :: Libraries',
            'Topic :: Software Development :: Libraries :: Python Modules',
            'Topic :: Utilities',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python',
            'Programming Language :: Python :: 3',
      ],
)
