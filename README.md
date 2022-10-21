## Running Test via Python3 Virtual Env
*Pre-requisite:* python3 should be installed in the machine
1. Create virtual env: 
> python3 -m venv bookingenv
2. Activate Environment: 
> source bookingenv/bin/activate
3. Install Package dependencies: 
> pip3 install -r requirements.txt
4. Install playwright: 
> playwright install
5. Run the test case: use command with --headed if wants to run with actual browser
> python3 -m pytest --headed tests/test_book_attraction.py
> python3 -m pytest tests/test_book_attraction.py



## Running Test via docker
*Pre-requisite:* docker should be installed in the machine
1. Make a build
> make build
2. Run the test
> make test



## Some Notes:
* Make sure the date selected in the test file is in the future
* if docker fails, check if playwright image has a new version