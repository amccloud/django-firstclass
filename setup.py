from setuptools import setup, find_packages

setup(
    name='django-firstclass',
    version='0.9.1',
    license='MIT',
    author='Andrew McCloud',
    author_email='andrew@amccloud.com',
    url='http://github.com/amccloud/django-firstclass/',
    packages=find_packages(exclude=['tests']),
    install_requires=open('requirements.txt').readlines(),
    zip_safe=False,
    include_package_data=True,
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ],
)
