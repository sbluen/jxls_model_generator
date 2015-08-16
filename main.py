'''
Created on Aug 15, 2015

@author: Steven
'''

import os
import csv
import re

class_template = """public class {classname} {{
    public {classname}({args}) {{
        {inits}
    }}
}}
"""

for filename in os.listdir("inputs"):
    
    if not filename.endswith(".csv"):
        continue
    
    reader = csv.DictReader(file(os.path.join("inputs", filename)))
    fieldnames = reader.fieldnames
    fieldnames = [fieldname.replace(" ", "_") for fieldname in fieldnames]
    fieldnames = [re.sub("[^a-zA-Z_]", "", fieldname) for fieldname in fieldnames]
    
    classname = ".".join(filename.split(".")[:-1])
    args = ", ".join(["String %s" % i for i in fieldnames])
    inits = "\n        ".join(["this.%s = %s;" % (i, i) for i in fieldnames])
    output_text = class_template.format(classname=classname, args=args, inits=inits) 
    java_filename_path = os.path.join("outputs", classname + ".java")
    
    with file(java_filename_path, "w") as f:
        f.write(output_text)
    
print("done")
