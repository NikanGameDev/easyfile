from setuptools import setup, find_packages
import pathlib
here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")
setup(
    name="sampleproject",
    version="2.0.0",
    description="A sample Python project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/NikanGameDev/easyfile",
    author="Nikan",
    author_email="author@example.com",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: Apache 2.0 License",
        "Programming Language :: Python :: All versions",
    ],
    keywords="file, eazy, developer",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=1.0, <4.0",
   
)
