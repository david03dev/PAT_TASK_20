from homepage import CowinAutomation
import pytest

# Define the URL for Cowin
url = "https://www.cowin.gov.in/"
cowin = CowinAutomation(url)

@pytest.fixture(scope="module", autouse=True)
def setup():
    cowin.start_automation()
    yield
    cowin.shutdown() 

# Test case for opening FAQ and Partners
def test_open_faq_and_partners():
    window_handles = cowin.open_faq_and_partners()  
    assert len(window_handles) > 1, "FAIL: New windows were not opened."
    print("SUCCESS: New windows opened successfully.")
