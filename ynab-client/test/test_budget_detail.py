# coding: utf-8

"""
    YNAB API Endpoints

    Our API uses a REST based design, leverages the JSON data format, and relies upon HTTPS for transport. We respond with meaningful HTTP response codes and if an error occurs, we include error details in the response body.  API Documentation is at https://api.youneedabudget.com  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import openapi_client
from openapi_client.models.budget_detail import BudgetDetail  # noqa: E501
from openapi_client.rest import ApiException

class TestBudgetDetail(unittest.TestCase):
    """BudgetDetail unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test BudgetDetail
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.budget_detail.BudgetDetail()  # noqa: E501
        if include_optional :
            return BudgetDetail(
                id = '0', 
                name = '0', 
                last_modified_on = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                first_month = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                last_month = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                date_format = openapi_client.models.date_format.DateFormat(
                    format = '0', ), 
                currency_format = openapi_client.models.currency_format.CurrencyFormat(
                    iso_code = '0', 
                    example_format = '0', 
                    decimal_digits = 56, 
                    decimal_separator = '0', 
                    symbol_first = True, 
                    group_separator = '0', 
                    currency_symbol = '0', 
                    display_symbol = True, ), 
                accounts = [
                    openapi_client.models.account.Account(
                        id = '0', 
                        name = '0', 
                        type = 'checking', 
                        on_budget = True, 
                        closed = True, 
                        note = '0', 
                        balance = 56, 
                        cleared_balance = 56, 
                        uncleared_balance = 56, 
                        transfer_payee_id = '0', 
                        deleted = True, )
                    ], 
                payees = [
                    openapi_client.models.payee.Payee(
                        id = '0', 
                        name = '0', 
                        transfer_account_id = '0', 
                        deleted = True, )
                    ], 
                payee_locations = [
                    openapi_client.models.payee_location.PayeeLocation(
                        id = '0', 
                        payee_id = '0', 
                        latitude = '0', 
                        longitude = '0', 
                        deleted = True, )
                    ], 
                category_groups = [
                    openapi_client.models.category_group.CategoryGroup(
                        id = '0', 
                        name = '0', 
                        hidden = True, 
                        deleted = True, )
                    ], 
                categories = [
                    openapi_client.models.category.Category(
                        id = '0', 
                        category_group_id = '0', 
                        name = '0', 
                        hidden = True, 
                        original_category_group_id = '0', 
                        note = '0', 
                        budgeted = 56, 
                        activity = 56, 
                        balance = 56, 
                        goal_type = 'TB', 
                        goal_creation_month = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        goal_target = 56, 
                        goal_target_month = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        goal_percentage_complete = 56, 
                        deleted = True, )
                    ], 
                months = [
                    null
                    ], 
                transactions = [
                    openapi_client.models.transaction_summary.TransactionSummary(
                        id = '0', 
                        date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        amount = 56, 
                        memo = '0', 
                        cleared = 'cleared', 
                        approved = True, 
                        flag_color = 'red', 
                        account_id = '0', 
                        payee_id = '0', 
                        category_id = '0', 
                        transfer_account_id = '0', 
                        transfer_transaction_id = '0', 
                        matched_transaction_id = '0', 
                        import_id = '0', 
                        deleted = True, )
                    ], 
                subtransactions = [
                    openapi_client.models.sub_transaction.SubTransaction(
                        id = '0', 
                        transaction_id = '0', 
                        amount = 56, 
                        memo = '0', 
                        payee_id = '0', 
                        category_id = '0', 
                        transfer_account_id = '0', 
                        deleted = True, )
                    ], 
                scheduled_transactions = [
                    openapi_client.models.scheduled_transaction_summary.ScheduledTransactionSummary(
                        id = '0', 
                        date_first = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        date_next = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        frequency = 'never', 
                        amount = 56, 
                        memo = '0', 
                        flag_color = 'red', 
                        account_id = '0', 
                        payee_id = '0', 
                        category_id = '0', 
                        transfer_account_id = '0', 
                        deleted = True, )
                    ], 
                scheduled_subtransactions = [
                    openapi_client.models.scheduled_sub_transaction.ScheduledSubTransaction(
                        id = '0', 
                        scheduled_transaction_id = '0', 
                        amount = 56, 
                        memo = '0', 
                        payee_id = '0', 
                        category_id = '0', 
                        transfer_account_id = '0', 
                        deleted = True, )
                    ]
            )
        else :
            return BudgetDetail(
                id = '0',
                name = '0',
        )

    def testBudgetDetail(self):
        """Test BudgetDetail"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
