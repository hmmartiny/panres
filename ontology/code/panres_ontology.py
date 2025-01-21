import pandas as pd
from owlready2 import *


panres_metadata = pd.read_csv('panres_annotations.csv')
onto = get_ontology("http://test.org/onto.owl")

print(panres_metadata)

# Create objects in the ontology
with onto:
    for metaVariable in panres_metadata['variable'].unique():
        new_property = types.new_class(metaVariable, (ObjectProperty, ))
#variables = panres_metadata['variable'].unique()
#print(variables)

# Save the ontology to a file
onto.save(file="panres.owl", format="rdfxml")
