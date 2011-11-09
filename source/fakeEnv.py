# DIRAC.Core.Base.DB
class DB:
  pass

## DIRAC.Core.Base.Client
class Client:
  pass

## DIRAC.Core.Base.AgentModule
class AgentModule:
  pass

## DIRAC.Core.Base.AgentReactor
class AgentReactor:
  pass

## DIRAC.Core.Base.API
class API:
  pass

## DIRAC.Core.Base.Script
class Script:
  def parseCommandLine(self):
    pass

def parseCommandLine():
  pass


################################################################################
# Fake Resource Status System
################################################################################

#### Utilities

class CS:
  
  @staticmethod
  def getTypedDictRootedAt( name ):
  
    d = {}
    res = [ 'Resources','Status','PolicyResult','Status','SiteType','ServiceType','ResourceType','PolicyTypes' ]
    for r in res:
      d[ r ] = {}
      
    d['PolicyResult'] = []
    d['Status']       = []  
      
    return d

  class CSError:
    pass

def CheckDBExecution(func):
  return func

def ValidateDBTypes(func):
  return func

def HandlerDec3( func ):
  return func

def AdminRequired( func ):
  return func

def ClientFastDec( func ):
  return func

class InvalidRes:
  pass

class RSSException:
  pass

class MySQLMonkey:
  pass

class Synchronizer:
  pass

class ResourceStatusValidator:
  pass

def where():
  pass

################################################################################
################################################################################

## DIRAC.ConfigurationSystem.Client.Config
#def getConfig():
#  pass
#class Fake:
#  def dummy( self, *args, **kwargs ):
#    pass 
#  def __getattr__( self, name ):
#    return self.dummy
#gMonitor = Fake()
#gLogger  = Fake()
#gConfig  = Fake()


#def server_init(a, b):
#	pass
#
#def connect( host, user, passwd, db ):
#	pass
#
#def thread_safe():
#	pass
#
#def server_end():
#	pass
#
#def timezone(a):
#	pass
#
#def array(a, b):
#	pass
#
#def absolute(a):
#	pass
#
#def average(a):
#	pass
#
#def sum(a):
#	pass
#
#def divide(a, b):
#	pass
#
#def date2num(a):
#	pass
#
#AutoDateLocator = AutoDateFormatter = DateFormatter = RRuleLocator = HOURLY = MINUTELY = SECONDLY = YEARLY = MONTHLY = DAILY = RRuleLocator = rrulewrapper = ''
#
#class FigureCanvasAgg:
#	pass
#
#class Figure:
#	pass
#
#class poisson:
#	pass
#
#class date2num:
#  pass
#
#class relativedelta:
#  pass
#
#class ScalarFormatter:
#	def ScalarFormatter(self, a):
#		pass
#
#class RequestDB:
#  pass
#  
#class Graph(object):
#  pass
#
#class barGraph(object):
#  pass
#
#class lineGraph:
#  pass
#
#class pieGraph:
#  pass
#
#class cumulativeGraph:
#  pass
#
#class qualityGraph:
#  pass
#
#class textGraph:
#  pass
#
#class PlotCache:
#  pass
#
#def gPlotCache():
#  pass
#
#class cx_Oracle:
#  pass
#


################################################################################