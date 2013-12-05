code2html
====

Convert source code repository to HTML.

Brief
-----

Do you like reading source code on your mobile devices?

``code2html`` is a tool converts source code repository to HTML format files so
that you can put them into your mobile devices and read it whenever with
a beautiful syntax highlight (thanks ``Vim``).


Usage
-----
::

    code2html [-h] [--color COLOR] input output
    
    positional arguments:
      input          path to the source code repository
      output         path for saving output files
    
    optional arguments:
      -h, --help     show this help message and exit
      --color COLOR  the color scheme to use for syntax highlighting
