Documentation in Sphinx
=======================

Documentation is a good thing, so I am setting up a documentation for this example project.

The initial thoughts about requirements were:

  - Documentation format should be text files with light-weight markup.
  - Documentation should be version controlled together with the code.
  - It should be possible to link between code and documentation in both directions.
  - It should be possible to include graphics, ideally within the text files.
  - Some functionality to manage requirements would be useful.
  - Documentation is mostly read from within the editor (VS Code)


-------------
Investigation
-------------

Due to prior experience of the author, a directory tree of markdown files appears like an attractive choice. 
Simple graphics can be written inside markdown documents with e.g. `Mermaid <https://mermaid.js.org/>`_.

Links within the documentation are possible, but apparently limited to headings.
Links to source code have not been investigated.

Links from the source code to documentation are not really part of markdown, but of the editor. 
A short search for such functionality within VS Code did not reveal anything obvious.

Requirements management within markdown files does not seem to be available.
Some RM systems (Doorstop, Gaphor) were briefly looked at, but don't seemt to integrate well into VS Code.
`Sphinx Needs <https://www.sphinx-needs.com/>`_ was the closest match.

Sphinx Needs integrates needs management into the `Sphinx <https://www.sphinx-doc.org/>`_ documentation system.
Sphinx is used by Python and other systems (Linux kernel, CMake, according to Wikipedia).
It uses reStructuredText by default and can be configured to use markdown. 

------------------------------
Choice of documentation system
------------------------------

Based on the broad usage within Python-related and other projects and the availability of extensions for VS Code, Sphinx is chosen as the documentation format.

Sphinx natively supports reStructuredText as the underlying text format and markdown via an extension.
Preference is given here to the native reStructuredText format, because fewer problems are expected with future extensions such as Sphinx Needs.
Sphinx Needs will be added later to manage requirements.

.. note::
  Documentation will be stored as reStructuredText files and managed by Sphinx.

----------------
Directory layout
----------------

Sphinx offers two directory layouts:
one where text files are placed at the root of the documents folder, and built files end up in a _build directory, 
while the other layout has a source and a build folder next to each other.
The default seems to be a split setup with separate source and build directories.
However, I prefer to have only a directory for sources, and therefore keep build as a subdirectory.

The following files are relevant for the system:

  - docs/

    - conf.py: Sphinx configuration file
    - index.rst: Root document for documentation tree
    - \*.rst: Other documentation files

  - docrequirements.txt: Python requirements file for Sphinx and extensions

----------
Extensions
----------

Mermaid
.......

.. note:: The Mermaid extension will be installed.

.. note:: The 

The following test diagram from the `Mermaid extension <https://pypi.org/project/sphinxcontrib-mermaid/>`_ should be rendered correctly:

.. mermaid::

   sequenceDiagram
      participant Alice
      participant Bob
      Alice->John: Hello John, how are you?
      loop Healthcheck
          John->John: Fight against hypochondria
      end
      Note right of John: Rational thoughts <br/>prevail...
      John-->Alice: Great!
      John->Bob: How about you?
      Bob-->John: Jolly good!

Sphinx Needs
............

Sphinx Needs implements requirements management in this project.

.. req:: Install and enable the Sphinx Needs extension.
    :id: req.001



Test: The following text should be rendered correctly:

.. req:: My first requirement
   :tags: main_example
   :id: req.bla

   This need is a requirement, and it includes a title, an ID, a tag and this text as a description.

.. req:: VS Code extension
  :id: req.needs.vscode

  Document the installation and usage of the Sphinx Needs extension for VS Code.

