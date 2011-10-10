DIRAC Section
=============

In this section global attributes are configured.


+---------------------+--------------------------------+----------------+---------------------------------+
| Name                | Description                    | Posible values | Example                         |
+---------------------+--------------------------------+----------------+---------------------------------+
| Extensions          | Define which extensions are    | lhcb, eela     | Extensions = lhcb               |
|                     | going to be used in the server |                |                                 |
+---------------------+--------------------------------+----------------+---------------------------------+
| VirtualOrganization | This option define the default | String         | VirtualOrganization = defaultVO |
|                     | virtual organization           |                |                                 |
+---------------------+--------------------------------+----------------+---------------------------------+



Two subsections are part of DIRAC section:

- Configuration: In this subsection DIRAC servers are configured.

- Setups: Instances installed in the server are installed.

.. toctree::
   :maxdepth: 2
   Configuration/index
   Setups/index
   Security/index