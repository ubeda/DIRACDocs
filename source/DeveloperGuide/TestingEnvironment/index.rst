==============================
Setting up testing environment
==============================

Every large enough software project needs to be carefully tested, monitored and evaluated to assure that minimum standards of 
quality are being attained by the development process. A primary purpose of that is to detect software and configuration failures so that 
defects may be discovered and corrected before making official release and to check if software meets requirements and works as 
expected. Testing itself could also speed up the development process rapidly tracing problems introduced with 
the new code. 

DIRAC is not different from that scenario, with the exception that service-oriented architecture paradigm, which is one of the basic 
concepts of the project, making the quality assurance and testing process the real challenge. However as DIRAC becomes more and more popular 
and now is being used by several different communities, the main question is not: *to test or not to test?*, but rather: *how to test in a 
efficient way?*

The topic of software testing is very complicated by its own nature, but depending on the testing method employed, the testing process itself
can be implemented at any time in the development phase and idealy should cover many different levels of the system: 

- *unit tests*, in which the resposible person for one source file is proving that his code is written in a right way,
- *integration tests* that should cover whole group of modules combined together to accomplish one well defined task, 
- *regression tests* that seek for errors in existing functinality after patches, functionality enhancements and/or configuration 
  changes have been made to the software,  
- *certification tests* (or *system tests*), which are run against the integrated and compiled system, treating it as a black box and trying 
  to evaluate the system's compliance with its specified requirements. 


In DIRAC project unit tests should be prepared for the developer herself, intergration tests could be developed in groups of code resposible persons,
for regression tests the responsible person should be a complete subsystem (i.e. WMS, DMS, SMS etc.) manager, while certification tests are meant 
to be prepared and prefomed by release managers.  

This document will try to formulate the basic requirements for the lowest level of testing: unit tests, on top of which any complicated 
and fully featured testing framework could be defined. 

    
Conventions
-----------

In DIRAC unit tests should be prepared for the developer herself. As the main implementation language is Python, the developers should 
use its default tool for unit testing, which is already a part of any Python distributions: the unittest_ module. 

This module provides a rich set of tools for constructing and running tests, supporting some very important concepts, like:

- *fixtures*: initialisation needed for setting up a group of tests together with apropriate cleanup after the execution
- *cases*: the smallest unit of testing for one use case scenario
- *suites*: collection of test cases for aggregation of test that should be executed together
- *runners*: classes for executing tests, checking all the spotted asserts and providing output results to the user.

The developers are encouraged to make themselves familiar with unittest module documentation, which could be found here [link].

All test modules should follow those conventions:

**T1**
  Tests defined in one unit test module should cover one class and nothing else.

**T2**
  The unit test name convention should follow the rule: module name extened with **Tests** word, i.e. in case of **BananaClient** module, 
  which implementation is kept **BananaClient.py** disk file, the unit test file should be named **BananaClientTests.py**  

**T3**
  The test modules should be kept as close as possible to the modules they are testing, prefereably in a *test* subdirectory on DIRAC subsystem
  package directory, i.e: all tests modules for WMS should be kept in *DIRAC/WMS/tests* directory.


Metodology
----------

Unit tests are typically created by the developer who will also write the code that is being tested. 
The tests may therefore share the same blind spots with the code: for example, a developer does not realize that certain 
input parameters must be checked, most likely neither the test nor the code will verify these input parameters. 
If the developer misinterprets the requirements specification for the module being developed, both the tests and the code will be wrong. 
Hence if the developer is going to prepare her own unit tests, then the first step in such occasions is to formulate all possible use cases scenarios.
The code (or even betetr software requirements document, if any of such exists, otherwise this is a great opportunity to prepare one) should be 
read carefully to isolate all the paths in execution. For each of such cases the developer should prepare and formulate all required inputs, 
configurations, internal objects states, underlying components etc. 

In this set the developer should concentrate first on one very special scenario, so special that it has got its own name: the main 
success scenario. 

.. _Python: http://www.python.org/
.. _unittest: http://docs.python.org/library/unittest.html
