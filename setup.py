import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="weighted_sum_ygzhang0103", 
    version="0.0.1",
    author="Yuge Zhang",
    author_email="ygzhang0103@gmail.com",
    description="A method to get lower and upper bounds of weighted sum",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ygzhang0103/weighted_sum.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
