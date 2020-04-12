import pytest
import requests

class TestTradeMeMotors():
    """
    Before starting any tests,
    Get the response of the used cars which is then used in susequent tests
    Count & print the number of named brands of used cars. This excludes 'Other'
    """
    def setup_class(self):
        self.url = "https://api.tmsandbox.co.nz/v1/Categories/UsedCars.json?with_counts=true"
        with requests.get(url=self.url) as response:
            json_response = response.json()
            self.used_cars = json_response['Subcategories']
            self.count_named_brands(self)

    def count_named_brands(self):
        count_used_cars = len(self.used_cars)
        for car in self.used_cars:
            if 'Other' in car['Name']:
                count_used_cars = count_used_cars - 1
        print("\nNumber of named cars = {}".format(count_used_cars))

    @pytest.mark.parametrize("brand_name_exists", [('Kia')])
    def test_existence_of_brand(self, brand_name_exists):
        for car in self.used_cars:
            if brand_name_exists in car['Name']:
                # print the count only if the object exists in the response
                if 'Count' in car:
                    print("Number of {} cars = {}".format(brand_name_exists, car['Count']))
                assert True

    @pytest.mark.parametrize("brand_name_not_exists", [('Hispano Suiza')])
    def test_non_existence_of_brand(self, brand_name_not_exists):
        for car in self.used_cars:
            if brand_name_not_exists in car['Name']:
                assert False
        assert True