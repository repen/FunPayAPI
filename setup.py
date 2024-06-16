from setuptools import setup, find_packages


with open("README.md", "r", encoding="utf-8") as f:
    long_desc = f.read()


setup(name='FunPayAPI',
      version="1.1.1",
      description='Прослойка между FunPayAPI и клиентом.',
      long_description=long_desc,
      long_description_content_type="text/markdown",
      author='Andrey',
      author_email='9keepa@gmail.com',
      url='https://github.com/repen/FunPayAPI',
      packages=find_packages("."),
      license='GPL3',
      keywords='funpay bot api tools',
      install_requires=['requests==2.28.1', 'beautifulsoup4', 'requests_toolbelt==0.10.1'],
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Programming Language :: Python :: 3',
          'Environment :: Console',
          'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
      ]
)
