from setuptools import find_packages, setup
from pathlib import Path

HERE = Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
	name="python-publish-subscriber",
	# packages=find_packages(include=["yahoo_api"], exclude=("tests",)),
	keywords="pubsub publisher subscriber",
	packages=["pubsub"],
	version="0.0.1",
	description="Python PubSub library",
	long_description=README,
	long_description_content_type="text/markdown",
	url="https://github.com/MihaiBlebea/python-pubsub",
	author="Mihai Blebea",
	author_email="mihaiserban.blebea@gmail.com",
	license="MIT",
	install_requires=[],
	setup_requires=["pytest-runner"],
	tests_require=["pytest==4.4.1"],
	test_suite="tests",
)