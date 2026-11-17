"""OSPF routing functions."""

from __future__ import annotations

from pyats_lab.device import IosXeRouter, _ensure_active


def get_ospf_neighbor_state(router: IosXeRouter, neighbor_id: str) -> str | None:
    """Get the OSPF neighbor state (for example FULL) from show ip ospf neighbor."""
    _ensure_active(router)
    return router.ospf_neighbors.get(neighbor_id)


def list_ospf_neighbors(router: IosXeRouter) -> list[str]:
    """List the OSPF neighbor router IDs from show ip ospf neighbor."""
    _ensure_active(router)
    return sorted(router.ospf_neighbors)
