student_data={"id1":
    {"name":["Sara"],
     "class":["V"],
     "subjectintegration":["english,sanskrit","SST"]
    },
    "id2":
     {"name":["Atharvan"],
     "class":["VII"],
     "subjectintegration":["english","Hindi","SST"] 
    },
    "id3":
      {"name":["Sara"],
     "class":["V"],
     "subjectintegration":["english,sanskrit","SST"]
    },
    "id4":
      {"name":["Zunairah"],
     "class":["VII"],
     "subjectintegration":["Science,sanskrit","SST"]
     },
}

result={}

for key,value in student_data.items():
    if value not in result.values():
        result[key]=value

print(result)