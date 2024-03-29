# coding: utf-8

"""
    Getir-Locals Integration Swagger Documentation

    This documentation is created by Getir Developers for Getir-Locals Integration.For this integration, you need to take CLIENT NAME and CLIENT SECRET keys from Getir-dev team and use these keys for authentication. You also need to use access token provided after successful login to be able to use all other endpoints  You can view information about the active order through /orders/unapproved endpoints. The status of the order is managed via verify, prepare, handover and cancel endpoints. Details on order management are as follows:  For orders to be made by the Getir courier, the flow is as follows:  Supplier confirms order --verify<br />Supplier prepares order --prepare (1-2 minutes must pass before delivery)<br />Supplier hands over the order to Getir courier --handover<br />For Getir delivery, transactions are made by the Getir courier after handover.  A valid reason will be requested from the supplier to cancel an order. Valid reasons may vary depending on the instant status of the order. For this reason, before canceling an order, you have to get instant valid order cancellation reasons from /orders/{orderId}/cancel-options endpoint.   # noqa: E501

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class OrderDtoResponse(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'order_id': 'str',
        'shop_id': 'str',
        'order_date': 'str',
        'cancel_source_code': 'float',
        'order_status_code': 'float',
        'order_total_price': 'float',
        'total_charged_amount_after_provision_or_refund': 'float'
    }

    attribute_map = {
        'order_id': 'orderId',
        'shop_id': 'shopId',
        'order_date': 'orderDate',
        'cancel_source_code': 'cancelSourceCode',
        'order_status_code': 'orderStatusCode',
        'order_total_price': 'orderTotalPrice',
        'total_charged_amount_after_provision_or_refund': 'totalChargedAmountAfterProvisionOrRefund'
    }

    def __init__(self, order_id=None, shop_id=None, order_date=None, cancel_source_code=None, order_status_code=None, order_total_price=None, total_charged_amount_after_provision_or_refund=None):  # noqa: E501
        """OrderDtoResponse - a model defined in Swagger"""  # noqa: E501
        self._order_id = None
        self._shop_id = None
        self._order_date = None
        self._cancel_source_code = None
        self._order_status_code = None
        self._order_total_price = None
        self._total_charged_amount_after_provision_or_refund = None
        self.discriminator = None
        if order_id is not None:
            self.order_id = order_id
        if shop_id is not None:
            self.shop_id = shop_id
        if order_date is not None:
            self.order_date = order_date
        if cancel_source_code is not None:
            self.cancel_source_code = cancel_source_code
        if order_status_code is not None:
            self.order_status_code = order_status_code
        if order_total_price is not None:
            self.order_total_price = order_total_price
        if total_charged_amount_after_provision_or_refund is not None:
            self.total_charged_amount_after_provision_or_refund = total_charged_amount_after_provision_or_refund

    @property
    def order_id(self):
        """Gets the order_id of this OrderDtoResponse.  # noqa: E501


        :return: The order_id of this OrderDtoResponse.  # noqa: E501
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this OrderDtoResponse.


        :param order_id: The order_id of this OrderDtoResponse.  # noqa: E501
        :type: str
        """

        self._order_id = order_id

    @property
    def shop_id(self):
        """Gets the shop_id of this OrderDtoResponse.  # noqa: E501


        :return: The shop_id of this OrderDtoResponse.  # noqa: E501
        :rtype: str
        """
        return self._shop_id

    @shop_id.setter
    def shop_id(self, shop_id):
        """Sets the shop_id of this OrderDtoResponse.


        :param shop_id: The shop_id of this OrderDtoResponse.  # noqa: E501
        :type: str
        """

        self._shop_id = shop_id

    @property
    def order_date(self):
        """Gets the order_date of this OrderDtoResponse.  # noqa: E501


        :return: The order_date of this OrderDtoResponse.  # noqa: E501
        :rtype: str
        """
        return self._order_date

    @order_date.setter
    def order_date(self, order_date):
        """Sets the order_date of this OrderDtoResponse.


        :param order_date: The order_date of this OrderDtoResponse.  # noqa: E501
        :type: str
        """

        self._order_date = order_date

    @property
    def cancel_source_code(self):
        """Gets the cancel_source_code of this OrderDtoResponse.  # noqa: E501


        :return: The cancel_source_code of this OrderDtoResponse.  # noqa: E501
        :rtype: float
        """
        return self._cancel_source_code

    @cancel_source_code.setter
    def cancel_source_code(self, cancel_source_code):
        """Sets the cancel_source_code of this OrderDtoResponse.


        :param cancel_source_code: The cancel_source_code of this OrderDtoResponse.  # noqa: E501
        :type: float
        """

        self._cancel_source_code = cancel_source_code

    @property
    def order_status_code(self):
        """Gets the order_status_code of this OrderDtoResponse.  # noqa: E501


        :return: The order_status_code of this OrderDtoResponse.  # noqa: E501
        :rtype: float
        """
        return self._order_status_code

    @order_status_code.setter
    def order_status_code(self, order_status_code):
        """Sets the order_status_code of this OrderDtoResponse.


        :param order_status_code: The order_status_code of this OrderDtoResponse.  # noqa: E501
        :type: float
        """

        self._order_status_code = order_status_code

    @property
    def order_total_price(self):
        """Gets the order_total_price of this OrderDtoResponse.  # noqa: E501


        :return: The order_total_price of this OrderDtoResponse.  # noqa: E501
        :rtype: float
        """
        return self._order_total_price

    @order_total_price.setter
    def order_total_price(self, order_total_price):
        """Sets the order_total_price of this OrderDtoResponse.


        :param order_total_price: The order_total_price of this OrderDtoResponse.  # noqa: E501
        :type: float
        """

        self._order_total_price = order_total_price

    @property
    def total_charged_amount_after_provision_or_refund(self):
        """Gets the total_charged_amount_after_provision_or_refund of this OrderDtoResponse.  # noqa: E501


        :return: The total_charged_amount_after_provision_or_refund of this OrderDtoResponse.  # noqa: E501
        :rtype: float
        """
        return self._total_charged_amount_after_provision_or_refund

    @total_charged_amount_after_provision_or_refund.setter
    def total_charged_amount_after_provision_or_refund(self, total_charged_amount_after_provision_or_refund):
        """Sets the total_charged_amount_after_provision_or_refund of this OrderDtoResponse.


        :param total_charged_amount_after_provision_or_refund: The total_charged_amount_after_provision_or_refund of this OrderDtoResponse.  # noqa: E501
        :type: float
        """

        self._total_charged_amount_after_provision_or_refund = total_charged_amount_after_provision_or_refund

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(OrderDtoResponse, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, OrderDtoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
