from setuptools import setup, find_packages

setup(
    name='python-package-encrypter',
    version='0.3',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='An package include functions square encryptor',
    install_requires=['numpy'],
    url='https://github.com/PJasiczek/python-package-encrypter',
    author='Piotr Jasiczek',
    author_email='225933@student.pwr.edu.pl'
)