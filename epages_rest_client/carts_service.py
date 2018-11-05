# DO NOT EDIT THIS FILE. This file will be overwritten when re-running go-raml.


class CartsService:
    def __init__(self, client):
        self.client = client

    def carts_byCartIdbilling_address_put(
            self,
            data,
            cartId,
            headers=None,
            query_params=None,
            content_type="application/json"):
        """
        It is method for PUT /carts/{cartId}/billing-address
        """
        if query_params is None:
            query_params = {}

        uri = self.client.base_url + "/carts/" + cartId + "/billing-address"
        return self.client.put(uri, data, headers, query_params, content_type)

    def carts_byCartIdcreate_payment_and_order_post(
            self,
            data,
            cartId,
            headers=None,
            query_params=None,
            content_type="application/json"):
        """
        It is method for POST /carts/{cartId}/create-payment-and-order
        """
        if query_params is None:
            query_params = {}

        uri = self.client.base_url + "/carts/" + cartId + "/create-payment-and-order"
        return self.client.post(uri, data, headers, query_params, content_type)

    def carts_byCartIdcreate_payment_post(
            self,
            data,
            cartId,
            headers=None,
            query_params=None,
            content_type="application/json"):
        """
        It is method for POST /carts/{cartId}/create-payment
        """
        if query_params is None:
            query_params = {}

        uri = self.client.base_url + "/carts/" + cartId + "/create-payment"
        return self.client.post(uri, data, headers, query_params, content_type)

    def carts_byCartIdline_itemslineItemId_delete(
            self,
            cartId,
            lineItemId,
            headers=None,
            query_params=None,
            content_type="application/json"):
        """
        It is method for DELETE /carts/{cartId}/line-items/{lineItemId}
        """
        if query_params is None:
            query_params = {}

        uri = self.client.base_url + "/carts/" + cartId + "/line-items/" + lineItemId
        return self.client.delete(uri, None, headers, query_params, content_type)

    def carts_byCartIdline_itemslineItemId_put(
            self,
            data,
            cartId,
            lineItemId,
            headers=None,
            query_params=None,
            content_type="application/json"):
        """
        It is method for PUT /carts/{cartId}/line-items/{lineItemId}
        """
        if query_params is None:
            query_params = {}

        uri = self.client.base_url + "/carts/" + cartId + "/line-items/" + lineItemId
        return self.client.put(uri, data, headers, query_params, content_type)

    def carts_byCartIdline_items_post(
            self,
            data,
            cartId,
            headers=None,
            query_params=None,
            content_type="application/json"):
        """
        It is method for POST /carts/{cartId}/line-items
        """
        if query_params is None:
            query_params = {}

        uri = self.client.base_url + "/carts/" + cartId + "/line-items"
        return self.client.post(uri, data, headers, query_params, content_type)

    def carts_byCartIdline_items_put(
            self,
            data,
            cartId,
            headers=None,
            query_params=None,
            content_type="application/json"):
        """
        It is method for PUT /carts/{cartId}/line-items
        """
        if query_params is None:
            query_params = {}

        uri = self.client.base_url + "/carts/" + cartId + "/line-items"
        return self.client.put(uri, data, headers, query_params, content_type)

    def carts_byCartIdorder_post(self, data, cartId, headers=None, query_params=None, content_type="application/json"):
        """
        It is method for POST /carts/{cartId}/order
        """
        if query_params is None:
            query_params = {}

        uri = self.client.base_url + "/carts/" + cartId + "/order"
        return self.client.post(uri, data, headers, query_params, content_type)

    def carts_byCartIdpayment_methodscurrent_get(
            self,
            cartId,
            headers=None,
            query_params=None,
            content_type="application/json"):
        """
        It is method for GET /carts/{cartId}/payment-methods/current
        """
        if query_params is None:
            query_params = {}

        uri = self.client.base_url + "/carts/" + cartId + "/payment-methods/current"
        return self.client.get(uri, None, headers, query_params, content_type)

    def carts_byCartIdpayment_methodscurrent_put(
            self,
            data,
            cartId,
            headers=None,
            query_params=None,
            content_type="application/json"):
        """
        It is method for PUT /carts/{cartId}/payment-methods/current
        """
        if query_params is None:
            query_params = {}

        uri = self.client.base_url + "/carts/" + cartId + "/payment-methods/current"
        return self.client.put(uri, data, headers, query_params, content_type)

    def carts_byCartIdpayment_methodsdefault_put(
            self,
            data,
            cartId,
            headers=None,
            query_params=None,
            content_type="application/json"):
        """
        It is method for PUT /carts/{cartId}/payment-methods/default
        """
        if query_params is None:
            query_params = {}

        uri = self.client.base_url + "/carts/" + cartId + "/payment-methods/default"
        return self.client.put(uri, data, headers, query_params, content_type)

    def carts_byCartIdpayment_methods_get(
            self,
            cartId,
            headers=None,
            query_params=None,
            content_type="application/json"):
        """
        It is method for GET /carts/{cartId}/payment-methods
        """
        if query_params is None:
            query_params = {}

        uri = self.client.base_url + "/carts/" + cartId + "/payment-methods"
        return self.client.get(uri, None, headers, query_params, content_type)

    def carts_byCartIdshipping_address_put(
            self,
            data,
            cartId,
            headers=None,
            query_params=None,
            content_type="application/json"):
        """
        It is method for PUT /carts/{cartId}/shipping-address
        """
        if query_params is None:
            query_params = {}

        uri = self.client.base_url + "/carts/" + cartId + "/shipping-address"
        return self.client.put(uri, data, headers, query_params, content_type)

    def carts_byCartIdshipping_methodscurrent_get(
            self,
            cartId,
            headers=None,
            query_params=None,
            content_type="application/json"):
        """
        It is method for GET /carts/{cartId}/shipping-methods/current
        """
        if query_params is None:
            query_params = {}

        uri = self.client.base_url + "/carts/" + cartId + "/shipping-methods/current"
        return self.client.get(uri, None, headers, query_params, content_type)

    def carts_byCartIdshipping_methodscurrent_put(
            self,
            data,
            cartId,
            headers=None,
            query_params=None,
            content_type="application/json"):
        """
        It is method for PUT /carts/{cartId}/shipping-methods/current
        """
        if query_params is None:
            query_params = {}

        uri = self.client.base_url + "/carts/" + cartId + "/shipping-methods/current"
        return self.client.put(uri, data, headers, query_params, content_type)

    def carts_byCartIdshipping_methodsdefault_put(
            self,
            data,
            cartId,
            headers=None,
            query_params=None,
            content_type="application/json"):
        """
        It is method for PUT /carts/{cartId}/shipping-methods/default
        """
        if query_params is None:
            query_params = {}

        uri = self.client.base_url + "/carts/" + cartId + "/shipping-methods/default"
        return self.client.put(uri, data, headers, query_params, content_type)

    def carts_byCartIdshipping_methods_get(
            self,
            cartId,
            headers=None,
            query_params=None,
            content_type="application/json"):
        """
        It is method for GET /carts/{cartId}/shipping-methods
        """
        if query_params is None:
            query_params = {}

        uri = self.client.base_url + "/carts/" + cartId + "/shipping-methods"
        return self.client.get(uri, None, headers, query_params, content_type)

    def carts_byCartId_delete(self, cartId, headers=None, query_params=None, content_type="application/json"):
        """
        It is method for DELETE /carts/{cartId}
        """
        if query_params is None:
            query_params = {}

        uri = self.client.base_url + "/carts/" + cartId
        return self.client.delete(uri, None, headers, query_params, content_type)

    def carts_byCartId_get(self, cartId, headers=None, query_params=None, content_type="application/json"):
        """
        It is method for GET /carts/{cartId}
        """
        if query_params is None:
            query_params = {}

        uri = self.client.base_url + "/carts/" + cartId
        return self.client.get(uri, None, headers, query_params, content_type)

    def carts_post(self, data, headers=None, query_params=None, content_type="application/json"):
        """
        It is method for POST /carts
        """
        if query_params is None:
            query_params = {}

        uri = self.client.base_url + "/carts"
        return self.client.post(uri, data, headers, query_params, content_type)