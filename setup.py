from setuptools import setup, find_packages

with open("requirements.txt", "r", encoding="utf-8") as f:
    requires = []
    for line in f:
        req = line.split("#", 1)[0].strip()
        requires.append(req)

setup(
    name="fextract_jsd_to_flanking",
    install_requires=requires,
    entry_points={"lbfextract": [
        "jsd_to_flanking = fextract_jsd_to_flanking.plugin:hook"
    ],
        "lbfextract_cli": [
            "extract_jsd_to_flanking = fextract_jsd_to_flanking.plugin:hook_cli"
        ]
    },
    packages=find_packages('src'),
    package_dir={
        '': 'src',
    },
)

