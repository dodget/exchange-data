from exchangerizer import build_output_data

TEST_DATA = [
    {
        "key": "value",
        "2. From_Currency Name": "Foo",
        "4. To_Currency Name": "Bar",
        "5. Exchange Rate": "1000.010000"
    },
    {
        "I": "don't care :)",
        "2. From_Currency Name": "Bin",
        "4. To_Currency Name": "Sh",
        "5. Exchange Rate": "-10.01"
    }
]


def test_build_output_data():
    expected = [
        {
            "from": "Foo",
            "to": "Bar",
            "exchange": 1000.01
        },
        {
            "from": "Bin",
            "to": "Sh",
            "exchange": -10.01
        }
    ]
    assert build_output_data(TEST_DATA) == expected