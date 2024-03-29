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

class InvoiceAddressResponse(object):
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
        'id': 'str',
        'address': 'str',
        'apt_no': 'str',
        'floor': 'str',
        'door_no': 'str'
    }

    attribute_map = {
        'id': 'id',
        'address': 'address',
        'apt_no': 'aptNo',
        'floor': 'floor',
        'door_no': 'doorNo'
    }

    def __init__(self, id=None, address=None, apt_no=None, floor=None, door_no=None):  # noqa: E501
        """InvoiceAddressResponse - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._address = None
        self._apt_no = None
        self._floor = None
        self._door_no = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if address is not None:
            self.address = address
        if apt_no is not None:
            self.apt_no = apt_no
        if floor is not None:
            self.floor = floor
        if door_no is not None:
            self.door_no = door_no

    @property
    def id(self):
        """Gets the id of this InvoiceAddressResponse.  # noqa: E501


        :return: The id of this InvoiceAddressResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InvoiceAddressResponse.


        :param id: The id of this InvoiceAddressResponse.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def address(self):
        """Gets the address of this InvoiceAddressResponse.  # noqa: E501


        :return: The address of this InvoiceAddressResponse.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this InvoiceAddressResponse.


        :param address: The address of this InvoiceAddressResponse.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def apt_no(self):
        """Gets the apt_no of this InvoiceAddressResponse.  # noqa: E501


        :return: The apt_no of this InvoiceAddressResponse.  # noqa: E501
        :rtype: str
        """
        return self._apt_no

    @apt_no.setter
    def apt_no(self, apt_no):
        """Sets the apt_no of this InvoiceAddressResponse.


        :param apt_no: The apt_no of this InvoiceAddressResponse.  # noqa: E501
        :type: str
        """

        self._apt_no = apt_no

    @property
    def floor(self):
        """Gets the floor of this InvoiceAddressResponse.  # noqa: E501


        :return: The floor of this InvoiceAddressResponse.  # noqa: E501
        :rtype: str
        """
        return self._floor

    @floor.setter
    def floor(self, floor):
        """Sets the floor of this InvoiceAddressResponse.


        :param floor: The floor of this InvoiceAddressResponse.  # noqa: E501
        :type: str
        """

        self._floor = floor

    @property
    def door_no(self):
        """Gets the door_no of this InvoiceAddressResponse.  # noqa: E501


        :return: The door_no of this InvoiceAddressResponse.  # noqa: E501
        :rtype: str
        """
        return self._door_no

    @door_no.setter
    def door_no(self, door_no):
        """Sets the door_no of this InvoiceAddressResponse.


        :param door_no: The door_no of this InvoiceAddressResponse.  # noqa: E501
        :type: str
        """

        self._door_no = door_no

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
        if issubclass(InvoiceAddressResponse, dict):
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
        if not isinstance(other, InvoiceAddressResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
