from setuptools import setup, find_packages

# Read requirements from requirements.txt
try:
    with open("requirements.txt", "r") as f:
        requirements = f.read().splitlines()
except FileNotFoundError:
    requirements = []  # Fallback to empty list if requirements.txt is missing

setup(
    name="hotel-reservations-prediction",  # Simplified, conventional name
    version="0.1",
    author="Faheem Khan",
    author_email="faheemthakur23@gmail.com",
    description="End to end MLOps Project for Hotel Reservations Prediction",
    packages=find_packages(),
    install_requires=requirements  # Corrected typo
)