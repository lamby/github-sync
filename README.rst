===========
github-sync
===========

Tool for mirroring non-Github repos on Github. WIP.


Instructions
------------

First, setup ``github-sync.cfg``:

Then add to to ``.git/hooks/post-receive``:

::

    curl -qs -X POST http://github-sync.example.com:2727/Organisation/repository || true
