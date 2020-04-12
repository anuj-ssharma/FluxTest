import pytest
import requests

class TestTradeMeMotors():
    def setup_class(self):
        self.url = "https://api.tmsandbox.co.nz/v1/Categories/UsedCars.json?with_counts=true"
        response = requests.get(url=self.url)
        json_response = response.json()
        self.used_cars = json_response['Subcategories']
        self.count_named_brands(self)

    def count_named_brands(self):
        count_used_cars = len(self.used_cars)
        for car in self.used_cars:
            if 'Other' in car['Name']:
                count_used_cars = count_used_cars - 1
        print("\nNumber of named cars = {}".format(count_used_cars))

    @pytest.fixture
    def brand_name_exists(self):
        return 'Kia'

    @pytest.fixture
    def brand_name_not_exists(self):
        return 'Hispano Suiza'

    def test_existence_of_brand(self, brand_name_exists):
        for car in self.used_cars:
            if brand_name_exists in car['Name']:
                print("Number of {} cars = {}".format(brand_name_exists, car['Count']))
                assert True

    def test_non_existence_of_brand(self, brand_name_not_exists):
        for car in self.used_cars:
            if brand_name_not_exists in car['Name']:
                assert False
        assert True