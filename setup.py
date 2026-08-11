from setuptools import setup, find_packages

setup(
    name="retail_ops_analytics",
    version="1.2.0",
    author="Gowri Likhi",
    author_email="gowrilikhitha30@gmail.com",
    description="An enterprise-grade supply chain & fulfillment metrics calculation engine.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "pandas>=2.0.0",
        "numpy>=1.24.0",
        "streamlit>=1.25.0",
        "plotly>=5.15.0",
    ],
)
