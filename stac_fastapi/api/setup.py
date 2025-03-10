"""stac_fastapi: api module."""

from setuptools import find_namespace_packages, setup

with open("README.md") as f:
    desc = f.read()

install_requires = [
    "brotli_asgi",
    "stac-fastapi.types",
]

extra_reqs = {
    "dev": [
        "httpx",
        "pytest",
        "pytest-cov",
        "pytest-asyncio",
        "pre-commit",
        "requests",
        "pystac[validation]==1.*",
    ],
    "benchmark": [
        "pytest-benchmark",
    ],
    "docs": ["mkdocs", "mkdocs-material", "pdocs"],
}


setup(
    name="stac-fastapi.api",
    description="An implementation of STAC API based on the FastAPI framework.",
    long_description=desc,
    long_description_content_type="text/markdown",
    python_requires=">=3.8",
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
    ],
    keywords="STAC FastAPI COG",
    author="Arturo Engineering",
    author_email="engineering@arturo.ai",
    url="https://github.com/stac-utils/stac-fastapi",
    license="MIT",
    packages=find_namespace_packages(exclude=["alembic", "tests", "scripts"]),
    zip_safe=False,
    install_requires=install_requires,
    tests_require=extra_reqs["dev"],
    extras_require=extra_reqs,
)
