# tests/test_integration_registry.py

import pytest
from integration.registry import IntegrationRegistry


class MockIntegration:
    name = "test_integration"


def test_register_integration():
    registry = IntegrationRegistry()
    registry.register(MockIntegration)
    assert "test_integration" in registry.get_all_integrations()
    assert registry.get_integration("test_integration").__class__ == MockIntegration


def test_register_integration_without_name():
    registry = IntegrationRegistry()

    class InvalidIntegration:
        pass

    with pytest.raises(AttributeError, match="must have a 'name' attribute"):
        registry.register(InvalidIntegration)


def test_register_duplicate_integration():
    registry = IntegrationRegistry()
    registry.register(MockIntegration)

    class DuplicateIntegration:
        name = "test_integration"

    with pytest.raises(ValueError, match="is already registered"):
        registry.register(DuplicateIntegration)


def test_get_non_existent_integration():
    registry = IntegrationRegistry()
    with pytest.raises(ValueError):
        registry.get_integration("non_existent")


def test_get_all_integrations():
    registry = IntegrationRegistry()

    class Integration1:
        name = "integration1"

    class Integration2:
        name = "integration2"

    registry.register(Integration1)
    registry.register(Integration2)

    all_integrations = registry.get_all_integrations()
    assert len(all_integrations) == 2
    assert "integration1" in all_integrations
    assert "integration2" in all_integrations
