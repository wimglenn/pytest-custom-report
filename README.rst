|pypi|_ |pyversions|_ |actions|_ |womm|_

.. |pypi| image:: https://img.shields.io/pypi/v/pytest-custom-report.svg
.. _pypi: https://pypi.org/project/pytest-custom-report

.. |pyversions| image:: https://img.shields.io/pypi/pyversions/pytest-custom-report.svg
.. _pyversions:

.. |actions| image:: https://github.com/wimglenn/pytest-custom-report/actions/workflows/ci.yml/badge.svg
.. _actions: https://github.com/wimglenn/pytest-custom-report/actions/workflows/ci.yml/

.. |womm| image:: https://cdn.rawgit.com/nikku/works-on-my-machine/v0.2.0/badge.svg
.. _womm: https://github.com/nikku/works-on-my-machine


.. image:: https://user-images.githubusercontent.com/6615374/44383803-a48a7600-a4df-11e8-9ce5-dfd5eca9d208.png


pytest-custom-report
====================

A plugin for defining your own characters to be used when displaying test outcomes in `pytest <https://docs.pytest.org/en/latest/>`_ (passed, failed, skipped etc).

For example, if you wanted to see a `PILE OF POO (U+1F4A9) <https://www.fileformat.info/info/unicode/char/1f4a9/index.htm>`_ glyph displayed in the terminal report for each failing test:

.. code-block:: bash

   pytest --report-failed=💩

To persist your custom characters, add a section like this in the `configuration file <https://docs.pytest.org/en/latest/customize.html>`_ (i.e. in ``pytest.ini``, ``tox.ini``, ``setup.cfg`` or whatever):

.. code-block::

   [pytest]
   report_failed = 💩
   report_failed_verbose = OH CRAP


Installation and Usage
----------------------

.. code-block:: bash

   pip install pytest-custom-report

This will add new command-line arguments and configuration file options to ``pytest`` (detailed in the following section). Command line arguments take precedence over configuration file settings. The plugin is always enabled, but unless you've configured your own symbols the ``pytest`` defaults are used.

To execute tests with the plugin disabled temporarily, use this:

.. code-block:: bash

   pytest -p no:pytest-custom-report

If you're trying to use emojis but you can't see the glyphs properly in your terminal, you may be missing unicode fonts with the upper plane - you could install for example `GNU Unifont <http://unifoundry.com/unifont/index.html>`_.


Configuration
-------------

The table below shows the available options as well as ``pytest``'s default style for each outcome.

==============  ============================  ======================  =======================
test outcome    command-line argument name    .ini file config key    default report symbol
==============  ============================  ======================  =======================
``passed``      ``--report-passed``           ``report_passed``       ``.``
``xpassed``     ``--report-xpassed``          ``report_xpassed``      ``X``
``failed``      ``--report-failed``           ``report_failed``       ``F``
``xfailed``     ``--report-xfailed``          ``report_xfailed``      ``x``
``skipped``     ``--report-skipped``          ``report_skipped``      ``s``
``error``       ``--report-error``            ``report_error``        ``E``
==============  ============================  ======================  =======================

When tests are executed with ``-v`` or ``--verbose`` flag enabled, you'll see longer strings displayed and one-line per test outcome. These can be specified too.

==============  ============================  ==========================  =======================
test outcome    command-line argument name    .ini file config key        default report string
==============  ============================  ==========================  =======================
``passed``      ``--report-passed-verbose``   ``report_passed_verbose``   ``PASSED``
``xpassed``     ``--report-xpassed-verbose``  ``report_xpassed_verbose``  ``XPASS``
``failed``      ``--report-failed-verbose``   ``report_failed_verbose``   ``FAILED``
``xfailed``     ``--report-xfailed-verbose``  ``report_xfailed_verbose``  ``XFAIL``
``skipped``     ``--report-skipped-verbose``  ``report_skipped_verbose``  ``SKIPPED``
``error``       ``--report-error-verbose``    ``report_error_verbose``    ``ERROR``
==============  ============================  ==========================  =======================


Example config file
-------------------

Here is some example ``pytest.ini`` content that you can copy-paste and modify to your liking:

.. code::

   [pytest]

   report_passed = ✔
   report_xpassed = 🦄
   report_failed = ✗
   report_xfailed = 👎
   report_skipped = ?
   report_error = 🔥

   report_passed_verbose = OH YEAH
   report_xpassed_verbose = WHAT IN TARNATION?
   report_failed_verbose = OH CRAP
   report_xfailed_verbose = YEAH WHATEVER
   report_skipped_verbose = DON'T CARE
   report_error_verbose = YOU MEDDLING KIDS!


.. image:: https://user-images.githubusercontent.com/6615374/44383928-02b75900-a4e0-11e8-9d81-84c0d2b14155.png