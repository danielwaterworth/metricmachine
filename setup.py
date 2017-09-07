import os
from setuptools import setup

setup(
    name = "metricmachine",
    version = "0.0.1",
    author = "Daniel Waterworth",
    author_email = "daniel@manganizeme.com",
    description = "",
    keywords = "metrics",
    url = "https://github.com/danielwaterworth/metricmachine",
    packages=['metricmachine', 'metricmachine.app'],
    long_description="",
    classifiers=[],
    install_requires=['requests', 'flask', 'Flask-Bootstrap'],
    include_package_data=True,
)
