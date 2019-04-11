# DPASTE -- a CLI paste tool

This script can help you paste content from the CLI onto a web service at `dpaste.de`.

## Usage

### Paste one liners

`python3 dpaste.py --content <content> --expire <time> --lexer <content_type>`

### Pase a file content

`python3 dpaste.py --file <file> --expire <time> --lexer <content_type>`

### Using a pipe to send pastes

You can also use a pipe to send text to dpaste, for example

`journalctl -b | dpaste`

When successful, the link to the pasted content will be printed to the console.

## Variables

### Expiration time

This variable sets how long the page will keep your snippet. You can use:

* onetime (This will let you display once.)
* hour (default)
* day
* week

### Content type (lexer)

This variable tells the engine how to highlight the content.

* txt (default)
* bash
* c
* html
* perl
* python
* java
* rst
* tex
* vim

More can be seen [in the Dpaste documentaton](https://docs.elephant.house/dpaste/settings.html#settings).

## Example

When you have a python script `program.py` and you want to paste it for a *week*, with *Python* highlighting, do:

`python3 dpaste.py --file program.py --expire week --lexer python`

You can also use `-f`, `-e`, and `-l` shortcuts to provide arguments.
