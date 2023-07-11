import argparse
import os
import logging
import quickfix as fix
import sys

# Get the parent directory of the current script directory
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

try:
    # Ensure the logs directory exists
    os.makedirs(os.path.join(parent_dir, 'Logs'), exist_ok=True)

    # Define your log file path
    log_file = os.path.join(parent_dir, 'Logs', 'fix_socket.log')

    # Create a custom logger
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    # Create handlers
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.INFO)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # Create formatters and add it to handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
except Exception as e:
    print(f"Failed to configure logger: {str(e)}")
    sys.exit(1)


def start_fix_initiator(gateway):
    try:
        # Parse command line arguments
        parser = argparse.ArgumentParser(description='FIX Client')
        parser.add_argument('-c', '--configfile', default="clientLocal.cfg", help='file to read the config from')
        args = parser.parse_args()

        # Load session settings from configuration file
        settings = fix.SessionSettings(args.configfile)

        # Create store and log factories
        storeFactory = fix.FileStoreFactory(settings)
        logFactory = fix.FileLogFactory(settings)

        # Create and start the initiator
        initiator = fix.SocketInitiator(gateway, storeFactory, settings, logFactory)
        initiator.start()

        logger.info('FIX initiator started successfully')

        return initiator
    except Exception as e:
        logger.error(f'Failed to start FIX initiator: {str(e)}')
        sys.exit(1)


def stop_fix_initiator(initiator):
    if initiator is None:
        logger.error("No active FIX initiator to stop.")
        return

    try:
        initiator.stop()
    except fix.ConfigError as e:
        logger.error(f"Failed to stop FIX initiator: {str(e)}")
