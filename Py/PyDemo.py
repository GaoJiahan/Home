
import json


d = [{"firstname" : "jiahan","lastname" : "gao"},{"firstname":"qianqiao","lastname":"gao"}]

jd = json.loads('[{"firstname" : "jiahan","lastname" : "gao"},{"firstname":"qianqiao","lastname":"gao"}]')

strd = json.dumps(d)


print(jd[0]["firstname"])