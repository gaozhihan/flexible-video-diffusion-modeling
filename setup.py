from setuptools import setup

setup(
    name="fvd",
    py_modules=["fvd"],
    install_requires=["blobfile>=1.0.5", "torch", "tqdm"],
)
