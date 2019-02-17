import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Flask2Neo4J",
    version="0.0.1",
    author="Ganggas95",
    author_email="subhannizar25@amail.com",
    description="""Extension Flask for integration with neo4j graph database""",
    long_description=long_description,
    include_package_data=True,
    long_description_content_type="text/markdown",
    url="https://github.com/ganggas95/flask2neo4j",
    packages=setuptools.find_packages(),
    install_requires=[
        'Flask>=1.0',
        'py2neo>=3.0',
        'prompt-toolkit>=2.0.7<2.1'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Database"
    ],
)