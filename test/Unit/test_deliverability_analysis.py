"""
Tests for DeliverabilityAnalysis enum validation (issue #220).

The US verification API can return dpv_inactive_reason "00", which the
generated model rejected with ApiValueError.
"""

import unittest

from lob_python.model.deliverability_analysis import DeliverabilityAnalysis


def analysis(**overrides):
    fields = dict(
        dpv_confirmation="Y",
        dpv_cmra="N",
        dpv_vacant="N",
        dpv_active="Y",
        dpv_inactive_reason="",
        dpv_throwback="N",
        dpv_non_delivery_day_flag="N",
        dpv_non_delivery_day_values="",
        dpv_no_secure_location="N",
        dpv_door_not_accessible="N",
        dpv_footnotes=["AA", "BB"],
        ews_match=False,
        lacs_indicator="",
        lacs_return_code="",
        suite_return_code="",
    )
    fields.update(overrides)
    return DeliverabilityAnalysis(**fields)


class TestDeliverabilityAnalysis(unittest.TestCase):

    def test_accepts_inactive_reason_00(self):
        self.assertEqual(analysis(dpv_inactive_reason="00").dpv_inactive_reason, "00")

    def test_accepts_documented_inactive_reasons(self):
        for value in ["01", "02", "03", "04", "05", "06", ""]:
            self.assertEqual(analysis(dpv_inactive_reason=value).dpv_inactive_reason, value)

    def test_rejects_unknown_inactive_reason(self):
        with self.assertRaises(Exception):
            analysis(dpv_inactive_reason="99")

    def test_deserializes_response_with_00(self):
        data = {
            "dpv_confirmation": "Y", "dpv_cmra": "N", "dpv_vacant": "N", "dpv_active": "Y",
            "dpv_inactive_reason": "00", "dpv_throwback": "N", "dpv_non_delivery_day_flag": "N",
            "dpv_non_delivery_day_values": "", "dpv_no_secure_location": "N",
            "dpv_door_not_accessible": "N", "dpv_footnotes": ["AA", "BB"], "ews_match": False,
            "lacs_indicator": "", "lacs_return_code": "", "suite_return_code": "",
        }
        model = DeliverabilityAnalysis._from_openapi_data(**data)
        self.assertEqual(model.dpv_inactive_reason, "00")


if __name__ == "__main__":
    unittest.main()
