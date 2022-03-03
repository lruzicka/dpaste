import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dpaste-console",
    version="1.1.3",
    py_modules=['dpaste'],
    author="Lukáš Růžička",
    author_email="lruzicka@redhat.com",
    description="A copypaster for console",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lruzicka/dpaste",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
    install_requires=['requests'],
    entry_points={'console_scripts': ['dpaste = dpaste:main']}
)
