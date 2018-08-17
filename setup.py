from setuptools import setup

setup(
    name="pytest-custom-report",
    version="1.0.0",
    url="https://github.com/wimglenn/pytest-custom-report",
    description="Configure the symbols displayed for test outcomes",
    long_description=open("README.rst").read(),
    long_description_content_type="text/x-rst; charset=UTF-8",
    author="Wim Glenn",
    author_email="hey@wimglenn.com",
    license="MIT",
    install_requires=["pytest"],
    py_modules=["pytest_custom_report"],
    entry_points={"pytest11": ["pytest-custom-report=pytest_custom_report"]},
    classifiers=[
        "Framework :: Pytest",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
    ],
)
