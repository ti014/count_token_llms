from setuptools import setup, find_packages

setup(
    name="count_token_llms",
    version="0.1.0",
    author="timewo",
    author_email="timewo.aise@gmail.com",
    description="count token llms with tkinter application tool",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=["tiktoken"],
    entry_points={
        "console_scripts": [
            "count_token_llms = main:main",
        ],
    },
    python_requires=">=3.10",
)