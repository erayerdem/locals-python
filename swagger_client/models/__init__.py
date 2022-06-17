# coding: utf-8

# flake8: noqa
"""
    Getir-Locals Integration Swagger Documentation

    This documentation is created by Getir Developers for Getir-Locals Integration.For this integration, you need to take CLIENT NAME and CLIENT SECRET keys from Getir-dev team and use these keys for authentication. You also need to use access token provided after successful login to be able to use all other endpoints  You can view information about the active order through /orders/unapproved endpoints. The status of the order is managed via verify, prepare, handover and cancel endpoints. Details on order management are as follows:  For orders to be made by the Getir courier, the flow is as follows:  Supplier confirms order --verify<br />Supplier prepares order --prepare (1-2 minutes must pass before delivery)<br />Supplier hands over the order to Getir courier --handover<br />For Getir delivery, transactions are made by the Getir courier after handover.  A valid reason will be requested from the supplier to cancel an order. Valid reasons may vary depending on the instant status of the order. For this reason, before canceling an order, you have to get instant valid order cancellation reasons from /orders/{orderId}/cancel-options endpoint.   # noqa: E501

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

# import models into model package
from swagger_client.models.api_response_authentication_response import ApiResponseAuthenticationResponse
from swagger_client.models.api_response_get_shop_response import ApiResponseGetShopResponse
from swagger_client.models.api_response_list_cancel_option_response import ApiResponseListCancelOptionResponse
from swagger_client.models.api_response_list_order_response import ApiResponseListOrderResponse
from swagger_client.models.api_response_object import ApiResponseObject
from swagger_client.models.api_response_order_report_response import ApiResponseOrderReportResponse
from swagger_client.models.api_response_order_report_response_wrapper import ApiResponseOrderReportResponseWrapper
from swagger_client.models.api_response_pageable_response_shop_products_response import ApiResponsePageableResponseShopProductsResponse
from swagger_client.models.api_response_pageable_response_shop_products_response_data import ApiResponsePageableResponseShopProductsResponseData
from swagger_client.models.api_response_price_and_quantity_batch_response import ApiResponsePriceAndQuantityBatchResponse
from swagger_client.models.api_response_price_and_quantity_batch_response_wrapper import ApiResponsePriceAndQuantityBatchResponseWrapper
from swagger_client.models.api_response_product_batch_ticket_response import ApiResponseProductBatchTicketResponse
from swagger_client.models.api_response_shop_couriers_working_status_response import ApiResponseShopCouriersWorkingStatusResponse
from swagger_client.models.api_response_shop_working_hours_response import ApiResponseShopWorkingHoursResponse
from swagger_client.models.api_response_void import ApiResponseVoid
from swagger_client.models.artisan_order_response import ArtisanOrderResponse
from swagger_client.models.authentication_response import AuthenticationResponse
from swagger_client.models.cancel_option_response import CancelOptionResponse
from swagger_client.models.cancel_order_request import CancelOrderRequest
from swagger_client.models.customer_response import CustomerResponse
from swagger_client.models.field_validation import FieldValidation
from swagger_client.models.general_error import GeneralError
from swagger_client.models.general_error_wrapper import GeneralErrorWrapper
from swagger_client.models.get_shop_response import GetShopResponse
from swagger_client.models.health_response import HealthResponse
from swagger_client.models.internal_error import InternalError
from swagger_client.models.internal_error_wrapper import InternalErrorWrapper
from swagger_client.models.invoice_address_response import InvoiceAddressResponse
from swagger_client.models.invoice_request import InvoiceRequest
from swagger_client.models.menu_options_response import MenuOptionsResponse
from swagger_client.models.model5001_internal_error import Model5001InternalError
from swagger_client.models.name_response import NameResponse
from swagger_client.models.operation_result import OperationResult
from swagger_client.models.order_dto_response import OrderDtoResponse
from swagger_client.models.order_response import OrderResponse
from swagger_client.models.page_size_invalid_error import PageSizeInvalidError
from swagger_client.models.page_size_invalid_error_meta import PageSizeInvalidErrorMeta
from swagger_client.models.pageable_response_supplier_product_response import PageableResponseSupplierProductResponse
from swagger_client.models.password_reset_request import PasswordResetRequest
from swagger_client.models.payment_method_text_response import PaymentMethodTextResponse
from swagger_client.models.prepared_order_request import PreparedOrderRequest
from swagger_client.models.price_and_quantity_batch_product_response import PriceAndQuantityBatchProductResponse
from swagger_client.models.product_batch_request import ProductBatchRequest
from swagger_client.models.product_batch_ticket_response import ProductBatchTicketResponse
from swagger_client.models.product_request import ProductRequest
from swagger_client.models.product_response import ProductResponse
from swagger_client.models.shop_couriers_working_status_response import ShopCouriersWorkingStatusResponse
from swagger_client.models.shop_products_response import ShopProductsResponse
from swagger_client.models.shop_working_hours_response import ShopWorkingHoursResponse
from swagger_client.models.supplier_data_chain_response import SupplierDataChainResponse
from swagger_client.models.supplier_data_response import SupplierDataResponse
from swagger_client.models.supplier_data_response_wrapper import SupplierDataResponseWrapper
from swagger_client.models.supplier_data_shop_response import SupplierDataShopResponse
from swagger_client.models.supplier_product_response import SupplierProductResponse
from swagger_client.models.update_shop_couriers_status_request import UpdateShopCouriersStatusRequest
from swagger_client.models.update_shop_status_request import UpdateShopStatusRequest
from swagger_client.models.update_shop_working_hours_request import UpdateShopWorkingHoursRequest
from swagger_client.models.updated_product import UpdatedProduct