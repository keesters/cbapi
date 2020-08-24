# Test to ensure two main functions are working appropriately
# 1) people()
# 2) companies()

import cbapi

def test_cbapi():
  try:
    test_people = cbapi.people(name='Steve',types='investor')
    test_orgs = cbapi.companies(name='Data',locations='California')
  except Exception:
    print("Execution Error")

if __name__ == "__main__":
    test_cbapi()
