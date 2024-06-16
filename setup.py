from setuptools import setup, find_packages


with open("README.md", "r", encoding="utf-8") as f:
    long_desc = f.read()


setup(name='FunPayAPI',
      version="1.1.2",
      description='Прослойка между FunPayAPI и клиентом.',
      long_description=long_desc,
      long_description_content_type="text/markdown",
      author='Andrey',
      author_email='9keepa@gmail.com',
      url='https://github.com/repen/FunPayAPI',
      packages=find_packages("."),
      license='GPL3',
      keywords='funpay bot api tools',
      install_requires=[
          'requests',
          'bs4',
          'requests_toolbelt'
      ],
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Programming Language :: Python :: 3',
          'Environment :: Console',
          'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
      ]
)
