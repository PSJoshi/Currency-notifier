from setuptools import setup, find_packages

setup(name='currency-notifier',
      version='0.1',
      description='Tracks exchange rates of Indian rupees',
      long_description='This program tracks exchange rates of Indian rupees Vis-a-vis with other global currencies',
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
      ],
      keywords='currency exchange-rates',
      url='http://github.com/PSJoshi/currency-notifier',
      author='Joshi Pradyumna',
      author_email='joshi.pradyumna@gmail.com',
      license='MIT',
      packages=find_packages(),
      install_requires=[
          'notify2', 'requests', 'argparse', 'json', 'time'
      ],
      include_package_data=False,
      zip_safe=False)
