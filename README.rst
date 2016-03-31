Galilee Bedouin Camplodge / Shevet-ahim static sites
====================================================

Static, pelican_ generated, sites, English and Hebrew versions.

.. code-block:: bash

    # virtualenv is highly recommended
    virtualenv env
    source env/bin/activate
    pip install -r requirements.txt

.. _pelican: http://docs.getpelican.com/

Download required pelican plugins, regenerate, serve, and sync the site to my server with:

.. code-block:: bash

    make get_plugins  # a must!
    make regenerate
    make serve
    make rsync_upload

Moreover, autoenv_ is really fun. Use it!

Deployment
----------

I'm using Codeship_ to deploy. Use the followin setup commands:

.. code-block:: bash

    # Replace default virtualenv with python3
    rm -rf ${HOME}/.virtualenv
    virtualenv -p $(which python3) "${HOME}/.virtualenv"
    pip install -r requirements.txt
    make get_plugins

And custom deployment script:

.. code-block:: bash

    make rsync_upload

.. _autoenv: https://github.com/horosgrisa/autoenv
.. _Codeship: https://codeship.com
