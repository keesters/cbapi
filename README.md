# CrunchBase API
CrunchBase API is a library to allow downloading and presenting organization and people data from Crunchbase.

## Quick Start
There are two main functions to be used in the CrunchBase API.
These functions allow you to pull people and organization data directly from CrunchBase fitting a given set of inputs.
```python
import cbapi

people_data = cbapi.people(name='Steve',types='investor') # returns people data based on the given inputs
companies_data = cbapi.companies(name='Data',locations='California') # returns company data based on the given inputs
```
## Installation
Use the package manager [pip](https://github.com/keesters/cbapi.git) to install cbapi.

```bash
pip install git+https://github.com/keesters/cbapi.git
```

