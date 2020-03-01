from models.alert import Alert


# _alert = Alert('8f976b58058d42c3a87273b210f39ff3', 500)

# _alert.saveToDb()

alerts = Alert.all()

for alert in alerts:
    alert.load_item_price()
    alert.notify_if_price_reached()

# 問題？ 為何不要 price 做在 item 裡面就好

if not alerts:
    print("no alerts")