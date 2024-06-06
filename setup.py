from setuptools import find_packages,setup

setup(
    name="mcqgenerator",
    version='0.0.1',
    authors='anselm',
    author_email='slemiu@live.com',
    install_requires=['openai', 'langchain', 'streamlit', 'python-dotenv', 'PyPDF2'],
    packages=find_packages()
)