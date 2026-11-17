"""Reachability functions."""

from __future__ import annotations

from pyats_lab.device import IosXeRouter, _ensure_active

MAIN_LINK = "GigabitEthernet1"


def execute_ping(router: IosXeRouter, address: str, count: int = 5) -> float:
    """Execute a ping to an IP address from the router and return the success rate percent.

    Success rate is 100.0 for a reachable address and 0.0 when the address is
    unknown or GigabitEthernet1 is shut.
    """
    _ensure_active(router)
    link_up = router.interfaces[MAIN_LINK]["status"] == "up"
    return 100.0 if link_up and address in router.reachable else 0.0
