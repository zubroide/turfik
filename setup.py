import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="turfik",
    version="0.0.2",
    author="Nikolay Matyushenkov, Zubroid",
    author_email="mnvx@yandex.ru",
    description="Turfik is implementation of Turf.js library on Python",
    url="https://github.com/zubroide/turfik",
    license='MIT',
    packages=setuptools.find_packages(),
    install_requires=['shapely'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
