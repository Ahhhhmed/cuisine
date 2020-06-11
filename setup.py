import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cuisine", # Replace with your own username
    version="0.0.1",
    author="Nenad",
    author_email="Ahhhhmed@gmail.com",
    description="A bunch of recepies.",
    long_description=long_description,
    long_description_content_type="markdown",
    url="https://github.com/ahhhhmed/cuisine",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'cuisine = cuisine.__main__:main'
        ]
    },
)