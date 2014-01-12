code2html
====
Convert source code repository to HTML files.

Brief
-----
Do you like reading source code on your mobile devices?

HTML is a light-weight format (unlike PDF or EPUB) that can be easily read on
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

    code2html [-h] [--color COLOR] [--include INCLUDES] [--pre] input output

    positional arguments:
      input               Path to the source code repository
      output              Path for saving output files

    optional arguments:
      -h, --help          show this help message and exit
      --color COLOR       Specify the color scheme use for syntaxhighlighting
      --include INCLUDES  Specify file matching patterns, then only the matched
                          files will be convert. Wild card characters are
                          supported. e.g. --include="*.c" --include="?.py"
      --pre               Instead of actually performing the conversion, simply
                          display what *would* have been converted if --pre
                          weren't used

Example 1
~~~~~~~~~
Use ``--pre`` to check what would be converted::

    $ code2html --pre --include="*.cpp" /path/to/input /path/to/output


Example 2
~~~~~~~~~
Convert all Python sources, ``ext.c`` and a README file from ``/path/to/input``
to ``/path/to/output``, using ``jellybeans`` as the syntax highlight scheme::

    $ code2html --color=jellybeans --include="*.py" --include="ext.c"
    --include="README.rst" /path/to/input /path/to/output
