from setuptools import setup, find_packages

setup(
    name="math_quiz",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        'pytest>=7.0.0',
    ],
    entry_points={
        'console_scripts': [
            'math_quiz=math_quiz.math_quiz:math_quiz'
        ],
    },
    author="jimsh shajeendran",
    author_email="jimsh7237@gmail.com",
    description="Math quiz game",
    python_requires='>=3.6',
)
