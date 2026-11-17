"""VLAN configuration functions."""

from __future__ import annotations

from pyats_lab.device import IosXeRouter, _ensure_active, _mark_changed


def configure_vlan(router: IosXeRouter, vlan_id: int, name: str = "") -> None:
    """Configure (create) a VLAN with an ID and optional name on the router.

    Raises ValueError when the VLAN ID is outside the valid range 1-4094.
    """
    _ensure_active(router)
    if not 1 <= int(vlan_id) <= 4094:
        raise ValueError("VLAN ID must be between 1 and 4094")
    router.vlans[int(vlan_id)] = name or f"VLAN{int(vlan_id):04d}"
    _mark_changed(router)


def vlan_exists(router: IosXeRouter, vlan_id: int) -> bool:
    """Verify whether a VLAN exists on the router (show vlan brief)."""
    _ensure_active(router)
    return int(vlan_id) in router.vlans


def get_vlan_name(router: IosXeRouter, vlan_id: int) -> str | None:
    """Get the configured name of a VLAN on the router."""
    _ensure_active(router)
    return router.vlans.get(int(vlan_id))


def list_vlans(router: IosXeRouter) -> list[int]:
    """List all VLAN IDs configured on the router."""
    _ensure_active(router)
    return sorted(router.vlans)


def unconfigure_vlan(router: IosXeRouter, vlan_id: int) -> None:
    """Unconfigure (delete, no vlan) a VLAN from the router."""
    _ensure_active(router)
    router.vlans.pop(int(vlan_id), None)
    _mark_changed(router)
