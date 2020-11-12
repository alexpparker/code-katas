from setuptools import setup


dependencies = ["pytest", "pytest-cov"]


setup(
    name="code_katas_pkg",
    description="Code katas for practise",
    package_dir={"": "src"},
    install_requires=dependencies
)
