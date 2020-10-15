import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="mazegen",
    version="0.0.1",
    author="Ujjwal Dimri",
    author_email="ujjwaldimri123@gmail.com",
    description="Python utility to generate and solve mazes.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ujjujjuj/mazegen",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={'console_scripts': ['mazegen=mazegen.__main__:main']},
    python_requires='>=3.6',
    install_requires=[],
    project_urls={
        'Documentation': 'https://github.com/ujjujjuj/mazegen/README.md',
        'Source': 'https://github.com/ujjujjuj/mazegen'
    },
)
