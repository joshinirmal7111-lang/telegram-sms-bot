import random
import time
import xml.etree.ElementTree as ET

count = 25000

root = ET.Element("smses")
root.set("count", str(count))

now = int(time.time())
one_year = 365 * 24 * 60 * 60

banks = ["SBI", "HDFC Bank", "ICICI Bank", "Axis Bank", "Kotak Bank"]
shops = ["Amazon", "Flipkart", "Myntra", "Ajio", "Swiggy", "Zomato"]
people = ["Rahul", "Amit", "Neha", "Priya", "Arjun", "Riya", "Karan"]

chat_msgs = [
    "Hey where are you?",
    "Call me when you reach.",
    "I'm outside your house.",
    "Let's meet tomorrow.",
    "Send me the address.",
    "Did you finish the work?"
]

spam_msgs = [
    "Congratulations! You won ₹5000 voucher. Claim now.",
    "Get instant personal loan approval today.",
    "Exclusive offer just for you! Shop now.",
    "Limited time deal. Click link to claim."
]

for i in range(count):

    sms = ET.SubElement(root, "sms")

    amount = random.randint(10,10000)

    number = random.choice(["98","97","96","95","94","93","92","91","90"]) + "".join(str(random.randint(0,9)) for _ in range(8))

    timestamp = (now - random.randint(0, one_year)) * 1000

    sms_type = random.choice([
        "credit","debit","upi","shopping",
        "recharge","otp","delivery","chat","spam"
    ])

    if sms_type == "credit":
        body = f"Rs.{amount} credited to your {random.choice(banks)} account. Avl bal updated."

    elif sms_type == "debit":
        body = f"Rs.{amount} debited from your {random.choice(banks)} account via card txn."

    elif sms_type == "upi":
        body = f"You paid Rs.{amount} to {random.choice(people)} via UPI. Ref No {random.randint(1000000000,9999999999)}."

    elif sms_type == "shopping":
        body = f"Payment of Rs.{amount} successful at {random.choice(shops)}. Thank you for shopping."

    elif sms_type == "recharge":
        body = f"Recharge of Rs.{amount} successful. Validity 28 days. Enjoy unlimited calls."

    elif sms_type == "otp":
        otp = random.randint(100000,999999)
        body = f"Your OTP is {otp}. Do not share this OTP with anyone."

    elif sms_type == "delivery":
        body = f"Your order from {random.choice(shops)} is out for delivery and will arrive today."

    elif sms_type == "chat":
        body = random.choice(chat_msgs)

    else:
        body = random.choice(spam_msgs)

    sms.set("protocol","0")
    sms.set("address",number)
    sms.set("date",str(timestamp))
    sms.set("type","1")
    sms.set("subject","null")
    sms.set("body",body)
    sms.set("toa","null")
    sms.set("sc_toa","null")
    sms.set("service_center","null")
    sms.set("read","1")
    sms.set("status","-1")
    sms.set("locked","0")

tree = ET.ElementTree(root)

filename = f"sms_backup_{int(time.time())}.xml"

tree.write(filename,encoding="utf-8",xml_declaration=True)

print("SMS file generated:", filename)
