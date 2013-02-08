#!/usr/bin/env python
''' buildCodeDOC
  
  It accepts as argument the DIRAC version ( or branch name )

'''

import DIRAC

import os
import sys
import tempfile
import urllib
import zipfile

# Get the code directly from GitHub
DIRAC_URL = "https://github.com/DIRACGrid/DIRAC/archive/"

def getTmpDir():
  ''' Creates a temporary dir and adds it to sys.path so that we can import
      whatever lies there.
  '''

  try:
    tmpDir = tempfile.mkdtemp()
  except IOError:
    sys.exit( 'IOError creating tmp dir' )
      
  sys.path.append( tmpDir )

  return tmpDir

def getDIRAC( tmpDir, version = 'integration' ):
  ''' Given a version of DIRAC, downloads it on tmpDir and unzips it. Last
      step is to rename the extracted file from DIRAC-<version> to DIRAC.
  '''
 
  gitHubUrl = '%s%s.zip' % ( DIRAC_URL, version )
  diracZipPath = os.path.join( tmpDir, 'DIRACzip' )
  
  print 'downloading from %s to %s' % ( gitHubUrl, diracZipPath )
  urllib.urlretrieve( gitHubUrl, diracZipPath )

  print 'extracting files'
  zip = zipfile.ZipFile( diracZipPath )
  zip.extractall( tmpDir )

  print 'renaming DIRAC directory'
  diracPath = os.path.join( tmpDir, 'DIRAC' )
  os.rename( '%s-%s' % ( diracPath, version ), diracPath )

  print 'DIRAC is on %s' % diracPath

#...............................................................................
# Functions generating rst files

def getCodeDocumentationPath():

  whereAmI = os.path.dirname( os.path.abspath( __file__ ) )
  relativePathToWrite = '../source/CodeDocumentation'
  
  codeDocumentationPath = os.path.abspath( os.path.join( whereAmI, 
                                                         relativePathToWrite ) )

  return codeDocumentationPath  

def getDIRACPackages():
  
  pkgpath = os.path.dirname( DIRAC.__file__ )
  packages = [ name for _, name, _ in pkgutil.iter_modules([pkgpath]) ]
  
  packages.sort()
  
  print 'Found %s packages' % ','.join( packages )
  
  return packages

def writeCodeDocumentationIndexRST( codeDocumentationPath, diracPackages ):
  '''
  '''
    
  indexPath = os.path.join( codeDocumentationPath, 'index.rst' )
  
  with open( indexPath, 'a' ) as index:
    
    for diracPackage in diracPackages:
      index.write( '\n\n%s\n' % moduleName )

#...............................................................................
# run

def run( diracVersion, tmpDir = None ):

  if tmpDir is None:
    tmpDir = getTmpDir()
  getDIRAC( tmpDir, diracVersion )

  diracPackages = getDIRACPackages()

  codeDocumentationPath = getCodeDocumentationPath()


#...............................................................................
# main

if __name__ == "__main__":

  if len( arguments ) > 1:
    diracVersion = arguments[ 1 ]
  else:
    diracVersion = 'integration'
  
  run( diracVersion )
  
#...............................................................................  
#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF  