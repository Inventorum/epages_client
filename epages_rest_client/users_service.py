# DO NOT EDIT THIS FILE. This file will be overwritten when re-running go-raml.


class UsersService:
    def __init__(self, client):
        self.client = client

    def users_confirm_email_change_post(self, data, headers=None, query_params=None, content_type="application/json"):
        """
        It is method for POST /users/confirm-email-change
        """
        if query_params is None:
            query_params = {}

        uri = self.client.base_url + "/users/confirm-email-change"
        return self.client.post(uri, data, headers, query_params, content_type)

    def users_reset_password_post(self, data, headers=None, query_params=None, content_type="application/json"):
        """
        It is method for POST /users/reset-password
        """
        if query_params is None:
            query_params = {}

        uri = self.client.base_url + "/users/reset-password"
        return self.client.post(uri, data, headers, query_params, content_type)

    def users_searchfind_by_username_get(self, headers=None, query_params=None, content_type="application/json"):
        """
        It is method for GET /users/search/find-by-username
        """
        if query_params is None:
            query_params = {}

        uri = self.client.base_url + "/users/search/find-by-username"
        return self.client.get(uri, None, headers, query_params, content_type)

    def users_search_get(self, headers=None, query_params=None, content_type="application/json"):
        """
        It is method for GET /users/search
        """
        if query_params is None:
            query_params = {}

        uri = self.client.base_url + "/users/search"
        return self.client.get(uri, None, headers, query_params, content_type)

    def users_support_delete(self, headers=None, query_params=None, content_type="application/json"):
        """
        It is method for DELETE /users/support
        """
        if query_params is None:
            query_params = {}

        uri = self.client.base_url + "/users/support"
        return self.client.delete(uri, None, headers, query_params, content_type)

    def users_support_get(self, headers=None, query_params=None, content_type="application/json"):
        """
        It is method for GET /users/support
        """
        if query_params is None:
            query_params = {}

        uri = self.client.base_url + "/users/support"
        return self.client.get(uri, None, headers, query_params, content_type)

    def users_support_post(self, data, headers=None, query_params=None, content_type="application/json"):
        """
        It is method for POST /users/support
        """
        if query_params is None:
            query_params = {}

        uri = self.client.base_url + "/users/support"
        return self.client.post(uri, data, headers, query_params, content_type)

    def users_verify_password_post(self, data, headers=None, query_params=None, content_type="application/json"):
        """
        It is method for POST /users/verify-password
        """
        if query_params is None:
            query_params = {}

        uri = self.client.base_url + "/users/verify-password"
        return self.client.post(uri, data, headers, query_params, content_type)

    def users_byIdchange_password_post(
            self,
            data,
            id,
            headers=None,
            query_params=None,
            content_type="application/json"):
        """
        It is method for POST /users/{id}/change-password
        """
        if query_params is None:
            query_params = {}

        uri = self.client.base_url + "/users/" + id + "/change-password"
        return self.client.post(uri, data, headers, query_params, content_type)

    def users_byIdchange_username_post(
            self,
            data,
            id,
            headers=None,
            query_params=None,
            content_type="application/json"):
        """
        It is method for POST /users/{id}/change-username
        """
        if query_params is None:
            query_params = {}

        uri = self.client.base_url + "/users/" + id + "/change-username"
        return self.client.post(uri, data, headers, query_params, content_type)

    def users_byIdroles_get(self, id, headers=None, query_params=None, content_type="application/json"):
        """
        It is method for GET /users/{id}/roles
        """
        if query_params is None:
            query_params = {}

        uri = self.client.base_url + "/users/" + id + "/roles"
        return self.client.get(uri, None, headers, query_params, content_type)

    def users_byIdroles_post(self, data, id, headers=None, query_params=None, content_type="application/json"):
        """
        It is method for POST /users/{id}/roles
        """
        if query_params is None:
            query_params = {}

        uri = self.client.base_url + "/users/" + id + "/roles"
        return self.client.post(uri, data, headers, query_params, content_type)

    def users_byIdroles_put(self, data, id, headers=None, query_params=None, content_type="application/json"):
        """
        It is method for PUT /users/{id}/roles
        """
        if query_params is None:
            query_params = {}

        uri = self.client.base_url + "/users/" + id + "/roles"
        return self.client.put(uri, data, headers, query_params, content_type)

    def users_byId_get(self, id, headers=None, query_params=None, content_type="application/json"):
        """
        It is method for GET /users/{id}
        """
        if query_params is None:
            query_params = {}

        uri = self.client.base_url + "/users/" + id
        return self.client.get(uri, None, headers, query_params, content_type)

    def users_get(self, headers=None, query_params=None, content_type="application/json"):
        """
        It is method for GET /users
        """
        if query_params is None:
            query_params = {}

        uri = self.client.base_url + "/users"
        return self.client.get(uri, None, headers, query_params, content_type)

    def users_post(self, data, headers=None, query_params=None, content_type="application/json"):
        """
        It is method for POST /users
        """
        if query_params is None:
            query_params = {}

        uri = self.client.base_url + "/users"
        return self.client.post(uri, data, headers, query_params, content_type)
