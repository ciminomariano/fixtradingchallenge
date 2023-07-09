import argparse
import uuid

import quickfix as fix
import quickfix44 as fix44

from api.models.order import OrderRequest


class BrokerGatewayApplication(fix.Application):
    def onCreate(self, sessionID):
        pass

    def onLogon(self, sessionID):
        pass

    def onLogout(self, sessionID):
        pass

    def toAdmin(self, message, sessionID):
        pass

    def fromAdmin(self, sessionID, message):
        pass

    def toApp(self, sessionID, message):
        pass

    def fromApp(self, message, sessionID):
        pass

    def request_quote(self, order: OrderRequest):
        req_id = str(uuid.uuid4())
        message = fix44.MarketDataRequest()
        message.setField(fix.Symbol(order.symbol))
        message.setField(fix.MDReqID(req_id))
        message.setField(fix.OrderQty(order.quantity))

        try:
            response = fix.Session.sendToTarget(message, self.sessionID)
            return response
        except Exception as e:
            return str(e)


def main():
    try:
        settings = fix.SessionSettings("../core/gateway.cfg")

        application = BrokerGatewayApplication()
        storeFactory = fix.FileStoreFactory(settings)
        logFactory = fix.FileLogFactory(settings)
        initiator = fix.SocketInitiator(application, storeFactory, settings, logFactory)

        initiator.start()

        while True:
            input1 = input("Input\n")
            if input1 == 'q':
                print("Request Quote")
                application.request_quote()
            elif input1 == '2':
                break
            elif input1 == 'd':
                import pdb
                pdb.set_trace()
            else:
                print("Valid input is 'q' for quote, '2' for exit, 'd' for debugging")

        initiator.stop()
    except fix.ConfigError as e:
        print(e)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='FIX Client')
    parser.add_argument('-c', '--configfile', default="clientLocal.cfg", help='file to read the config from')
    args = parser.parse_args()
    main(args.configfile)
