from setuptools import setup, find_packages

setup(
    name='uschema-p-py',
    version='0.1',
    packages=find_packages(),
    package_data={'uschema-p-py': ['USchema-p.ecore', 'USchema-p/*']},
    include_package_data=True,
    install_requires=[
        "pyecore>=0.15.0"
    ]
)
