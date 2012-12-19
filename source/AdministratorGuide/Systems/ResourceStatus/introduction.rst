============
Introduction
============

.. contents:: Table of contents
   :depth: 3

The **Resource Status System**, from now **RSS**, is an autonomous policy system acting 
as a central status information point for grid elements. Due its complexity, it has been 
split into two major sections: 

1. Status Information Point 
2. Monitoring System 

On this section, the *status information point* for grid elements is documented.

Looking backwards, there were two end-points where information regarding Grid
Elements statuses was stored. The first one, the :doc:`../Configuration/index` ( CS ) stored the
*Storage Element* ( SE ) status information mixed with static information like the SE
description among other things. The second one, the :doc:`../WorkloadManagement/index` ( WMS ) 
stored the *Site* status information ( more specifically, on a dedicated table on 
JobDB called *SiteMask* ).

The case of the SEs was particularly inconvenient due to the changing nature of a SE
status stored on a almost dynamic container as it is the CS. In spite of being a working
solution, it was pointing out the bounds of the system. The CS had not been designed for
such purpose. 

With that problem in hand, it was very easy to abstract it and include the site status
information stored on the SiteMask. And that was just the beginning... Nowadays the DIRAC
interware offers a formal description to describe grid elements and their status information 
using two complementary systems: 

* CS, which holds the descriptions and hierarchy relationships ( no need to say they are static )
* RSS, which takes care of the status information. 

You can find the details on the `RFC5`_.

-------   
Element
-------

--------
Topology
--------

-----
State
-----

----------
StatusType
----------

---------
Ownership
---------

----------
Parenthood
----------

Resources() Helper
==================

---------------
Database schema
---------------

------------
Synchronizer
------------

--------------
Accessing data
--------------

Client
======

Server
======

Database
========

-----------
Maintenance
-----------

TokenAgent
==========

DatabaseCleanerAgent
====================

SummarizeLogsAgent
==================




.. External links

.. _RFC5: https://github.com/DIRACGrid/DIRAC/wiki/RFC-%235:-Resources-CS-section-structure
