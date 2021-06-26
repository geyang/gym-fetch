from os import path
from setuptools import setup, find_packages

with open(path.join(path.abspath(path.dirname(__file__)), 'VERSION'), encoding='utf-8') as f:
    version = f.read()

with open(path.join(path.abspath(path.dirname(__file__)), 'README'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='gym-fetch',
      # note: only include the fetch package and children, no tests or experiments
      packages=[p for p in find_packages() if p == "fetch" or "fetch." in p],
      install_requires=[
          "cmx",
          "numpy",
      ],
      description="A goal-conditioned multitask suite for the fetch robot",
      long_description=long_description,
      author='Ge Yang<ge.ike.yang@gmail.com>',
      url='https://github.com/geyang/gym-fetch',
      author_email='ge.ike.yang@gmail.com',
      package_data={'fetch': ['fetch/*.*', 'fetch/**/*.*']},
      version=version)
