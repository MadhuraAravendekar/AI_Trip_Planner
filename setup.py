from setuptools import find_packages, setup
from typing import List

def get_requirements() -> List[str]:
    """
    Read the requirements from the requirements.txt file.
    Returns a list of requirement strings.
    """
    requirement_list: List[str] = []  # Initialize an empty list to hold requirements

    try:
        # Open the requirements.txt file and read its contents
        with open("requirements.txt", "r") as file:
            # process each line to remove newline characters
            for line in file:
                # Strip whitespace and newline characters
                requirement = line.strip()
                # Ignore empty lines and -e .
                if requirement != "-e .":
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found. No dependencies will be installed.")

    return requirement_list
print(get_requirements())
setup(
    name = "AI-TRAVEL-PLANNER",
    version = "0.0.1",
    author = "Madhura Aravendekar",
    author_email = "madhuraaravendekar29@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements()
)