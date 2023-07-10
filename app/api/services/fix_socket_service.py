import argparse
import quickfix as fix


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

        return initiator
    except fix.ConfigError as e:
        print(e)


def stop_fix_initiator(initiator):
    try:
        # Stop the initiator
        initiator.stop()
    except fix.ConfigError as e:
        print(e)
