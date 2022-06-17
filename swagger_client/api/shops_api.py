# coding: utf-8

"""
    Getir-Locals Integration Swagger Documentation

    This documentation is created by Getir Developers for Getir-Locals Integration.For this integration, you need to take CLIENT NAME and CLIENT SECRET keys from Getir-dev team and use these keys for authentication. You also need to use access token provided after successful login to be able to use all other endpoints  You can view information about the active order through /orders/unapproved endpoints. The status of the order is managed via verify, prepare, handover and cancel endpoints. Details on order management are as follows:  For orders to be made by the Getir courier, the flow is as follows:  Supplier confirms order --verify<br />Supplier prepares order --prepare (1-2 minutes must pass before delivery)<br />Supplier hands over the order to Getir courier --handover<br />For Getir delivery, transactions are made by the Getir courier after handover.  A valid reason will be requested from the supplier to cancel an order. Valid reasons may vary depending on the instant status of the order. For this reason, before canceling an order, you have to get instant valid order cancellation reasons from /orders/{orderId}/cancel-options endpoint.   # noqa: E501

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class ShopsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_shop(self, shop_id, **kwargs):  # noqa: E501
        """It is used to get the shop informations.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_shop(shop_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str shop_id: (required)
        :return: ApiResponseGetShopResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_shop_with_http_info(shop_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_shop_with_http_info(shop_id, **kwargs)  # noqa: E501
            return data

    def get_shop_with_http_info(self, shop_id, **kwargs):  # noqa: E501
        """It is used to get the shop informations.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_shop_with_http_info(shop_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str shop_id: (required)
        :return: ApiResponseGetShopResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['shop_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_shop" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'shop_id' is set
        if ('shop_id' not in params or
                params['shop_id'] is None):
            raise ValueError("Missing the required parameter `shop_id` when calling `get_shop`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'shop_id' in params:
            path_params['shopId'] = params['shop_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/v1/shops/{shopId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiResponseGetShopResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_shop_courier_working_status(self, body, shop_id, **kwargs):  # noqa: E501
        """It is used to put the shops couiers working status.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_shop_courier_working_status(body, shop_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UpdateShopCouriersStatusRequest body: (required)
        :param str shop_id: (required)
        :return: ApiResponseShopCouriersWorkingStatusResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_shop_courier_working_status_with_http_info(body, shop_id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_shop_courier_working_status_with_http_info(body, shop_id, **kwargs)  # noqa: E501
            return data

    def update_shop_courier_working_status_with_http_info(self, body, shop_id, **kwargs):  # noqa: E501
        """It is used to put the shops couiers working status.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_shop_courier_working_status_with_http_info(body, shop_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UpdateShopCouriersStatusRequest body: (required)
        :param str shop_id: (required)
        :return: ApiResponseShopCouriersWorkingStatusResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'shop_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_shop_courier_working_status" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_shop_courier_working_status`")  # noqa: E501
        # verify the required parameter 'shop_id' is set
        if ('shop_id' not in params or
                params['shop_id'] is None):
            raise ValueError("Missing the required parameter `shop_id` when calling `update_shop_courier_working_status`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'shop_id' in params:
            path_params['shopId'] = params['shop_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/v1/shops/{shopId}/couriers/working-status', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiResponseShopCouriersWorkingStatusResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_shop_working_hours(self, body, shop_id, **kwargs):  # noqa: E501
        """It is used to put the shops working hours.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_shop_working_hours(body, shop_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UpdateShopWorkingHoursRequest body: (required)
        :param str shop_id: (required)
        :return: ApiResponseShopWorkingHoursResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_shop_working_hours_with_http_info(body, shop_id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_shop_working_hours_with_http_info(body, shop_id, **kwargs)  # noqa: E501
            return data

    def update_shop_working_hours_with_http_info(self, body, shop_id, **kwargs):  # noqa: E501
        """It is used to put the shops working hours.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_shop_working_hours_with_http_info(body, shop_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UpdateShopWorkingHoursRequest body: (required)
        :param str shop_id: (required)
        :return: ApiResponseShopWorkingHoursResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'shop_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_shop_working_hours" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_shop_working_hours`")  # noqa: E501
        # verify the required parameter 'shop_id' is set
        if ('shop_id' not in params or
                params['shop_id'] is None):
            raise ValueError("Missing the required parameter `shop_id` when calling `update_shop_working_hours`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'shop_id' in params:
            path_params['shopId'] = params['shop_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/v1/shops/{shopId}/working-hours', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiResponseShopWorkingHoursResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_shop_working_status(self, body, shop_id, **kwargs):  # noqa: E501
        """It is used to put the shops working status.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_shop_working_status(body, shop_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UpdateShopStatusRequest body: (required)
        :param str shop_id: (required)
        :return: ApiResponseObject
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_shop_working_status_with_http_info(body, shop_id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_shop_working_status_with_http_info(body, shop_id, **kwargs)  # noqa: E501
            return data

    def update_shop_working_status_with_http_info(self, body, shop_id, **kwargs):  # noqa: E501
        """It is used to put the shops working status.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_shop_working_status_with_http_info(body, shop_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UpdateShopStatusRequest body: (required)
        :param str shop_id: (required)
        :return: ApiResponseObject
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'shop_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_shop_working_status" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_shop_working_status`")  # noqa: E501
        # verify the required parameter 'shop_id' is set
        if ('shop_id' not in params or
                params['shop_id'] is None):
            raise ValueError("Missing the required parameter `shop_id` when calling `update_shop_working_status`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'shop_id' in params:
            path_params['shopId'] = params['shop_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/v1/shops/{shopId}/working-status', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiResponseObject',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)