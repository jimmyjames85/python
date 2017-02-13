from subprocess import call
import os
import time
import datetime

class A(object):
    config = ''
    def __init__(self, config):
        self.config = config + 'A'
    	print "Constructor A was called with: ", self.config

class B(A):
    def __init__(self, config):
        super(B, self).__init__(config)
        self.config = self.config + 'B'        
    	print "Constructor B was called with: ", self.config

class C(B):
    def __init__(self, config):
        B.__init__(self, config)
        self.config = self.config + 'C' 
    	print "Constructor C was called with: ", self.config



arr=[1,2,3,4]

val = None

if(len(arr)>4):
    val = arr[4]

if val == None:
    val = 15;

print "val is " + str(val)


myvar = {}
myvar['n'] = 0


myvar['n'] = 2
print "myvar['n'] = " , myvar['n'], "\n"
# c = C("config_here:")


mymap = {"age":134, "name":"oldman"}

msg = "len of mymap is "
msg +=  str(len(mymap))
print msg

logfile = open('/tmp/test.log', 'w')
logfile.write('hello world\nhowdy doody :-)\n')
logfile.close()
call(["cat", "/tmp/test.log"])
ts = time.time()
print ts
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
print st


msg = "creating new pool for " + "(table)" + " " + "type" + " " + "3" + " with " + str(34) + " connections and max-pending depth of " + str(34)
logfile = open('/tmp/test.log', 'w')
logfile.close()


print msg


def walk(somedict, level=0):
    for key, item in somedict.iteritems():
        tabs = ""
        for i in range(level):
            tabs += "\t"

        if type(item).__name__ == "dict":
            print tabs, key, "  {dict}"
            walk(item, level+1)
        else:
            print tabs, key, "=" , str(item)


mymap["new"] = {}
mymap["new"]["one"] = "hi"
mymap["new"]["two"] = {}
mymap["new"]["two"]["abc"] = "hi"
mymap["new"]["two"]["def"] = "bye"

for key, item in mymap.iteritems():
    print key
    print item
    print type(item).__name__

print "\n walkingh mymap   \n"    
walk(mymap)

if mymap["new"] == 2:
    print "yup"

del mymap["new"]
    
if "new" in  mymap:
    print "yup"
else:
    print "nope"

call(["clear"])

mymap = {}







resources = {}
dbs = {}
hosts = {}

def createPool(table, type, host, db, max_connections):

    
    if not table in dbs:
        dbs[table] = {}

    if not host in hosts:
        hosts[host] = {}

    if db in hosts[host]:
        #reuse conn
        dbs[table][type] = hosts[host][db]
        return

    max_pending_call_depth = 32;

    print("Creating a new pool with " + str(max_connections) + " connections and a max-pending depth of " + str(max_pending_call_depth) +
            " to " + host + ":" + db + " for " + str(type) + " resource '" + str(table) + "'")

    resource = table + ":" + host + ":" + db + ":" + str(type) + ":" + str(max_connections)

    dbs[table][type] = resource
    hosts[host][db] = resource



    
