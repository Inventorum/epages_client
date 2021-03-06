# DO NOT EDIT THIS FILE. This file will be overwritten when re-running go-raml.


class Private_appsService:
    def __init__(self, client):
        self.client = client

    def private_apps_byIdregenerate_client_secret_post(
            self,
            data,
            id,
            headers=None,
            query_params=None,
            content_type="application/json"):
        """
        It is method for POST /private-apps/{id}/regenerate-client-secret
        """
        if query_params is None:
            query_params = {}

        uri = self.client.base_url + "/private-apps/" + id + "/regenerate-client-secret"
        return self.client.post(uri, data, headers, query_params, content_type)

    def private_apps_byIdscopes_get(self, id, headers=None, query_params=None, content_type="application/json"):
        """
        It is method for GET /private-apps/{id}/scopes
        """
        if query_params is None:
            query_params = {}

        uri = self.client.base_url + "/private-apps/" + id + "/scopes"
        return self.client.get(uri, None, headers, query_params, content_type)

    def private_apps_byIdscopes_put(self, data, id, headers=None, query_params=None, content_type="application/json"):
        """
        It is method for PUT /private-apps/{id}/scopes
        """
        if query_params is None:
            query_params = {}

        uri = self.client.base_url + "/private-apps/" + id + "/scopes"
        return self.client.put(uri, data, headers, query_params, content_type)

    def private_apps_byId_delete(self, id, headers=None, query_params=None, content_type="application/json"):
        """
        It is method for DELETE /private-apps/{id}
        """
        if query_params is None:
            query_params = {}

        uri = self.client.base_url + "/private-apps/" + id
        return self.client.delete(uri, None, headers, query_params, content_type)

    def private_apps_byId_get(self, id, headers=None, query_params=None, content_type="application/json"):
        """
        It is method for GET /private-apps/{id}
        """
        if query_params is None:
            query_params = {}

        uri = self.client.base_url + "/private-apps/" + id
        return self.client.get(uri, None, headers, query_params, content_type)

    def private_apps_byId_put(self, data, id, headers=None, query_params=None, content_type="application/json"):
        """
        It is method for PUT /private-apps/{id}
        """
        if query_params is None:
            query_params = {}

        uri = self.client.base_url + "/private-apps/" + id
        return self.client.put(uri, data, headers, query_params, content_type)

    def private_apps_get(self, headers=None, query_params=None, content_type="application/json"):
        """
        It is method for GET /private-apps
        """
        if query_params is None:
            query_params = {}

        uri = self.client.base_url + "/private-apps"
        return self.client.get(uri, None, headers, query_params, content_type)

    def private_apps_post(self, data, headers=None, query_params=None, content_type="application/json"):
        """
        It is method for POST /private-apps
        """
        if query_params is None:
            query_params = {}

        uri = self.client.base_url + "/private-apps"
        return self.client.post(uri, data, headers, query_params, content_type)
