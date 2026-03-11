from setuptools import setup, find_packages
import os

# Dynamically calculate the version based on moderation.VERSION.
version = __import__('moderation').__version__

extras_require = {
    "test": [
        "django>=4.2",
        "django-webtest",
        "webtest",
        "pillow",
    ]
}

install_requires = ["django<6"]

setup(
    name='django-moderation',
    version=version,
    description='Generic Django objects moderation application',
    long_description=open('README.rst').read()
    + '\n'
    + open(os.path.join('docs', 'history.rst')).read(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: 3 :: Only",
        "Framework :: Django",
        "Framework :: Django :: 4.2",
        "Framework :: Django :: 5.0",
        "Framework :: Django :: 5.1",
        "Framework :: Django :: 5.2",
    ],
    keywords='django moderation models',
    author='Dominik Szopa',
    author_email='dszopa@gmail.com',
    url='https://github.com/dominno/django-moderation',
    license='BSD',
    packages=find_packages('.', exclude=('tests', 'example_project')),
    include_package_data=True,
    extras_require=extras_require,
    install_requires=install_requires,
    zip_safe=False,
)
