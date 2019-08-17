import unittest
from schemas.AuthorizeSchema import AuthorizeSchema
from services.TransactionValidator import validate_rules

rule_6_expected = [{
    "rule6": "There should not be more than 3 transactions on a 2 minutes interval"
    }]


rule_6_obj = {
            "account": {
                "cardIsActive": "true",
                "limit": "100",
                "denylist": ["loja", "loja3"]
            },
            "lasttransactions": [{
                    "merchant": "loja",
                    "amount": "10",
                    "time": "2019-08-17T11:02:00.000000"
                }, {
                    "merchant": "loja10",
                    "amount": "20",
                    "time": "2019-08-17T11:02:05.000000"
                },
                 {
                    "merchant": "loja10",
                    "amount": "20",
                    "time": "2019-08-17T11:02:10.000000"
                },
                 {
                    "merchant": "loja10",
                    "amount": "20",
                    "time": "2019-08-17T11:08:00.000000"
                }
            ],
            "transaction": {
                "merchant": "loja10",
                "amount": "80",
                "time": "2019-08-17T11:09:00.000000"
            }
}


class ValidatorRulesTest(unittest.TestCase):
    def test_validate_rule_6(self):
        schema = AuthorizeSchema()
        input_object = schema.load(rule_6_obj)
        self.assertEqual(validate_rules(input_object.data), rule_6_expected)


if __name__ == '__main__':
    unittest.main()
