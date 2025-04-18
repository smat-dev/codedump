from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="codedump",
    version="1.0.0",
    author="sdmat-dev",
    author_email="smat-dev@users.noreply.github.com",
    description="A tool to concatenate and dump code from a directory",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/smat-dev/codedump",
    packages=find_packages(),
    install_requires=[
        "pyperclip",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "codedump=codedump.codedump:main",
        ],
    },
)