from setuptools import setup


setup(
    name='time',
    include_package_data=True,
    entry_points={
        'console_scripts':[
            'work_start=work_time:main'
        ]
    },
)
