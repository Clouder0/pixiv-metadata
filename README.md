<div id="top"></div>

<h3 align="center">Pixiv To Eagle</h3>
  <p align="center">
    A tiny script to fetch Pixiv Metadata to Eagle.
    <br />
    <!-- <a href="https://clouder0.github.io/pixiv-metadata/"><strong>Explore the docs »</strong></a> -->
    <!-- <br /> -->
    <a href="https://github.com/Clouder0/pixiv-metadata/blob/main/README.zh-Hans.md"><strong>中文 »</strong></a>
  </p>
</div>

## 📜 TOC

<details><summary>Table of Contents</summary>

- [🌟 Badges](#🌟-badges)
- [💡 Introduction](#💡-introduction)
- [✨ Features](#✨-features)
- [🎏 Getting Started](#🎏-getting-started)
- [🗺️ Roadmap](#🗺️-roadmap)
- [❓ Faq](#❓-faq)
- [💌 Contributing](#💌-contributing)
- [🙏 Acknowledgment](#🙏-acknowledgment)
- [📖 License](#📖-license)
- [📧 Contact](#📧-contact)

</details>

## 🌟 Badges

[![Test][github-action-test-shield]][github-action-test-url]
[![Codecov][codecov-shield]][codecov-url]
[![pre-commit-ci][pre-commit-ci-shield]][pre-commit-ci-url]
[![pepy-shield]][pepy-url]

[![release-shield]][release-url]
[![pyversions-shield]][pyversions-url]
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![CodeFactor-shield]][CodeFactor-url]
[![code-style-black-shield]][code-style-black-url]

<!-- INTRODUCTION -->

## 💡 Introduction

Iterate through your Eagle library, recognize Pixiv Pictures and fetch metadata from Pixiv.

Using this script requires manual code modification.

Search `Modify Here` in file `pixiv_metadata/__main__.py` and follow the comments to get things done.

![Preview](img/img1.png)

<p align="right">(<a href="#top">back to top</a>)</p>

## ✨ Features

- Async IO, blazing fast. Finished 2500+ images in less than 10 seconds.
- Keep your original tags.
- Extra tags generated from metadata. Highly extendable. (Default add Artist tag and Bookmark tag.)
- Annotation generating, including loads of info.
- Too lazy to add more.

<p align="right">(<a href="#top">back to top</a>)</p>

## 🎏 Getting Started

```bash
git clone https://github.com/Clouder0/pixiv-metadata.git
cd pixiv-metadata
pip install -r requirements.txt
```

Then modify the script. Execute: `python -m pixiv_metadata`.

<p align="right">(<a href="#top">back to top</a>)</p>

## 🗺️ Roadmap

<!-- Please check out our [Github Project](https://github.com/Clouder0/pixiv-metadata/projects/1). -->

<!-- See the [open issues](https://github.com/Clouder0/pixiv-metadata/issues) for a full list of proposed features (and known issues). -->

No roadmap, just use it.

<p align="right">(<a href="#top">back to top</a>)</p>

## ❓ FAQ

No questions yet.

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTRIBUTING -->

## 💌 Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

Don't forget to see our [Contributing Guidelines](https://github.com/Clouder0/pixiv-metadata/blob/main/CONTRIBUTING.md) for details.

<p align="right">(<a href="#top">back to top</a>)</p>

## 🙏 Acknowledgment

There are various open source projects that pixiv-metadata depends on, without which this tool wouldn't exist. Credits to them!

- [aiohttp](https://github.com/aio-libs/aiohttp), Apache License 2.0
- [loguru](https://github.com/Delgan/loguru), MIT License

<p align="right">(<a href="#top">back to top</a>)</p>

## 📖 License

Distributed under the MIT License. See `LICENSE` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>

## 📧 Contact

Clouder0's email: clouder0@outlook.com

Project Link: [https://github.com/Clouder0/pixiv-metadata](https://github.com/Clouder0/python-template)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->

<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/Clouder0/pixiv-metadata.svg?style=for-the-badge
[contributors-url]: https://github.com/Clouder0/pixiv-metadata/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Clouder0/pixiv-metadata.svg?style=for-the-badge
[forks-url]: https://github.com/Clouder0/pixiv-metadata/network/members
[stars-shield]: https://img.shields.io/github/stars/Clouder0/pixiv-metadata.svg?style=for-the-badge
[stars-url]: https://github.com/Clouder0/pixiv-metadata/stargazers
[issues-shield]: https://img.shields.io/github/issues/Clouder0/pixiv-metadata.svg?style=for-the-badge
[issues-url]: https://github.com/Clouder0/pixiv-metadata/issues
[license-shield]: https://img.shields.io/github/license/Clouder0/pixiv-metadata.svg?style=for-the-badge
[license-url]: https://github.com/Clouder0/pixiv-metadata/blob/main/LICENSE
[github-action-test-shield]: https://github.com/Clouder0/pixiv-metadata/actions/workflows/test.yml/badge.svg?branch=main
[github-action-test-url]: https://github.com/Clouder0/pixiv-metadata/actions/workflows/test.yml
[codecov-shield]:https://codecov.io/gh/Clouder0/pixiv-metadata/branch/main/graph/badge.svg?token=D2XT099AFB
[codecov-url]: https://codecov.io/gh/Clouder0/pixiv-metadata
[pre-commit-ci-shield]: https://results.pre-commit.ci/badge/github/Clouder0/pixiv-metadata/main.svg
[pre-commit-ci-url]: https://results.pre-commit.ci/latest/github/Clouder0/pixiv-metadata/main
[code-style-black-shield]: https://img.shields.io/badge/code%20style-black-000000.svg?style=for-the-badge
[code-style-black-url]: https://github.com/psf/black
[pyversions-shield]: https://img.shields.io/pypi/pyversions/pixiv-metadata.svg?style=for-the-badge
[pyversions-url]: https://pypi.org/project/pixiv-metadata/
[release-shield]: https://img.shields.io/github/release/Clouder0/pixiv-metadata.svg?style=for-the-badge
[release-url]: https://github.com/Clouder0/pixiv-metadata/releases
[CodeFactor-shield]: https://www.codefactor.io/repository/github/clouder0/pixiv-metadata/badge/main?style=for-the-badge
[CodeFactor-url]: https://www.codefactor.io/repository/github/clouder0/pixiv-metadata/overview/main
[pepy-shield]: https://static.pepy.tech/personalized-badge/pixiv-metadata?period=total&units=international_system&left_color=grey&right_color=brightgreen&left_text=Downloads
[pepy-url]: https://pepy.tech/project/pixiv-metadata
