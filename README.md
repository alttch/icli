# icli - interactive command line interfaces

## What is icli

**icli** is a Python library, built on top of **argparse**, which allows you to
quickly build rich interactive command line interfaces with sections, command
history, command batch processing, command repeating and interactive
auto-complete.

<img src="https://github.com/alttch/icli/blob/master/demo.gif?raw=true" width="800" />

**icli** uses **readline** library for command inputs.

## Features

* Jump between command sections (use / for root section, .. or Ctrl-d to jump
  to upper section)

* Send multiple commands, separated with *;*

* Repeat command execution, by adding *|X* to the end of input (X - delay in
  seconds between commands, use *|cX* to clear screen before next command
  execution)

* Auto-completion (via **argcomplete**)

## How to install

```
pip3 install icli
```

## How to use

* use **icli.ArgumentParser** just like **argparse.ArgumentParser** (create
  parsers, sub-parsers etc.)

* create dispatcher method for commands. This method receives parsed arguments
  in \*\*kwargs:

```python

def dispatcher(**kwargs):
    # ....
```

* define CLI sections tree and start interactive mode:

```python
import icli
ap = icli.ArgumentParser()

# ...

ap.sections = {'user': ['account', 'apikey'], 'document': []}
ap.run = dispatcher
ap.interactive()
```

## Customizing

Override:

* **get_interactive_prompt** customize input prompt
* **print_repeat_title** customize title for repeating commands
* **handle_interactive_exception** handle exceptions, raised during interactive
  loop

## Global commands

You may define global commands, which work in all sections, e.g. let's make *w*
system command executed, when user type *w*:

```python
def w(*args):
    # the method receives command name and optional command arguments in *args
    import os
    os.system('w')

ap.interactive_global_commands['w'] = w
```

Note: global commands are not auto-completed

## History file

If history file is defined, input commands are loaded before interactive
session is started and saved at the end.

```python
ap.interactive_history_file = '~/.test-icli'
```

By default, last 100 commands are saved. To change this behavior, modify:

```python
ap.interactive_history_length = 500
```

## Combining shell and interactive CLI

Let's launch interactive mode when your program is started without arguments,
otherwise process them:

```python
import sys

# prog param sets program name in help to empty for interactive mode
ap = icli.ArgumentParser(prog='' if len(sys.argv) < 2 else None)

# ...

if len(sys.argv) > 1:
    ap.launch()
else:
    ap.interactive()
```

## Batch processing

Your program may read commands from stdin or external file, then process them
without user input

To do this, put commands to I/O steam and launch **batch** method:

```python
import io

f = io.StringIO()
f.write('user account list ; user apikey list\ndocument list')
f.seek(0)
ap.batch(f)
```

or just launch **batch** method with a source stream:

```python
with open('commands.list') as cf:
    ap.batch(cf)
```
