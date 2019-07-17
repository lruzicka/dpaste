import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Dpaste",
    version="1.0.0",
    author="Lukáš Růžička",
    author_email="lruzicka@redhat.com",
    description="A copypaster for console",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lruzicka/dpaste",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: General Public License 3",
        "Operating System :: OS Independent",
    ],
    entry_points={'console_scripts': ['dpaste = dpaste:main']}
)
