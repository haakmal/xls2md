<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]


# [Excel to Markdown Converter](https://github.com/haakmal/xls2md)
A quick (and rather specific) `XLS` to `MD` conversion tool for my local pedagogy management system.

I'm improving programming skills as I go so please feel free to fork this repo and contribute, you can also: [Report a Bug](https://github.com/haakmal/xls2md/issues) / [Request Feature](https://github.com/haakmal/xls2md/issues)

<!-- ABOUT THE PROJECT -->
## About this tool

I've made this tool to support my own pedagogy management system that uses a local database made of Markdown files. I wanted a quick way to import student data to track locally. The database keeps me in touch with student trajectories and also helps with understanding where they are coming from, i.e. what courses/skills they have already picked up. I'm hoping to use this for my own post-human pedagogy research but that's another discussion :smile:.

This tool is pretty barebones and is meant to give me a blank canvas for every student based off of their unique ID's. *I should mention that this tool is designed around the **University of New South Wales' (Australia)** system where I work, and if you plan to use it you will need to make adjustments where necessary*. That said, if you are from UNSW and find this useful, I'm glad I could have been of help!

<!-- GETTING STARTED -->
## Getting Started

[![Python][Python]][Python-url]

This tool is made in Python and the code is open for scrutiny. Dependencies are required before you can use it from the CLI but installing a working copy of Python should be enough to run. To get a local copy up and running follow these simple example steps. *I'm working on an executable for later*

### Prerequisites

Make sure you have Python installed in your system, if you're on a Mac you can use Homebrew to install. The [Homebrew webpage](https://brew.sh/) has instructions on how to install `brew`. Some dependencies are required and can be installed with both Homebrew and `pip` once you have Python setup.

```sh
pip install pandas openpyxl
```

`pandas` is needed for handling Excel files and `openpyxl` for working with .xlsx files, make sure both are included when installing.

### Installation

There is no installation needed, you simply can clone the repo to a folder on your system.
   ```sh
   git clone https://github.com/haakmal/xls2md.git
   ```

***PS.** I still haven't gotten around to making an executable. If anyone with more experience in programming is willing to help, or explain how to reduce the file size I am all ears!*

<!-- USAGE EXAMPLES -->
## Usage

**Please be advised that this tool is very specific for my needs and I would recommend if you are using this to tweak to your requirements**.

### Setup

1. I have a template MD file for all my students, this is where I collect information I need and add to for instance their weekly reports, discussions with them, etc
2. I have a spreadsheet of students with required information (name, class, email, etc) that is fetched from our LMS. The script extracts the heading of each column as YAML data for the MD files and each row being a student comes a separate file. The filename for my database requirements is set as the first column which in this case is an ID number.
3. I have a list of tutors that are assigned to a student, I keep them also as MD files for my database and the script fetches the file names from a folder I pick so I can assign the tutor to the students record.

The *data.xlsx* is an example of how the spreadsheet should be prepared. In the *template* file there are sections for where data is added from the script. For my purposes I have it set in two places, you may need to tweak this to your requirements: `{{YAML_DATA}}` and `{{TITLE_DATA}}`.

### How to use

Once I have everything collected i.e. spreadsheet, template, list of tutors in a folder, the GUI then becomes self explanatory. Follow instructions and select appropriate options and click the convert button. Each row from the spreadsheet will be extracted as individual MD files ready for my database!

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star if you found this helpful! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<!-- CONTACT -->
## Contact

Dr Haider Ali Akmal - [Links](https://links.hakmal.com/)

**Project Link:** [https://github.com/haakmal/xls2md](https://github.com/haakmal/xls2md)

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/haakmal/xls2md.svg?style=for-the-badge
[contributors-url]: https://github.com/haakmal/xls2md/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/haakmal/xls2md.svg?style=for-the-badge
[forks-url]: https://github.com/haakmal/xls2md/network/members
[stars-shield]: https://img.shields.io/github/stars/haakmal/xls2md.svg?style=for-the-badge
[stars-url]: https://github.com/haakmal/xls2md/stargazers
[issues-shield]: https://img.shields.io/github/issues/haakmal/xls2md.svg?style=for-the-badge
[issues-url]: https://github.com/haakmal/xls2md/issues
[license-shield]: https://img.shields.io/github/license/haakmal/xls2md.svg?style=for-the-badge
[license-url]: https://github.com/haakmal/xls2md/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/haakmal/
[Python]: https://img.shields.io/pypi/pyversions/pandas?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://python.org/