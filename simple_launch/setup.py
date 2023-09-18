from setuptools import find_packages, setup

package_name = 'simple_launch'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='hem',
    maintainer_email='rauljihemraj@gmail.com',
    description='This repo will go through different concepts of launch files in ROS 2 (Humble Hawksbill).',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "sensor_data_pub = simple_launch.sensor_publisher:main",
            "robot_listener = simple_launch.robot_listener:main"
        ],
    },
)
