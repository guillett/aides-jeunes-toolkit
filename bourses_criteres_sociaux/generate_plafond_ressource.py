from pyexcel_ods import get_data
from pprint import pprint
import yaml


def main():
  data = get_data("/home/thomas/Documents/mes-aides.org/Jeunes/bourse.ods")
  pprint(data)

  dates = list(data.keys())
  date = dates[0]
  page = data[date]
  headers = page[0]

  echelons = headers[1:]
  result = {}

  for (echelon_col, echelon) in enumerate(echelons, start=1):
    name = "echelon_{}".format(echelon)
    pprint((echelon_col, name))
    brackets = list()
    for pts in range(1, len(page)):
      brackets.append({
        "threshold": {date : { "value": page[pts][0]}},
        "amount": {date : { "value": page[pts][echelon_col]}},
        })
    result[name] = {
      "metadata": { "type": "single_amount" },
    }
    result[name]["brackets"] = brackets



  print(yaml.dump(result))


if __name__ == '__main__':
  main()
