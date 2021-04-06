import json
import pickle
from pprint import pprint
from haversine import haversine_vector, Unit


def main_write_coords():
  with open('coords_data.json') as input:
    data = json.load(input)
    # data = data[0:10]
    for warning in [c for c in data if 'centre' not in c]:
      pprint(warning['code'])

    result = { c['code'] : (c['centre']['coordinates'][1], c['centre']['coordinates'][0]) for c in data if 'centre' in c }
    # pprint(result)

    with open('coords.pickle', 'bw+') as output:
      pickle.dump(result, output)



def main_read_coords():
    with open('coords.pickle', 'br') as input:
      result = pickle.load(input)

    base_key = b'69123'
    key = base_key if isinstance(base_key, str) else base_key.decode('utf-8')
    if key in result:
      pprint('ok')
      pprint(result[key])
    else:
      pprint('KO')


def main_formula():
  lyon = (45.7597, 4.8422) # (lat, lon)
  paris = (48.8567, 2.3508)
  error = (float('nan'), float('nan'))
  pprint(haversine_vector([lyon, lyon], [paris, error], Unit.KILOMETERS))



if __name__ == '__main__':
  # main_write_coords()
  main_read_coords()
  # main_formula()
