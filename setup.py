"""Setup for slack_xblock XBlock."""

import os

from setuptools import setup


def package_data(pkg, roots):
    """Generic function to find package_data.

    All of the files under each of the `roots` will be declared as package
    data for package `pkg`.

    """
    data = []
    for root in roots:
        for dirname, _, files in os.walk(os.path.join(pkg, root)):
            for fname in files:
                data.append(os.path.relpath(os.path.join(dirname, fname), pkg))

    return {pkg: data}


setup(
    name="slack_xblock-xblock",
    version="0.1",
    description="A simple XBlock to add a Slack channel link to Open edX courses.",
    license="UNKNOWN",  # TODO: choose a license: 'AGPL v3' and 'Apache 2.0' are popular.
    packages=[
        "slack_xblock",
    ],
    install_requires=[
        "XBlock",
        "xblock-utils",
        "requests",
        "python-decouple",  # For configuration management
        "django",
    ],
    entry_points={
        "xblock.v1": [
            "slack_xblock = slack_xblock:SlackXBlock",
        ]
    },
    package_data=package_data("slack_xblock", ["static", "public"]),
)
