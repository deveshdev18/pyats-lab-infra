"""Router health functions."""

from __future__ import annotations

from pyats_lab.device import IosXeRouter, _ensure_active


def get_cpu_utilization(router: IosXeRouter) -> float:
    """Get the five minute CPU utilization percent from show processes cpu."""
    _ensure_active(router)
    return router.cpu_percent


def get_free_memory_percent(router: IosXeRouter) -> float:
    """Get the free processor memory percent from show memory statistics."""
    _ensure_active(router)
    return router.free_memory_percent
