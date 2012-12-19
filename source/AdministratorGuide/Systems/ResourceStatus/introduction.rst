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

An *Element* in the RSS world represents a Grid Element as described on the `RFC5`_. It can be any of the following:

* Node
* Resource
* Site

Elements are the information unit used on RSS. Everything is an Element, and all are treated equally, simplifying the design
and reducing the complexity of the system. If all are treated equally, the reader may be wondering why three flavors instead
of just an Element type. The answer for that question is simply to keep them separated. On the RSS they are treated equally,
but in Real they have very different significance. Marking as unusable a Site or a CE on the RSS requires the same single and 
unique operation. However, the consequences of marking as unusable a Site instead of one if its CEs by mistake are not negligible.
So, you can also add "safety" as a secondary reason.   

-----------
ElementType
-----------

The Grid topology is not part of the RSS itself, but is worth mentioning the relations underneath to have a full picture. The Grid 
is composed by a "un"certain number of Sites. Those sites are registered with their respective descriptions on the DIRAC CS as follows:

::

 /Resources/Sites
                /CERN.ch
                ...
                /IN2P3.fr
                        /Domains = EGI, LCG
                        /ContactEmail = someone@somewhere
                        /MoreDetails = blah, blah, blah
                        /Computing
                               /...
                        /Storage
                               /...              
                /PIC.es
                ... 

Each Site can have any number of Resources, grouped into categories. In terms of RSS, those categories are *ElementTypes*. For the
Resources Element, we have the following Element Types:

* ComputingElement
* StorageElement
* ...

And if we take a look to the ComputingElement Resources, we can see the pattern happening again.

-> talk about queues

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
