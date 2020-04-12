[![Build Status](https://travis-ci.com/anuj-ssharma/FluxTest.svg?branch=master)](https://travis-ci.com/anuj-ssharma/FluxTest)

# Overview
* This repository contains the tests requested as part of the technical tests from Flux Federation. 
* The tests are defined in the `tm_test_motors.py` file. There are 2 tests and one setup step:
    * Setup Step - Requests the used cars API and counts the number of named brands 
    * test for brand existence - Checks that the brand name exists in the response. Test data is parameterised. Also prints outs the count of the cars if exists.
    * test for brand non existence - Checks that the brand name does not exist in the response. Test data is parameterised.

# Test Execution (Travis CI)
The tests are executed as part of the Travis CI. Click on the link above (build passing) to view the test results.

# Running tests locally

1. Install Python 3.8
2. Clone the project `git clone https://github.com/anuj-ssharma/FluxTest.git`
3. Within the project, run `pip install -r requirements.txt`. 
    * if pip is not installed, install using the instructions at (https://pip.pypa.io/en/stable/installing/)
4. Within the project, run `pytest -s`
 
