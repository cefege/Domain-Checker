import setuptools

with open("readme.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='domainChecker',
    version='0.0.1',
    author='Mihai Mateias',
    author_email='mateiasmihaiandrei@gmail.com',
    description='Package to check if the domain DNS record exist.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=['domainChecker'],
    install_requires=[],

)
