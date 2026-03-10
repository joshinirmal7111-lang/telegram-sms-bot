import os
import random
import time
import xml.etree.ElementTree as ET
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.environ.get("TOKEN")

banks = ["SBI", "HDFC Bank", "ICICI Bank", "Axis Bank", "Kotak Bank"]
bank_ids = ["VK-SBIATM", "AX-HDFCBK", "VM-ICICIB", "JD-KOTAKB", "BZ-AXISBK"]

shop_ids = ["JD-AMAZON", "VM-FLIPKR", "BZ-SWIGGY", "AD-ZOMATO", "VK-MYNTRA"]

otp_ids = ["AD-OTPMSG", "VK-VERIFY", "JD-SECURE"]
shops = ["Amazon", "Flipkart", "Myntra", "Ajio", "Swiggy", "Zomato"]
people = ["Rahul", "Amit", "Neha", "Priya", "Arjun", "Riya", "Karan"]

chat_msgs = [
    "Hey where are you?",
    "Call me when free.",
    "Let's meet tomorrow.",
    "Send me the address.",
    "Did you finish the work?"
]

spam_msgs = [
    "Congratulations! You won ₹5000 voucher.",
    "Get instant loan approval today.",
    "Exclusive shopping offer for you."
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "SMS Generator Bot Ready\n\nUse:\n/generate 15000"
    )

async def generate(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if len(context.args) == 0:
        await update.message.reply_text("Example: /generate 15000")
        return

    count = int(context.args[0])

    await update.message.reply_text(f"Generating {count} SMS...")

    root = ET.Element("smses")
    root.set("count", str(count))

    now = int(time.time())

    # 14 months range
    fourteen_months = 14 * 30 * 24 * 60 * 60

    for i in range(count):

        sms = ET.SubElement(root, "sms")

        amount = random.randint(10,10000)

        all_senders = bank_ids + shop_ids + otp_ids

number = random.choice(
    all_senders + [
        random.choice(["98","97","96","95","94","93","92","91","90"]) + "".join(str(random.randint(0,9)) for _ in range(8))
    ]
)
        timestamp = (now - random.randint(0, fourteen_months)) * 1000

        sms_type = random.choice([
            "credit","debit","upi","shopping",
            "recharge","otp","delivery","chat","spam"
        ])

        if sms_type == "credit":
            body = f"Rs.{amount} credited to your {random.choice(banks)} account."

        elif sms_type == "debit":
            body = f"Rs.{amount} debited from your {random.choice(banks)} account."

        elif sms_type == "upi":
            body = f"You paid Rs.{amount} to {random.choice(people)} via UPI."

        elif sms_type == "shopping":
            body = f"Payment of Rs.{amount} successful at {random.choice(shops)}."

        elif sms_type == "recharge":
            body = f"Recharge of Rs.{amount} successful."

        elif sms_type == "otp":
            otp = random.randint(100000,999999)
            body = f"Your OTP is {otp}. Do not share it."

        elif sms_type == "delivery":
            body = f"Your order from {random.choice(shops)} is out for delivery."

        elif sms_type == "chat":
            body = random.choice(chat_msgs)

        else:
            body = random.choice(spam_msgs)

        sms.set("protocol","0")
        sms.set("address",number)
        sms.set("date",str(timestamp))
        sms.set("type","1")
        sms.set("body",body)

    filename = f"sms_backup_{int(time.time())}.xml"

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)

    await update.message.reply_document(document=open(filename, "rb"))

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("generate", generate))

app.run_polling()
