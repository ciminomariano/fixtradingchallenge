import argparse
import quickfix as fix

from api.gateway.broker_gateway import BrokerGatewayApplication


def start_socket(order):
    try:
        parser = argparse.ArgumentParser(description='FIX Client')
        parser.add_argument('-c', '--configfile', default="clientLocal.cfg", help='file to read the config from')
        args = parser.parse_args()
        settings = fix.SessionSettings(args.configfile)
        application = BrokerGatewayApplication()
        storeFactory = fix.FileStoreFactory(settings)
        logFactory = fix.FileLogFactory(settings)
        initiator = fix.SocketInitiator(application, storeFactory, settings, logFactory)
        initiator.start()
        response = application.put_new_order(order)
        initiator.stop()
        return response
    except fix.ConfigError as e:
        print(e)
