from setuptools import setup, find_packages

setup(
    name='django-test-utils',
    version='0.11.18',
    packages=find_packages(),
    author='Jon Froiland',
    author_email='jon@crowdkeep.com',
    description='A package to help testing in Django',
    url='https://github.com/phroiland/django-test-utils',
    download_url='git@github.com:phroiland/django-test-utils.git',
    test_suite='test_project.run_tests.run_tests',
    include_package_data=True,
    install_requires=[
        'BeautifulSoup4',
        'twill-3',
    ]
)
