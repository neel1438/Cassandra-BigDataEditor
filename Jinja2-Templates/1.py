
import jinja2

templateLoader = jinja2.FileSystemLoader( searchpath="/" )
templateEnv = jinja2.Environment( loader=templateLoader )

TEMPLATE_FILE = "/home/nitin/Desktop/cloud_project_work/final-jinja/1.jinja"

template = templateEnv.get_template( TEMPLATE_FILE )

# Here we add a new input variable containing a list.
# Its contents will be expanded in the HTML as a unordered list.
inputs = { "ks_name":"Keyspace Name" , "replication":"Replication Factor" }

# Specify any input variables to the template as a dictionary.
templateVars = { "title" : "Create Keyspace",
                 "description" : "A simple inquiry of function.", 
                 "input" : inputs 
                 }

outputText = template.render( templateVars )
print outputText


