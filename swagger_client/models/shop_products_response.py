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

class ShopProductsResponse(object):
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
        'status': 'float',
        'type': 'float',
        'price': 'float',
        'product_name': 'str',
        'catalog_product_id': 'str',
        'menu_product_id': 'str',
        'menu_options': 'list[MenuOptionsResponse]',
        'barcodes': 'list[str]'
    }

    attribute_map = {
        'status': 'status',
        'type': 'type',
        'price': 'price',
        'product_name': 'productName',
        'catalog_product_id': 'catalogProductId',
        'menu_product_id': 'menuProductId',
        'menu_options': 'menuOptions',
        'barcodes': 'barcodes'
    }

    def __init__(self, status=None, type=None, price=None, product_name=None, catalog_product_id=None, menu_product_id=None, menu_options=None, barcodes=None):  # noqa: E501
        """ShopProductsResponse - a model defined in Swagger"""  # noqa: E501
        self._status = None
        self._type = None
        self._price = None
        self._product_name = None
        self._catalog_product_id = None
        self._menu_product_id = None
        self._menu_options = None
        self._barcodes = None
        self.discriminator = None
        if status is not None:
            self.status = status
        if type is not None:
            self.type = type
        if price is not None:
            self.price = price
        if product_name is not None:
            self.product_name = product_name
        if catalog_product_id is not None:
            self.catalog_product_id = catalog_product_id
        if menu_product_id is not None:
            self.menu_product_id = menu_product_id
        if menu_options is not None:
            self.menu_options = menu_options
        if barcodes is not None:
            self.barcodes = barcodes

    @property
    def status(self):
        """Gets the status of this ShopProductsResponse.  # noqa: E501


        :return: The status of this ShopProductsResponse.  # noqa: E501
        :rtype: float
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShopProductsResponse.


        :param status: The status of this ShopProductsResponse.  # noqa: E501
        :type: float
        """

        self._status = status

    @property
    def type(self):
        """Gets the type of this ShopProductsResponse.  # noqa: E501


        :return: The type of this ShopProductsResponse.  # noqa: E501
        :rtype: float
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ShopProductsResponse.


        :param type: The type of this ShopProductsResponse.  # noqa: E501
        :type: float
        """

        self._type = type

    @property
    def price(self):
        """Gets the price of this ShopProductsResponse.  # noqa: E501


        :return: The price of this ShopProductsResponse.  # noqa: E501
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this ShopProductsResponse.


        :param price: The price of this ShopProductsResponse.  # noqa: E501
        :type: float
        """

        self._price = price

    @property
    def product_name(self):
        """Gets the product_name of this ShopProductsResponse.  # noqa: E501


        :return: The product_name of this ShopProductsResponse.  # noqa: E501
        :rtype: str
        """
        return self._product_name

    @product_name.setter
    def product_name(self, product_name):
        """Sets the product_name of this ShopProductsResponse.


        :param product_name: The product_name of this ShopProductsResponse.  # noqa: E501
        :type: str
        """

        self._product_name = product_name

    @property
    def catalog_product_id(self):
        """Gets the catalog_product_id of this ShopProductsResponse.  # noqa: E501


        :return: The catalog_product_id of this ShopProductsResponse.  # noqa: E501
        :rtype: str
        """
        return self._catalog_product_id

    @catalog_product_id.setter
    def catalog_product_id(self, catalog_product_id):
        """Sets the catalog_product_id of this ShopProductsResponse.


        :param catalog_product_id: The catalog_product_id of this ShopProductsResponse.  # noqa: E501
        :type: str
        """

        self._catalog_product_id = catalog_product_id

    @property
    def menu_product_id(self):
        """Gets the menu_product_id of this ShopProductsResponse.  # noqa: E501


        :return: The menu_product_id of this ShopProductsResponse.  # noqa: E501
        :rtype: str
        """
        return self._menu_product_id

    @menu_product_id.setter
    def menu_product_id(self, menu_product_id):
        """Sets the menu_product_id of this ShopProductsResponse.


        :param menu_product_id: The menu_product_id of this ShopProductsResponse.  # noqa: E501
        :type: str
        """

        self._menu_product_id = menu_product_id

    @property
    def menu_options(self):
        """Gets the menu_options of this ShopProductsResponse.  # noqa: E501


        :return: The menu_options of this ShopProductsResponse.  # noqa: E501
        :rtype: list[MenuOptionsResponse]
        """
        return self._menu_options

    @menu_options.setter
    def menu_options(self, menu_options):
        """Sets the menu_options of this ShopProductsResponse.


        :param menu_options: The menu_options of this ShopProductsResponse.  # noqa: E501
        :type: list[MenuOptionsResponse]
        """

        self._menu_options = menu_options

    @property
    def barcodes(self):
        """Gets the barcodes of this ShopProductsResponse.  # noqa: E501


        :return: The barcodes of this ShopProductsResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._barcodes

    @barcodes.setter
    def barcodes(self, barcodes):
        """Sets the barcodes of this ShopProductsResponse.


        :param barcodes: The barcodes of this ShopProductsResponse.  # noqa: E501
        :type: list[str]
        """

        self._barcodes = barcodes

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
        if issubclass(ShopProductsResponse, dict):
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
        if not isinstance(other, ShopProductsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other