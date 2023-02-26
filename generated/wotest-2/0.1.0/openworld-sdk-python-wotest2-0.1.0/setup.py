# Copyright 2022 Expedia, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from setuptools import setup

setup(
    name='openworld-sdk-python-wotest2',
    version='0.1.0',
    packages=['openworld.sdk.wotest2', 'openworld.sdk.wotest2.model', 'openworld.sdk.wotest2.client'],
    package_dir={'openworld-sdk-python-wotest2': '.'},
    license='Apache License, Version 2.0',
    author='Expedia Group',
    author_email='oss@expediagroup.com',
    url='https://github.com/ExpediaGroup/openworld-sdk-python',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires='>=3.8',
    install_requires=['dataclasses_json', 'uri', 'requests', 'furl', 'openworld-sdk-python-core'],
    description='Open World wotest2 SDK for Python',
    long_description='Open World wotest2 SDK for Python'
)