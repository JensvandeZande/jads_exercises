# Introduction
Dear students,

This guide describes how to install various software you will need during our lecture but more importantly during your (study) career. This guide contains both MacOS and Windows guides.

We tried to be as precise as possible, but ofcourse problems can still occur despite our efforts. Monday morning before the lecture, we will be present to help out if you encountered any problems during installation. We will be present from 0900hr. Please make sure to be on time if you have any installation issues and you want our help to resolve them.


# Primer
## What is an operating system?
An Operating System (OS) is a collection of software that manages computer hardware resources and provides common services for computer programs. The operating system is the most important type of system software in a computer system.

Operating System is a fully integrated set of specialized programs that handle all the operations of the computer. It controls and monitors the execution of all other programs that reside in the computer, which also includes application programs and other system software of the computer. Examples of Operating Systems are Windows, Linux, Mac OS, etc.

## What is a Terminal
A terminal is a text-based user-interface to interact with your computer. Depending on you operating system they are called slightly different and use slightly different commands. On a Mac for example, instead of using the mouse to create a new folder, we can use the terminal and type in a command to create a new folder: 
```
mkdir my_new_folder
```
Here, `mkdir` is the command used to create a new folder, a.k.a. a directory.
Using commands in a terminal, you can do exactly the same things as you would do by clicking and dragging your mouse.

## What is Windows Subsystem for Linux? (Windows users)
Windows Subsystem for Linux (WSL) is a feature of Windows that allows developers to run a Linux environment without the need for a separate virtual machine or dual booting. In layman's terms, it means you have, sort of, two operating systems on your computer: A Microsoft Windows OS and a Linux OS.

In the world of software development and especially data science and data engineering, almost every piece of software is written on and written for a so called UNIX-like operating system. These UNIX-like operating systems include MacOs and Linux. This means that certain software and packages will simply not work on Windows. Or you have to go through many hoops and hurdles to make it work on Windows (trust me, you don't want this). Also, almost every guide online, stackoverflow answers, github discussions, are assuming you work either on Linux or MacOs.

This is why we ask the student who have a windows laptop to install WSL and use WSL for their software development. It is maybe a bit of an upfront investment, but it will pay off really quick!

# MacOS installation guide

## Create Github Account
Please make sure to [create a github account](https://github.com/signup?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F&source=header-home) before moving forward to the next sections.

## Install Homebrew
Open a terminal and follow the steps.
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
Brew will promt you with next steps. Follow these.
### Verify Installation of brew and Xcode.
To verify installation of brew run the following code in the terminal.
```
brew
```
If Homebrew is not installed, you will see:
```
zsh: command not found: brew
```
Verify Xcode command line tools is installed:
```
brew doctor
```
You should see this:
```
Your system is ready to brew.
```

## Install GIT
To install git exucute the following commands in the terminal.
```
brew install git
```
Verify the installation was successful by typing which ```git --version```:
```
git --version
```
Configure your Git username and email using the following commands, replacing Emma's name with your own. These details will be associated with any commits that you create:
```
git config --global user.name "Emma Paris" 
git config --global user.email "eparis@atlassian.com"
```
Git Credential Manager (GCM) is another way to store your credentials securely and connect to GitHub over HTTPS. With GCM, you don't have to manually create and store a personal access token, as GCM manages authentication on your behalf, including 2FA (two-factor authentication).
```
brew install --cask git-credential-manager
```
After installing you can stay up-to-date with new releases by running:
```
brew upgrade --cask git-credential-manager
```


## Install Visual Studio Code
Follow the [installation guide](https://code.visualstudio.com/docs/setup/mac) up to and including the paragraph “Launching from the command line”

Make sure to reload the terminal window for the new $PATH value to take effect:
```
exec "$SHELL"
```

## Install PyEnv
First install some dependencies by copying this in the terminal.
```
brew install openssl readline sqlite3 xz zlib tcl-tk
```
Install PyEnv
```
brew update
brew install pyenv
```
Run the following commands in the terminal.
```
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init -)"' >> ~/.zshrc
```
Restart your shell to for the PATH to take affect.
```
exec "$SHELL"
```
OPTIONAL. To fix brew doctor's warning ""config" scripts exist outside your system or Homebrew directories"

If you're going to build Homebrew formulae from source that link against Python like Tkinter or NumPy (This is only generally the case if you are a developer of such a formula, or if you have an EOL version of MacOS for which prebuilt bottles are no longer provided and you are using such a formula).

To avoid them accidentally linking against a Pyenv-provided Python, add the following line into your interactive shell's configuration:
```
alias brew='env PATH="${PATH//$(pyenv root)\/shims:/}" brew'
```
## Install Poetry
```
curl -sSL https://install.python-poetry.org | python3 -
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc
```
Restart Shell
```
exec "$SHELL"
```
Check installation
```
poetry --version
```
### Configure Poetry
The following command makes sure vitual environments will be made inside the project.
```
poetry config virtualenvs.in-project true
```
Use currently activated Python version to create a new virtual environment.
```
poetry config virtualenvs.prefer-active-python true
```

## Install Python
We will be using pyenv to install python. With pyenv we can use and manage multiple python versions.

Lets install the latest python version and set it as our global python version.
```
pyenv install 3.11
pyenv global 3.11
```

The next step is to install the necessary Visual Studio Code Extensions. To do this:
1. Open a new (Ubuntu) Terminal window.
2. run the command `code .` Do not forget the dot at the end! The dot tells to open VS-Code within the current directory.
3. On the left pain, click on the extensions icon.
4. Search for "python"
5. Select the [microsoft's python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python) and click on install. (the one with 95+ mil downloads)
6. Other usefull extensions:
    1. [Python Indent](https://marketplace.visualstudio.com/items?itemName=KevinRose.vsc-python-indent)
    2. [autoDocstring](https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring)

## Lets create our first project.
1. Open a new (Ubuntu) Terminal window.
2. Navigate to the folder where you would like to create your new python project. Use this [cheatsheet](https://terminalcheatsheet.com/) to see the relevant commands.
3. Create a new python project using poetry: `poetry new hello_world`
4. Navigate to the newly created project: `cd hello_world`
5. Activate the virtual environment: `poetry shell`
6. Open Visual Studio Code inside the new project: `code .`
7. Add pandas as a dependency: `poetry add pandas`
8. In Visual Studio Code, create a new file "my_first_code.py" under the folder "hello_world".
9. Write your first code! Happy coding all!














# Windows installation guide.
## Create Github Account
Please make sure to [create a github account](https://github.com/signup?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F&source=header-home) before moving forward to the next sections.
## Install WSL 2
Please read about WSL 2 [here](https://learn.microsoft.com/en-us/windows/wsl/about).

Follow the [installation guide](https://learn.microsoft.com/en-us/windows/wsl/setup/environment) up to and including the paragraph “Update and upgrade packages”

## Install Windows Terminal
Follow the [installation guide](https://learn.microsoft.com/en-us/windows/terminal/install) up to and including the paragraph “Set your default terminal profile”. Set your default profile to your previously installed “ubuntu” distribution.

## Install GIT
For git properly work between Windows and WSL 2, you need to install GIT on both.
### Install Git on Windows
Go to the [this](https://github.com/git-for-windows/git/releases/tag/v2.42.0.windows.1) website. At the bottom of the page under the paragraph "Assets" download the latest executable. At the moment of writing this guide, the latest version is "Git-2.42.0-64-bit.exe". Make sure to download the 64 bit installation. Once the download is completed, execute the executable. During the installation, you will be asked to select a credential helper, with GCM set as the default.

### Install GIT on Ubuntu(WSL 2)
Follow the [installation guide](https://learn.microsoft.com/en-us/windows/wsl/tutorials/wsl-git) up to and including the paragraph “Git Credential Manager setup”. Under the paragraph “Git Credential Manager setup” make sure to sue the first command, i.e., `git config --global credential.helper "/mnt/c/Program\ Files/Git/mingw64/bin/git-credential-manager.exe"`


## Install Visual Studio Code
Follow the [installation guide](https://learn.microsoft.com/en-us/windows/wsl/tutorials/wsl-vscode) up to and including the paragraph “Update your Linux distribution”. Run the commands specified in paragraph “Update your Linux distribution” in the previously opened terminal.

## Install PyEnv
First install some dependencies by copying this in the Ubuntu terminal.
```
sudo apt update; sudo apt install build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev curl \
libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
```
Install PyEnv
```
curl https://pyenv.run | bash
```
Stock Bash startup files vary widely between distributions in which of them source which, under what circumstances, in what order and what additional configuration they perform. As such, the most reliable way to get Pyenv in all environments is to append Pyenv configuration commands to both .bashrc (for interactive shells) and the profile file that Bash would use (for login shells).

First, add the commands to ~/.bashrc by running the following in your terminal:
```
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc
```
Then, if you have ~/.profile, ~/.bash_profile or ~/.bash_login, add the commands there as well. If you have none of these, add them to ~/.profile.

You can see which files you have by opening a new Ubuntu terminal and running the following commands. It will return a prompt if a **file does not exist**.
```
[[ ! -f ~/.profile ]] && echo "File ~/.profile does not exist!"
[ ! -f ~/.bash_profile ] && echo "File ~/.bash_profile does not exist!"
[ ! -f ~/.bash_login ] && echo "File ~/.bash_login does not exist!"
```

to add to ~/.profile:
```
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.profile
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.profile
echo 'eval "$(pyenv init -)"' >> ~/.profile
```

to add to ~/.bash_profile:
```
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
echo 'eval "$(pyenv init -)"' >> ~/.bash_profile
```


Restart your shell to for the PATH to take affect.
```
exec "$SHELL"
```

## Install Poetry
```
curl -sSL https://install.python-poetry.org | python3 -
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
```
Restart Shell
```
exec "$SHELL"
```
Check installation
```
poetry --version
```

### Configure Poetry
The following command makes sure vitual environments will be made inside the project.
```
poetry config virtualenvs.in-project true
```
Use currently activated Python version to create a new virtual environment.
```
poetry config virtualenvs.prefer-active-python true
```

## Install Python
We will be using pyenv to install python. With pyenv we can use and manage multiple python versions.

Lets install the latest python version and set it as our global python version.
```
pyenv install 3.11
pyenv global 3.11
```

The next step is to install the necessary Visual Studio Code Extensions. To do this:
1. Open a new (Ubuntu) Terminal window.
2. run the command `code .` Do not forget the dot at the end! The dot tells to open VS-Code within the current directory.
3. On the left pain, click on the extensions icon.
4. Search for "python"
5. Select the [microsoft's python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python) and click on install. (the one with 95+ mil downloads)
6. Other usefull extensions:
    1. [Python Indent](https://marketplace.visualstudio.com/items?itemName=KevinRose.vsc-python-indent)
    2. [autoDocstring](https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring)
    3. [Jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter&ssr=false#overview)


## Lets create our first project.
1. Open a new (Ubuntu) Terminal window.
2. Navigate to the folder where you would like to create your new python project. Use this [cheatsheet](https://terminalcheatsheet.com/) to see the relevant commands.
3. Create a new python project using poetry: `poetry new hello_world`
4. Navigate to the newly created project: `cd hello_world`
5. Activate the virtual environment: `poetry shell`
6. Open Visual Studio Code inside the new project: `code .`
7. Add pandas as a dependency: `poetry add pandas`
8. In Visual Studio Code, create a new file "my_first_code.py" under the folder "hello_world".
9. Write your first code! Happy coding all!
