from setuptools import setup, find_packages

setup(
    name = 'whitepaper',
    version = '0.1.0',
    description = """example""",
    author = "Nicholas Cain",
    author_email = "nicholasc@alleninstitute.org",
    url = 'https://github.com/AllenInstitute/whitepaper',
    packages = find_packages(),
    include_package_data=True,
    entry_points={
          'console_scripts': [
              'whitepaper = whitepaper.__main__:main'
        ]
    },
    setup_requires=['pytest-runner'],
)
