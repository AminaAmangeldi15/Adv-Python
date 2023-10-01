from setuptools import setup, find_packages

setup(
    name='mylogger',
    version='0.1',
    packages=find_packages(),
    author='Amina',
    author_email='aminaamangeldi15@gmail.com',
    description='A custom logging library',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/mylogger',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
