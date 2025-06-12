import setuptools

setuptools.setup(
    name="GpioPin",
    version="0.1.0",
    author="Oleksandr Shevchenko",
    author_email="shevchenko.adb@gmail.com",
    description="A pure Python 3 library to work with GPIO state using gpiod",
    long_description=open("README.md", 'r').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/oshevchenko/gpio_state",
    packages=setuptools.find_packages(where="src"),  # Look for packages inside "src"
    package_dir={"": "src"},  # Map packages to "src"
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Embedded Systems',
        'Topic :: System :: Hardware',
        'Topic :: System :: Hardware :: Hardware Drivers'
    ],
    # entry_points = {
    #     'console_scripts': [
    #         'lmk05318c=lmk05318.console:main',
    #     ],
    # },
    python_requires='~=3.7',
    license='MIT',
    keywords='gpio gpiod embedded linux',
)
