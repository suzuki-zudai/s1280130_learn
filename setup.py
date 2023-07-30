import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='s1280130_learn',
    version='2023.07.30',
    author='Suzuki Shota',
    author_email='zudaiaka@gmail.com',
    description='This software is being developed at the University of Aizu, Aizu-Wakamatsu, Fukushima, Japan',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(),
    url='https://github.com/suzuki-zudai/s1280130_learn/',
    license='GPLv3',
    install_requires=[            # All necessary packages utilized by our s1280130_learn software
        'pandas',
        'plotly',
        'matplotlib',
        'numpy',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.5',
)
