import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Flask2Neo4J",
    version="0.1a1",
    author="Ganggas95",
    author_email="subhannizar25@amail.com",
    description="""Extension Flask for integration with neo4j graph database""",
    long_description=long_description,
    license="MIT",
    long_description_content_type="text/markdown",
    url="https://github.com/ganggas95/flask2neo4j",
    packages=setuptools.find_packages(),
    py_module=["flask2neo4j"],
    include_package_data=True,
    install_requires=[
        'Flask >= 1.0',
        'py2neo >= 3.0',
        "prompt_toolkit<2.1,>=2.0.7"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Database"
    ],
)