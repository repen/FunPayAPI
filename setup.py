from setuptools import setup, find_packages


setup(name='FunPayAPI',
      version="1.0.0",
      description='Прослойка между FunPayAPI и клиентом.',
      author='Woopertail',
      author_email='woopertail@gmail.com',
      url='https://github.com/woopertail/FunPayAPI',
      packages=find_packages(),
      license='GPL2',
      keywords='funpay bot api tools',
      install_requires=['requests', 'beautifulsoup4', 'requests_toolbelt'],
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Programming Language :: Python :: 3',
          'Environment :: Console',
          'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
      ]
)
