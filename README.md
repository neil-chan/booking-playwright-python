## Steps how to run(needs python3 installed in the machine):
1. Create virtual env: 
> python3 -m venv bookingenv

2. Activate Environment: 
> souce bookingenv/bin/activate

3. Install Package dependencies: 
> pip3 install -r requirements.txt

4. Install playwright: 
> playwright install

5. Run the test case: 
> python3 -m pytest tests/test_book_attraction.py



***Notes:***
* to run headless, remove  *--headed* in pytest.ini