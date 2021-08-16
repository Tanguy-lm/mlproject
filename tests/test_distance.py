from mlproject.distance import haversine

def test_length_of_hello_world():
    lat1, lon1 = 48.865070, 2.380009
    lat2, lon2 = 43.7044166, 7.262691
    assert haversine(lon1, lat1, lon2, lat2) >= 0
    assert type(haversine(lon1, lat1, lon2, lat2)) == float
    