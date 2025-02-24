from pathlib import Path

from setuptools import find_packages, setup

CURRENT_DIR = Path(__file__).parent

DESCRIPTION = "A simple toolkit for Competitive Programming."
README = (CURRENT_DIR / "README.md").read_text(encoding="utf-8")
VERSION = "0.2.0"

setup(
    name="cptool",
    version=VERSION,
    description=DESCRIPTION,
    long_description=README,
    long_description_content_type="text/markdown",
    author="Tho Nguyen",
    url="https://sr.ht/~naiwaaa/competitive-programming-toolkit",
    python_requires=">=3.6.0",
    packages=find_packages(where="."),
    package_dir={"": "."},
    include_package_data=True,
    install_requires=["beautifulsoup4>=4.9.0", "ruamel.yaml>=0.16.10"],
    entry_points={"console_scripts": ["cptool = cptool:run_main"]},
    zip_safe=False,
)
