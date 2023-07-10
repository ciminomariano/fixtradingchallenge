import sys
import argparse
import uuid
from datetime import datetime

import quickfix as fix
import quickfix44 as fix44

from api.models.order import OrderRequest

ECHO_DEBUG= True
sessionID = 0


class BrokerGatewayApplication(fix.Application):
        orderID = 0
        execID = 0
        global sessionID

        def gen_ord_id(self):
            global orderID
            orderID+=1
            return orderID


        def onCreate(self, sessionID):
            return

        def onLogon(self, sessionIDIn):


            mktcodes = ["GBPUSD", "EURUSD", "CCCCCC"]

            reqID = 1
            for mkt in mktcodes:

                message = fix.Message()
                header = message.getHeader();
                header.setField(fix.MsgType("R")) #35
                message.setField(644, "99999999")  # ReqId
                message.setField(146, "1")  # ReqId # 644
                message.setField(55, "GBPUSD")  # 55=SMBL
                message.setField(263, "1")  # SubscriptionRequestType
                message.setField(262, "12356") #Request Type
                message.setField(264, "1")  # Market Depth
                fix.Session.sendToTarget(message, self.sessionID)
            return

        def onLogout(self, sessionID):
            return

        def toAdmin(self, message, sessionID):
            self.sessionID = sessionID
            print(" toAdmin " + str(message))
            if(message.getHeader().getField(fix.MsgType().getField()) == "A"):
                print(" login Message " + str(sessionID))
                message.setField(fix.Username("chris"))
                message.setField(fix.Password("tradermade"))
            return

        def fromAdmin(self, sessionID, message):
            print("fromAdmin: %s" % message.toString())

            return

        def toApp(self, sessionID, message):
            print("ToApp: %s" % message.toString())
            return

        def fromApp(self, message, sessionID):
            print(" FromApp: %s " + str(message))
            symbol = message.getField(fix.Symbol().getField())
            print(symbol)
            # bid = message.getField(fix.BidPx().getField())
            # ask = message.getField(fix.OfferPx().getField())
            #
            # print(symbol + " " + bid + " " + ask )
            return


        def genOrderID(self):
            self.orderID = self.orderID+1
            return self.orderID


        def genExecID(self):
            self.execID = self.execID+1
            return self.execID

        def request_quote(self, order: OrderRequest):

            try:

                message = fix.Message()
                header = message.getHeader();
                header.setField(fix.MsgType("R"))
                message.setField(55, 'CCCCCC')  # 55=SMBL ?
                id = self.gen_ord_id()
                fix.Session.sendToTarget(message, id)

            except Exception as e:
                return str(e)

        def put_new_order(self, order: OrderRequest):
            try:
                message = fix.Message()
                header = message.getHeader();
                header.setField(fix.MsgType("R"))
                message.setField(55, 'CCCCCC')  # 55=SMBL ?
                response = fix.Session.sendToTarget(message, self.sessionID)
                return response


            except Exception as e:
                return str(e)
