from unittest.mock import MagicMock, patch
from app.api.services.fix_socket_service import start_fix_initiator, stop_fix_initiator


def test_start_fix_initiator():
    # Mock the necessary objects and functions
    gateway = MagicMock()
    settings = MagicMock()
    storeFactory = MagicMock()
    logFactory = MagicMock()
    initiator = MagicMock()

    # Patch the necessary functions
    with patch("app.api.services.fix_socket_service.fix.SessionSettings") as mock_SessionSettings, \
            patch("app.api.services.fix_socket_service.fix.FileStoreFactory") as mock_FileStoreFactory, \
            patch("app.api.services.fix_socket_service.fix.FileLogFactory") as mock_FileLogFactory, \
            patch("app.api.services.fix_socket_service.fix.SocketInitiator") as mock_SocketInitiator:
        # Configure the mock objects and functions
        mock_SessionSettings.return_value = settings
        mock_FileStoreFactory.return_value = storeFactory
        mock_FileLogFactory.return_value = logFactory
        mock_SocketInitiator.return_value = initiator

        # Call the function under test
        result = start_fix_initiator(gateway, "configfile.cfg")

        # Assertions
        mock_SessionSettings.assert_called_once_with("configfile.cfg")
        mock_FileStoreFactory.assert_called_once_with(settings)
        mock_FileLogFactory.assert_called_once_with(settings)
        mock_SocketInitiator.assert_called_once_with(gateway, storeFactory, settings, logFactory)
        initiator.start.assert_called_once()
        assert result == initiator


def test_stop_fix_initiator():
    # Mock the initiator object
    initiator = MagicMock()

    # Call the function under test
    stop_fix_initiator(initiator)

    # Assertions
    initiator.stop.assert_called_once()
