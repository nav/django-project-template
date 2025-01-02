class IntegrationRegistry:
    def __init__(self):
        self._registry = {}

    def register(self, integration_class):
        if not hasattr(integration_class, "name"):
            raise AttributeError(
                f"Integration class {integration_class.__name__} must have a 'name' attribute"
            )

        name = integration_class.name
        if name in self._registry:
            raise ValueError(f"Integration {name} is already registered")
        self._registry[name] = integration_class

    def get_integration(self, name):
        if name not in self._registry:
            raise ValueError(f"Integration {name} does not exist.")
        return self._registry.get(name)()

    def get_all_integrations(self):
        return self._registry


integration_registry = IntegrationRegistry()


def register_integration(cls):
    integration_registry.register(cls)
    return cls
