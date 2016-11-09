from pandaharvester.harvestercore.PluginBase import PluginBase
import PreparatorUtils


# plugin for preparator with RSE + directIO
class RseDirectPreparator(PluginBase):
    # constructor
    def __init__(self, **kwarg):
        PluginBase.__init__(self, **kwarg)

    # check status
    def checkStatus(self, jobSpec):
        return True, ''

    # trigger preparation
    def triggerPreparation(self, jobSpec):
        return True, ''

    # resolve input file paths
    def resolveInputPaths(self, jobSpec):
        # get input files
        inFiles = jobSpec.getInputFileAttributes()
        # set path to each file
        for inLFN, inFile in inFiles.iteritems():
            inFile['path'] = PreparatorUtils.constructFilePath(self.basePath, inFile['dataset'], inFile['scope'], inLFN)
        # set
        jobSpec.setInputFilePaths(inFiles)
        return True, ''