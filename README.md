# `OpenPDFManager` 📄

> A free and open-source cross-platform PDF Management Software.

The goal of this project is to provide an all-in-one PDF toolkit that allows users to extract, rotate, and delete pages instantly, as well as combine PDFs, all in just a few clicks. 

Additionally, we aim to create a nice graphical user interface to make the tool accessible to a larger audience.

<p align="left">
    <img src="https://img.shields.io/badge/version-0.1.0-blue.svg" title="version" alt="version">
    <a href="https://github.com/dnarchery/dnarchery/blob/master/LICENSE"><img alt="github license" src="https://img.shields.io/github/license/dnarchery/dnarchery.svg"></a>
</p>

Built with ❤️ at [**FOSSHack 3.0**](https://fossunited.org/fosshack/2023)!

## Table of Contents

- [Goals](#goals)
- [Features](#features)
- [Installation](#installation)
- [Acknowledgments](#acknowledgements)
- [Contribution](#contribution)
- [License](#license)
- [Project Progress](#faq)

## Goals

- The goal of the project is to create a **PDFManager** which supports all the operations performed a PDF into a nice GUI.
- The **PDFManager** is an oofline toolkit for all your PDF related issues.
- The goal is to also make a cross-platform application.

## Features

The **OpenPDFManager** currently supports the following features:

- Merge two PDFs
- Offline Support

Features to implement/come in future:

- Split PDF
- Trim PDF
- Encrypt PDF
- Decrypt PDF (Brute Force and Other Techniques)
- Rotate Pages of a PDF
- Select and Merge Feature
- Preview before download Feature

<img src="https://github.com/peb-peb/PDFManager/blob/main/assets/MockUp.png" align="center">

The **`OpenPDFManager`** is developed in Python using `flet` (a relatively new GUI library for python). This would serve as a personal project and a guide for any new flet learners. 

### Installation

**Prerequisites:**

- `python` must be installed on your system. To install it, refer [this](https://www.python.org/downloads/)
- `git` should also be present. Refer [this](https://git-scm.com/downloads)
- That's all you need!!! 😉

Now, go into your terminal and run the following commands step-by-step:

1. Clone the Reposistory

```
git clone git@github.com:peb-peb/PDFManager.git
```

2. Install all the external libraries using

```
pip install -r requirements.txt
```

3. Run the **`OpenPDFManager`**

```
flet src\pdfmanager\pdfmanager.py
```

## Contribution

Contributions are always welcomed 🤗.
Refer <a href="https://github.com/peb-peb/PDFManager/blob/main/CONTRIBUTING.md">CONTRIBUTING</a> for more info.

## License

Licensed under the MIT License, see <a href="https://github.com/peb-peb/PDFManager/blob/main/LICENSE">LICENSE</a> for more information.

## Acknowledgements

Resources refered during FOSS Hack 3.0 - 

- [flet docs](https://flet.dev/docs/)
- [PyPDF2](https://pypdf2.readthedocs.io/en/3.0.0/)

## FAQ

**_FOSSHack Questionnaire:_**

Q. What was the idea for the project?

> I frequently required to perform many operations on PDF due to my College Assignments.

Q. What stage is it in now?

> The Application was built in 2 days in FOSS Hack 3.0. So, it currently supports only the `merge` feature, but, soon I'll be adding other features to it.

---
