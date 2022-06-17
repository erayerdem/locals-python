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

class ApiResponseAuthenticationResponse(object):
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
        'meta': 'OperationResult',
        'data': 'AuthenticationResponse'
    }

    attribute_map = {
        'meta': 'meta',
        'data': 'data'
    }

    def __init__(self, meta=None, data=None):  # noqa: E501
        """ApiResponseAuthenticationResponse - a model defined in Swagger"""  # noqa: E501
        self._meta = None
        self._data = None
        self.discriminator = None
        if meta is not None:
            self.meta = meta
        if data is not None:
            self.data = data

    @property
    def meta(self):
        """Gets the meta of this ApiResponseAuthenticationResponse.  # noqa: E501


        :return: The meta of this ApiResponseAuthenticationResponse.  # noqa: E501
        :rtype: OperationResult
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this ApiResponseAuthenticationResponse.


        :param meta: The meta of this ApiResponseAuthenticationResponse.  # noqa: E501
        :type: OperationResult
        """

        self._meta = meta

    @property
    def data(self):
        """Gets the data of this ApiResponseAuthenticationResponse.  # noqa: E501


        :return: The data of this ApiResponseAuthenticationResponse.  # noqa: E501
        :rtype: AuthenticationResponse
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this ApiResponseAuthenticationResponse.


        :param data: The data of this ApiResponseAuthenticationResponse.  # noqa: E501
        :type: AuthenticationResponse
        """

        self._data = data

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
        if issubclass(ApiResponseAuthenticationResponse, dict):
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
        if not isinstance(other, ApiResponseAuthenticationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
