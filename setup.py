from setuptools import setup, find_packages

setup(
    name='allsafe-otp',  # Package name
    version='0.1.0',  # Version number
    packages=find_packages(),  # Automatically find packages
    install_requires=[
        # List any dependencies your package needs here
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Minimum Python version
)
