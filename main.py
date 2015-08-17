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
    
    public {classname}(List source) {{
        {arraylist_inits}
    }}
    
    {getters}
    {setters}
}}
"""

for filename in os.listdir("inputs"):
    
    if not filename.endswith(".csv"):
        continue
    
    reader = csv.DictReader(file(os.path.join("inputs", filename)))
    fieldnames = reader.fieldnames
    fieldnames = [fieldname.replace(" ", "_") for fieldname in fieldnames]
    fieldnames = [re.sub("[^a-zA-Z_]", "", fieldname) for fieldname in fieldnames]
    
    classname = filename[0].upper() + filename.split(".")[0][1:]
    args = ", ".join(["String %s" % i for i in fieldnames])
    inits = "\n        ".join(["this.%s = %s;" % (i, i) for i in fieldnames])
    arraylist_inits = "\n        ".join(["this.%s = source.get(%s);" % (i, i) for i in fieldnames]) 
    
    getters = ""
    setters = ""
    for fieldname in fieldnames:
        
        cased_name = fieldname[0].upper() + fieldname[1:]
        getters += """    public void set{cased_name}(String {fieldname}) {{
        this.{fieldname} = {fieldname};
    }}
    
    """.format(cased_name=cased_name, fieldname=fieldname)
    
        setters += """    public String get{cased_name}() {{
        return {fieldname};
    }}
    
    """.format(cased_name=cased_name, fieldname=fieldname)
    
    output_text = class_template.format(classname=classname, args=args,
        inits=inits, arraylist_inits=arraylist_inits,
        getters=getters, setters=setters)
    
    java_filename_path = os.path.join("outputs", classname + ".java")
    with file(java_filename_path, "w") as f:
        f.write(output_text)
    
print("done")
