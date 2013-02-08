''' fakeEnvironment
   
   this module allows to create the documentation without having to do
   any kind of special installation. The list of mocked modules is:
      
   GSI
   
'''

#...............................................................................
# mocks...
import mock

mockGSI                     = mock.Mock()
mockGSI.__version__         = "1"
mockGSI.version.__version__ = "1"

#...............................................................................
# sys.modules hacked

sys.modules[ 'GSI' ] = mockGSI

#...............................................................................
#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF