from setuptools import find_packages, setup

setup(
    name="taekwondo_glossario",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "streamlit>=1.32.0",
        "python-Levenshtein==0.23.0",
    ],
)
