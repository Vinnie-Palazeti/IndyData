import setuptools

setuptools.setup(
    name="indydata",  
    version="0.0.0",
    author="Vinnie Palazeti",
    author_email="vinnie.palazeti@gmail.com",
    description="Indiana Data Wrangling",
    packages=setuptools.find_packages(),
    install_requires=[
        'pandas',
        'numpy',
    ],
    python_requires='>=3.6',
)
