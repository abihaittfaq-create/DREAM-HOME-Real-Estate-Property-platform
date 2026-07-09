# ==========================
# LEAD SCORING + INTENT RECOGNITION
# Single Cell - Google Colab
# ==========================

import json
import re
from google.colab import files

print("Upload inquiries.json (or inquiries (1).json)")
uploaded = files.upload()

filename = list(uploaded.keys())[0]

with open(filename, "r", encoding="utf-8") as f:
    data = json.load(f)

# ---------- Intent Recognition ----------
def detect_intent(text):
    text = text.lower()

    if any(word in text for word in ["buy", "purchase", "own"]):
        return "Buy Property"

    elif any(word in text for word in ["rent", "lease"]):
        return "Rent Property"

    elif any(word in text for word in ["visit", "schedule", "appointment"]):
        return "Schedule Visit"

    elif any(word in text for word in ["price", "cost", "budget"]):
        return "Price Inquiry"

    else:
        return "General Inquiry"


# ---------- Lead Scoring ----------
def lead_score(text):
    text = text.lower()

    score = 0

    if re.search(r"\d", text):
        score += 2

    if any(word in text for word in ["dha","bahria","gulberg","karachi","lahore","islamabad"]):
        score += 2

    if any(word in text for word in ["buy","purchase","visit","schedule"]):
        score += 3

    if any(word in text for word in ["urgent","today","asap","immediately"]):
        score += 2

    if score >= 6:
        return "High"

    elif score >= 3:
        return "Medium"

    else:
        return "Low"


# ---------- Read Inquiry Text ----------
def get_text(item):
    if isinstance(item, str):
        return item

    for key in ["query","message","text","inquiry","description"]:
        if key in item:
            return str(item[key])

    return str(item)


print("\n================ RESULTS ================\n")

if isinstance(data, list):

    for i, item in enumerate(data,1):

        query = get_text(item)

        print(f"Inquiry {i}")
        print("Query :", query)
        print("Intent :", detect_intent(query))
        print("Lead Score :", lead_score(query))
        print("-"*50)

else:

    query = get_text(data)

    print("Query :", query)
    print("Intent :", detect_intent(query))
    print("Lead Score :", lead_score(query))


# ---------- User Query ----------
print("\n================ USER INPUT ================\n")

user_query = input("Enter your own query: ")

print("\nResult")
print("Intent :", detect_intent(user_query))
print("Lead Score :", lead_score(user_query))
