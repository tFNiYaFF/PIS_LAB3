from SPARQLWrapper import SPARQLWrapper, JSON
import json

sparql = SPARQLWrapper("https://query.wikidata.org/sparql")
sparql.setQuery("""SELECT ?avLabel WHERE {
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
  wd:Q19355 wdt:P57 ?name
  OPTIONAL {?name wdt:P166 ?av.}
}""")
sparql.setReturnFormat(JSON)
results = sparql.query().convert()

clean_json = []
for result in results["results"]["bindings"]:
    clean_json.append(result["avLabel"]["value"])
print(json.dumps(clean_json, indent=4))
