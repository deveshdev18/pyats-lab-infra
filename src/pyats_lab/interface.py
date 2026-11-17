"""Interface administration and status functions."""

from __future__ import annotations

from pyats_lab.device import IosXeRouter, _ensure_active, _mark_changed


def _port(router: IosXeRouter, interface: str) -> dict:
    _ensure_active(router)
    if interface not in router.interfaces:
        raise KeyError(f"Unknown interface {interface}")
    return router.interfaces[interface]


def shut_interface(router: IosXeRouter, interface: str) -> None:
    """Shut (shutdown, disable) an interface on the router."""
    _port(router, interface)["status"] = "administratively down"
    _mark_changed(router)


def unshut_interface(router: IosXeRouter, interface: str) -> None:
    """Unshut (no shutdown, enable) an interface on the router."""
    _port(router, interface)["status"] = "up"
    _mark_changed(router)


def get_interface_status(router: IosXeRouter, interface: str) -> str:
    """Get the interface status (up or down) of an interface."""
    return _port(router, interface)["status"]


def configure_interface_description(router: IosXeRouter, interface: str, description: str) -> None:
    """Configure (set) the description text of an interface on the router."""
    _port(router, interface)["description"] = description
    _mark_changed(router)


def get_interface_description(router: IosXeRouter, interface: str) -> str:
    """Get the description text of an interface on the router."""
    return _port(router, interface)["description"]


def get_interface_input_errors(router: IosXeRouter, interface: str) -> int:
    """Get the input errors counter of an interface from show interfaces."""
    return _port(router, interface)["input_errors"]
