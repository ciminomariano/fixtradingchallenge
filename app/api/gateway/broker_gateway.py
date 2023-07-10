import quickfix as fix

from api.models.order import OrderRequest

ECHO_DEBUG = True
sessionID = 0


class BrokerGatewayApplication(fix.Application):
    orderID = 0
    execID = 0
    global sessionID

    def gen_ord_id(self):
        global orderID
        orderID += 1
        return orderID

    def onCreate(self, sessionID):
        return

    def onLogon(self, sessionIDIn):

        mktcodes = ["GBPUSD", "EURUSD", "CCCCCC"]

        reqID = 1
        for mkt in mktcodes:
            message = fix.Message()
            header = message.getHeader();
            header.setField(fix.MsgType("R"))  # 35
            message.setField(644, "99999999")  # ReqId
            message.setField(146, "1")  # ReqId # 644
            message.setField(55, "GBPUSD")  # 55=SMBL
            message.setField(263, "1")  # SubscriptionRequestType
            message.setField(262, "12356")  # Request Type
            message.setField(264, "1")  # Market Depth
            fix.Session.sendToTarget(message, self.sessionID)
        return

    def onLogout(self, sessionID):
        return

    def toAdmin(self, message, sessionID):
        self.sessionID = sessionID
        print(" toAdmin " + str(message))
        if (message.getHeader().getField(fix.MsgType().getField()) == "A"):
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
        return

    def genOrderID(self):
        self.orderID = self.orderID + 1
        return self.orderID

    def genExecID(self):
        self.execID = self.execID + 1
        return self.execID

    def put_new_order(self, order: OrderRequest):
        try:
            message = fix.Message()
            header = message.getHeader()
            header.setField(fix.MsgType("D"))  # Use "D" message type (New Order - Single)
            message.setField(fix.Symbol(order.symbol))  # Symbol of the stock, e.g., "TSLA"
            message.setField(fix.Side(fix.Side_BUY))  # Side of the order: Buy
            message.setField(fix.OrderQty(order.quantity))  # Order quantity
            message.setField(fix.OrdType(fix.OrdType_MARKET))  # Order type: Market Order
            # Add other relevant fields as per your needs

            response = fix.Session.sendToTarget(message, self.sessionID)

            # Check if the order was successfully sent
            if response:
                return {
                    "success": True,
                    "message": "Order created successfully",
                }
            else:
                return {
                    "success": False,
                    "message": "Failed to create order",
                }

        except Exception as e:
            return {
                "success": False,
                "error_message": str(e),
            }




