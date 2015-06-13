from setuptools import setup, find_packages

setup(
    name = "django-responsive-dashboard",
    version = "1.3.2",
    author = "David Burke",
    author_email = "david@burkesoftware.com",
    description = ("A generic and easy dashboard for Django applications."),
    license = "BSD",
    keywords = "django dashboard responsive",
    url = "https://github.com/burke-software/django-responsive-dashboard",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        'Environment :: Web Environment',
        'Framework :: Django',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        "License :: OSI Approved :: BSD License",
    ],
    install_requires=['django', 'django-positions',]
)
