"""Lightweight installed-provider metadata; model code is loaded on creation."""
from conceptmod.contracts import BackendCapabilities
from conceptmod.providers import BackendProvider

PROVIDER = BackendProvider(
    name="sana",
    factory="sana_conceptmod.backend:SanaBackend",
    distribution="sana-conceptmod",
    capabilities=BackendCapabilities(),
)
