# recuprer le secret de github "APIS_KEYS" via le workflow

import os
omg = os.environ.get('APIS_KEYS')

print(omg)