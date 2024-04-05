from setuptools import setup, find_packages

setup(
    name='uschemap-py',
    version='0.1',
    packages=find_packages(),
    package_data={'uschemap-py': ['USchemap.ecore', 'USchemap/*']},
    include_package_data=True,
    install_requires=[
        "pyecore>=0.15.0"
    ]
)
