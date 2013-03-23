=========
nose-lazy
=========

nose-lazy is a nose_ plugin that determine which tests need to be run
based on the current GIT diff

It's conceptually similar to nose-quickunit_ but a bit smarter: you don't need to respect
any strict structure to contains your tests. nose-lazy will find them analyzing
the last coverage_ report.

.. _nose: http://somethingaboutorange.com/mrl/projects/nose/
.. _nose-quickunit: https://github.com/dcramer/nose-quickunit
.. _coverage: https://pypi.python.org/pypi/coverage

Django Support
--------------

nose-lazy can run your Django tests via django-nose_. Just install
django-nose, then run your tests like so::

  ./manage.py test --with-lazy --logging-clear-handlers

.. _django-nose: https://github.com/jbalogh/django-nose

Installation
============

::

  pip install nose-lazy

Or, get the bleeding-edge, unreleased version::

  pip install -e git://github.com/mgaitan/nose-lazy.git#egg=nose-lazy

Upgrading
=========

To upgrade from an older version of nose-lazy, assuming you didn't
install it from git::

  pip install --upgrade nose-lazy

Use
===

The simple way::

  nosetests --with-lazy


To `use nose-lazy by default`_, add ``with-lazy=1`` to
``.noserc``.

.. _`use nose-lazy by default`: http://readthedocs.org/docs/nose/en/latest/usage.html#basic-usage

Kudos
=====

Thanks to nose-quickunit_ plugin, which provided
inspiration and starting points. Thanks to `Roberto Alsina <http://ralsina.com.ar>`_
for the idea of use coverage_.
Thanks to Machinalis_ and `Python Argentina`_'s folks for the feedback
and encouragement.

.. _Machinalis: http://machinalis.com
.. _Python Argentina: http://python.org.ar/

Author
======

Martín Gaitán
    Email: gaitan@gmail.com
    Twitter: `@tin_nqn_ <http://twitter.com/tin_nqn_>`_

License
=======

GPL

Version History
===============

0.1
  * Initial release
