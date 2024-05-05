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

