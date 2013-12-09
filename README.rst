code2html
====

Convert source code repository to HTML.

Brief
-----

Do you like reading source code on your mobile devices?

HTML is a light-weight format (unlike PDF or EPUB) that can be easily readed on
every browser-included mobile device.

``code2html`` is a tool converts source code repository to HTML format files so
that you can put them into your mobile devices and read it whenever and
wherever with a beautiful syntax highlight (thanks ``Vim``).

Get rid of those social networking applications, start to **enjoy code reading**.

Requirements
------------

By taking advantages of the magic ``TOhtml`` function from ``Vim``,
``code2html`` requires you have ``Vim`` installed, also if you specify
a non-default color scheme to use, it must be available on your system as well.

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
