# The CryptoParty Handbook

Few months ago I decided to update CryptoParty's handbook topics as some of them were outdated. In the meantime I'll try to make pull requests and make changes to CryptoParty's original repo. If you're truly impatient, you can convert the markdown files to pdf and in case you have anything to contribute, go ahead and make a pull request. You can find the repo here: [https://github.com/cryptoparty/handbook](https://github.com/cryptoparty/handbook)
## Prerequisites

For building the handbook artifacts (PDF, LaTeX, EPUB etc...) the following prerequisites are required:
 - GNU make
 - pandoc
 - pdflatex

On Ubuntu all prerequisites can be installed with the following line:

```bash
$ sudo apt-get install build-essential pandoc texlive-full
```

On Arch Linux, try:

```bash
$ sudo pacman -S ghc alex happy cabal-install texlive-core texlive-science texlive-latexextra
$ sudo cabal update
$ sudo cabal install --global pandoc
```

Alternatively you can skip `ghc` and `cabal` and just use `pandoc-bin` from the AUR.

## Build

In order to build the handbook artifacts (PDF, LaTeX, EPUB) execute the following from the src/ folder:

```bash
$ cd src
$ make clean
$ make install
```
    

## License

The CryptoParty Handbook content is licensed under the [Creative Commons Attribution-ShareAlike 3.0 Unported (CC BY-SA 3.0)](https://creativecommons.org/licenses/by-sa/3.0/).

All chapters © the contributors unless otherwise noted.

