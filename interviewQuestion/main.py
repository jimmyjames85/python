import urllib2
import sys
from twisted.internet import reactor, defer
from twisted.web.client import getPage

#######################################################################
# My original approach was with urllib2 Twisted has a getPage function
# but I decided to use this for the first query, which returns the
# list of n urls for us to visit
######################################################################
class UrlData:
    """Class to hold data retrieved from a URL or the errors encountered during the retrieval process"""
    
    url=""
    httpCode=0
    data=""
    
    def __init__(self, url):
        self.url = url
        self.httpCode = 0
        
    def retrieveData(self):
        try:
            urlHandler = urllib2.urlopen(self.url)
            self.data = urlHandler.read()
            self.code = urlHandler.getcode()
        except urllib2.URLError as e:
            self.code = e.code
            self.data = "%s" % e
        except:
            self.data = "UNKOWN ERROR"
            self.code = -1
            raise
        return self.data


######################################################################
#request class to hold results
######################################################################        
class request:
    attempts = 0
    code = -1
    data = ""
    successful = False
    url = ""
    
    def __init__(self, url):
        self.url = url

######################################################################
# Helper functions
######################################################################        
def printf(format, *args):
    sys.stdout.write(format % args)

def buildUrlList(n=2, dataType="/txt", baseUrl="http://coreinterview.sendgrid.net"):
    # dataType can be /json, /xml,  /txt or "" (empty string)
    url = UrlData("%s%s/sample?n=%s" % (baseUrl, dataType, n))
    data = url.retrieveData()
    urlList = data.split("\n")
    return urlList

######################################################################
# Callbacks
######################################################################        
def pageRequestCallback(data, dfrdPage, request, requestList, successful):
    request.attempts = request.attempts + 1
    request.successful = successful 
    request.data = data     

    # if(successful):
    #     printf("\t")
    #     #change request.successful if page returns but json is false 
    #     #todo find the return code
    # else:
    #     printf("ERROR\t")        
    #     #todo find the return code        

    printf("\t%s  %s\n", request.successful, request.url)
    if(successful):
        printf("\t%s\n",request.data)

    requestList.append(request)

def finishCallback(ign, requestList):
    #WHAT IS IGN---^--- for?!?!?     type(ign) returns NoneType

    failedCount=0
    successCount=0
    
    printf("=================Complete=======================\n")
    for req in requestList:
        if(req.successful):
            successCount = successCount + 1
        else:
            failedCount = failedCount + 1
            
        printf("%05s %d HTTP(%d) %s\n", req.successful, req.attempts, request.code, req.url) 
        #printf("%s\n\tAttempts: %d\n\tSuccessful: %s\n\t%Http Code: %d\n\tData: % s \n\n",req.url,req.attempts,req.successful,req.code)#,req.datba)


    printf("\n\nSuccessful: %d\nFailed: %d\n Total: %d\n", successCount, failedCount, (successCount + failedCount))
    reactor.stop()


######################################################################
#main() function
######################################################################
def main():

    n=20
    if(len(sys.argv)>1):
        n=sys.argv[1]
        
    requestList = []

    printf("Creating list for %s urls...\n", n)
    urlList = buildUrlList(n)
    dl = [] #temp list to hold created defered's
    
    i=0
    for u in urlList:
        if(u):
            req = request(u)
            printf("%03d: %s\n",i,req.url)
            dfrd = getPage(req.url)
            dfrd.addCallbacks(callback=pageRequestCallback, callbackArgs=[ dfrd, req, requestList, True],
                              errback=pageRequestCallback, errbackArgs=[ dfrd, req, requestList, False] )
            
            dl.append(dfrd)
            i=i+1

    printf("\n\n Retrieving Urls...\n")

    deferredList = defer.DeferredList(dl)
    deferredList.addCallbacks(finishCallback, callbackArgs=[requestList])
    reactor.run()




######################################################################
#main() 
######################################################################
main()
