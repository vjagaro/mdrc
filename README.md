`mdrc` Markdown Reference Converter
===================================

Convert [Markdown][1] [links][2] to [reference-links][2].

## Install

```sh
pip3 install mdrc
```

## Usage

Convert:

```sh
mdrc infile.md outfile.md
```

Convert in-place:

```sh
mdrc -i file.md
```

UNIX pipes:

```sh
cat infile.md | mdrc > out.md
```

## Bugs

- Currently only supports numeric references.

## Development

```sh
git clone https://.../mdrc.git
cd mdrc
poetry install
```

[1]: https://daringfireball.net/projects/markdown/syntax
[2]: https://daringfireball.net/projects/markdown/syntax#link
