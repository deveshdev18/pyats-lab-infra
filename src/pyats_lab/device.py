"""Router session and system settings."""

from __future__ import annotations

import json
import logging
import os
from pathlib import Path

LOG = logging.getLogger("pyats_lab")


class IosXeRouter:
    """State of one simulated Cisco IOS-XE router."""

    def __init__(self, name: str, host: str = "simulated"):
        self.name = name
        self.host = host
        self.hostname = name
        self.version = "17.9.4"
        self.connected = False
        self.config_saved = True
        self.vlans: dict[int, str] = {1: "default"}
        self.interfaces: dict[str, dict] = {
            port: {"status": "up", "description": "", "input_errors": 0}
            for port in ("GigabitEthernet1", "GigabitEthernet2", "GigabitEthernet3")
        }
        self.ospf_neighbors: dict[str, str] = {"2.2.2.2": "FULL", "3.3.3.3": "FULL"}
        self.reachable = {"2.2.2.2", "3.3.3.3", "10.0.12.2"}
        self.cpu_percent = 12.0
        self.free_memory_percent = 61.0


def _ensure_active(router: IosXeRouter) -> None:
    if not router.connected:
        raise RuntimeError(f"Session to {router.name} is closed")


def _open_session(router: IosXeRouter) -> None:
    router.connected = True


def _close_session(router: IosXeRouter) -> None:
    router.connected = False


def _mark_changed(router: IosXeRouter) -> None:
    router.config_saved = False


def _persist(router: IosXeRouter) -> None:
    router.config_saved = True


def connect_device(name: str) -> IosXeRouter:
    """Connect to a router from the testbed by name and return the open session.

    Uses the optional SUT file in AUTOMATEYE_SUT_FILE for the host address;
    without it a simulated router is used, so no lab is required.
    """
    host = "simulated"
    sut_file = os.environ.get("AUTOMATEYE_SUT_FILE")
    if sut_file and Path(sut_file).is_file():
        try:
            entry = json.loads(Path(sut_file).read_text(encoding="utf-8")).get("devices", {}).get(name, {})
            host = entry.get("host", host)
        except ValueError:
            LOG.warning("SUT file is not JSON; using simulated defaults")
    router = IosXeRouter(name, host=host)
    _open_session(router)
    LOG.info("Connected to %s (%s)", name, host)
    return router


def disconnect_device(router: IosXeRouter) -> None:
    """Disconnect from the router and close the session."""
    _close_session(router)
    LOG.info("Disconnected from %s", router.name)


def is_device_connected(router: IosXeRouter) -> bool:
    """Check whether the router session is connected (open)."""
    return router.connected


def get_software_version(router: IosXeRouter) -> str:
    """Get the IOS-XE software version from show version output."""
    _ensure_active(router)
    return router.version


def get_hostname(router: IosXeRouter) -> str:
    """Get the configured hostname of the router."""
    _ensure_active(router)
    return router.hostname


def configure_hostname(router: IosXeRouter, hostname: str) -> None:
    """Configure (set) the hostname of the router."""
    _ensure_active(router)
    if not hostname or " " in hostname:
        raise ValueError("Hostname must be a single non-empty word")
    router.hostname = hostname
    _mark_changed(router)


def save_running_config(router: IosXeRouter) -> None:
    """Save the running config to the startup config (write memory)."""
    _ensure_active(router)
    _persist(router)
    LOG.info("Running config saved on %s", router.name)


def is_running_config_saved(router: IosXeRouter) -> bool:
    """Check whether the running config is saved to the startup config."""
    _ensure_active(router)
    return router.config_saved
