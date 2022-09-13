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


Deployment
----------

The website is deployed on each push to master to GH pages. The domain registrar is NameCheap. DNS / CDN / SSL is managed by CloudFlare.
