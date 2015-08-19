'''
Created on Aug 15, 2015

@author: Steven
'''

import os
import csv
import re

class_template = """public class {classname} {{
    {declarations}
    
    public {classname}({args}) {{
        {inits}
    }}
    
    public {classname}(Map<String, String> source) {{
        {arraylist_inits}
    }}
    
    {getters}
    {setters}
}}
"""


print("To be pasted into spreadsheets:")
for filename in os.listdir("inputs"):
    
    if (not filename.endswith(".csv") or 
        not filename.count(".") == 1 or 
        not re.match("([a-zA-Z_$][a-zA-Z\d_$]*)*[a-zA-Z_$][a-zA-Z\d_$]*", filename)):
        print("Cannot generate valid class name from %s" % filename)
        continue
    
    reader = csv.DictReader(file(os.path.join("inputs", filename)))
    fieldnames = reader.fieldnames
    original_fieldname_values = fieldnames
    fieldnames = [re.sub("[^a-zA-Z_ ]", "", fieldname) for fieldname in fieldnames]
    fieldnames = [fieldname.strip().replace(" ", "_") for fieldname in fieldnames]
    original_fieldnames = dict(zip(fieldnames, original_fieldname_values))
    
    classname = filename[0].upper() + filename.split(".")[0][1:]
    declarations = "\n    ".join(["private String %s;" % i for i in fieldnames])
    args = ", ".join(["String %s" % i for i in fieldnames])
    inits = "\n        ".join(["this.%s = %s;" % (i, i) for i in fieldnames])
    arraylist_inits = "\n        ".join(["this.%s = source.get(\"%s\");" % (i, original_fieldnames[i]) for i in fieldnames]) 
    
    getters = ""
    setters = ""
    for fieldname in fieldnames:
        
        cased_name = fieldname[0].upper() + fieldname[1:]
        getters += """    public void set{cased_name}(String {fieldname}) {{
        this.{fieldname} = {fieldname};
    }}
    
    """.format(cased_name=cased_name, fieldname=fieldname, 
               original_fieldname = original_fieldnames[fieldname])
    
        setters += """    public String get{cased_name}() {{
        return {fieldname};
    }}
    
    """.format(cased_name=cased_name, fieldname=fieldname)
    
    output_text = class_template.format(classname=classname, args=args,
        inits=inits, arraylist_inits=arraylist_inits,
        getters=getters, setters=setters, declarations=declarations)
    
    java_filename_path = os.path.join("outputs", classname + ".java")
    with file(java_filename_path, "w") as f:
        f.write(output_text)
    
    stdout_text = filename.split(".")[0] + ": "
    for fieldname in fieldnames:
        stdout_text += "${value.%s}\t" % fieldname
    stdout_text = stdout_text[:-1] #drop the last tab char
    print(stdout_text)
print("done")
