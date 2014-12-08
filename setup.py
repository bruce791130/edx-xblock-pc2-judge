

import os
from setuptools import setup, find_packages


def package_data(pkg, root_list):
    
    data = []
    for root in root_list:
        for dirname, _, files in os.walk(os.path.join(pkg, root)):
            for fname in files:
                data.append(os.path.relpath(os.path.join(dirname, fname), pkg))

    return {pkg: data}

setup(
    name='xblock-edx-pc2-judge',
    version='0.3.1',
    description='edx-sga Staff Graded Assignment XBlock',
    license='Affero GNU General Public License v3 (GPLv3)',
    url="https://github.com/mitodl/edx-sga",
    author="MITx",
    zip_safe=False,
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'XBlock',
    ],
    entry_points={
        'xblock.v1': [
            'edxpc2judge = edxpc2judge:EdxPc2JudgeBlock',
        ]
    },
    package_data=package_data("edxpc2judge", ["static"]),
)
