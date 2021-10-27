from setuptools import setup


setup(
    name='cldfbench_chang_et_al2015',
    py_modules=['cldfbench_chang_et_al2015'],
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'cldfbench.dataset': [
            'chang_et_al2015=cldfbench_chang_et_al2015:Dataset',
        ]
    },
    install_requires=[
        'phlorest',
        'tqdm',
    ],
    extras_require={
        'test': [
            'pytest-cldf',
        ],
    },
)
