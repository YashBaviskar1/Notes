# Conda envionment and pip install python, understanding them in deeper terms 



In order to solve the issue of dependencacy hell we have two intrinsic enviornments -> **pip** and **conda** which essentially  requires isolation of python enviornments for various dependecies projects can have 


### Pip : Python Package Manager 

- Standard official package installer for python. It installs python from PyPI (Python Package Index)

- It manages : strictly python packages. It works on the assumption that compilers, system utilities, tools like CUDA and GPU should be present. **this is a critical limitation**

- Pip itself does not manage environement , but it can work inside a environement, this enviornment cna be created by different tool which is called `venv` 

--> Uses requirements.txt

### Conda : Cross Platform Enviornment and Package Manager  

- manages both packages and environement 
- it manages everything, even non python libraries -> MKL, cuda toolkit can be installed and even python itself in its enviornment 
- it gets packages from repositories called "channels" (anaconda's main channel )
- manage enviornement using `conda` command 
- A conda envionement isolates all the Python Interpreator and system level dependicies 



