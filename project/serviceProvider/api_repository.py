# NOTE:
# To simplify the project API list considered as a static json.
# In real world it will replace with a database catch and a service to get updates from subsystems

apis = {
    "sales": {
        "base_url": "http://sales.sub:5010",
        "routes": {
            "products": {
                "custom_url": "",
                "methods": ["GET", "POST"]
            },
            "add_product": {
                "custom_url": "",
                "methods": ["POST"]
            }
        }
    },
    "accounting": {
        "base_url": "http://accounting.sub:5020",
        "routes": {
            "account_info": {
                "custom_url": "",
                "methods": ["GET"]
            },
            "add_amount": {
                "custom_url": "",
                "methods": ["POST"]
            }
        }
    },
    "warehouse": {
        "base_url": "http://warehouse.sub:5030",
        "routes": {
            "get_status": {
                "custom_url": "",
                "methods": ["GET"]
            },
            "save_log": {
                "custom_url": "",
                "methods": ["POST"]
            }
        }
    }
}


class ApiRepository:
    @staticmethod
    def validate_service(group, service_name, method):
        print((group, service_name, method))
        try:
            if group in apis \
                    and service_name in apis[group]['routes'].keys() \
                    and method in apis[group]['routes'][service_name]['methods']:
                return True
            else:
                return False
        except KeyError as e:
            return False

    @staticmethod
    def get_group(group):
        return apis[group] if group in apis.keys() else []

    @staticmethod
    def get_base_url(group):
        return apis[group]['base_url'] if group in apis.keys() else []

    @staticmethod
    def get_methods(group, service_name):
        return apis[group][service_name]['method'] \
            if group in apis.keys() and service_name in apis[group]['routes'].keys() \
            else None

    @staticmethod
    def get_custom_url(group, service_name):
        return apis[group]['routes'][service_name]['custom_url'] \
            if group in apis.keys() and service_name in apis[group]['routes'].keys() \
            else None

    @staticmethod
    def get_url(group, service_name):
        custom_url = ApiRepository.get_custom_url(group, service_name)
        base_url = ApiRepository.get_base_url(group)
        return '{}/{}'.format(base_url, service_name) if custom_url == "" else custom_url
