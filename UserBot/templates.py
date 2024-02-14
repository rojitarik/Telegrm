# Description: This file contains all the templates used in the bot.
from config import LANG
from UserBot.content import MESSAGES
from Utils.utils import rial_to_toman, toman_to_rial,all_configs_settings
from Database.dbManager import USERS_DB
# User Subscription Info Template
def user_info_template(sub_id, server, usr, header=""):
    settings = USERS_DB.find_bool_config(key='visible_hiddify_hyperlink')
    if settings:
        settings = settings[0]
        if settings['value']:
            user_name = f"<a href='{usr['link']}'> {usr['name']} </a>"
        else:
            user_name = usr['name']
    else:
        user_name = usr['name']
    # if usr['enable'] == 1:
    #     status = MESSAGES['ACTIVE_SUBSCRIPTION_STATUS']
    # else:
    #     status = MESSAGES['DEACTIVE_SUBSCRIPTION_STATUS']
    return f"""
{header}

{MESSAGES['USER_NAME']} {user_name}
{MESSAGES['SERVER']} {server['title']}
{MESSAGES['INFO_USAGE']} {usr['usage']['current_usage_GB']} {MESSAGES['OF']} {usr['usage']['usage_limit_GB']} {MESSAGES['GB']}
{MESSAGES['INFO_REMAINING_DAYS']} {usr['remaining_day']} {MESSAGES['DAY_EXPIRE']}
{MESSAGES['INFO_ID']} <code>{sub_id}</code>
"""
# {MESSAGES['SUBSCRIPTION_STATUS']} {status}

# Wallet Info Template
def wallet_info_template(balance):
    if balance == 0:
        return MESSAGES['ZERO_BALANCE']
    else:
        return f"""
         {MESSAGES['WALLET_INFO_PART_1']} {rial_to_toman(balance)} {MESSAGES['WALLET_INFO_PART_2']}
         """


# Plan Info Template
def plan_info_template(plan, header=""):
    msg = f"""
{header}
{MESSAGES['PLAN_INFO']}

{MESSAGES['PLAN_INFO_SIZE']} {plan['size_gb']} {MESSAGES['GB']}
{MESSAGES['PLAN_INFO_DAYS']} {plan['days']} {MESSAGES['DAY_EXPIRE']}
{MESSAGES['PLAN_INFO_PRICE']} {rial_to_toman(plan['price'])} {MESSAGES['TOMAN']}
"""
    if plan['description']:
        msg += f"""{MESSAGES['PLAN_INFO_DESC']} {plan['description']}"""
    return msg
    

# Owner Info Template (For Payment)
def owner_info_template(card_number, card_holder_name, price, header=""):
    card_number = card_number if card_number else "-"
    card_holder_name = card_holder_name if card_holder_name else "-"

    if LANG == 'FA':
        return f"""
{header}

💰تکایە بڕی: <code>{price}</code> {MESSAGES['RIAL']}
💴کە ئەبێتە: {rial_to_toman(price)} {MESSAGES['TOMAN']}
💳بۆ ژمارە کارتی: <code>{card_number}</code>
👤بە ناوی <b>{card_holder_name}</b> بنێرن.

❗️دواتر وێنەی پارە ناردنەکە بنێرە.
"""
    elif LANG == 'EN':
        return f"""
{header}

💰Please pay exactly: <code>{price}</code> {MESSAGES['TOMAN']}
💳To card number: <code>{card_number}</code>
Card owner <b>{card_holder_name}</b>

❗️After paying the amount, send us a screenshot of the transaction.
"""


# Payment Received Template - Send to Admin
def payment_received_template(payment,user, header="", footer=""):
    username = f"@{user['username']}" if user['username'] else MESSAGES['NOT_SET']
    name = user['full_name'] if user['full_name'] else user['telegram_id']


    if LANG == 'FA':
        return f"""
{header}

پێناسەی ناردن: <code>{payment['id']}</code>
بڕی ناردن: <b>{rial_to_toman(payment['payment_amount'])}</b> {MESSAGES['TOMAN']}
{MESSAGES['INFO_USER_NAME']} <b>{name}</b>
{MESSAGES['INFO_USER_USERNAME']} {username}
{MESSAGES['INFO_USER_NUM_ID']} {user['telegram_id']}
---------------------
⬇️ شارژکردنەوەی باڵانسەکەت ⬇️

{footer}
"""
    elif LANG == 'EN':
        return f"""
{header}

Payment number: <b>{payment['id']}</b>
Paid amount: <b>{payment['payment_amount']}</b> {MESSAGES['TOMAN']}
{MESSAGES['INFO_USER_NAME']} <b>{name}</b>
{MESSAGES['INFO_USER_USERNAME']} {username}
{MESSAGES['INFO_USER_NUM_ID']} {user['telegram_id']}
---------------------
⬇️Request to increase wallet balance⬇️

"""


# Help Guide Template
def connection_help_template(header=""):
    if LANG == 'FA':
        return f"""
{header}

⭕️ ئەو بەرنامانەی کە پێویستن بۆ وەسڵ بوون
    
📥 ئەندرۆید:
<a href='https://play.google.com/store/apps/details?id=com.v2ray.ang'>V2RayNG</a>
<a href='https://play.google.com/store/apps/details?id=ang.hiddify.com'>HiddifyNG</a>

📥 ئایفۆن:
<a href='https://apps.apple.com/us/app/streisand/id6450534064'>Streisand</a>
<a href='https://apps.apple.com/us/app/foxray/id6448898396'>Foxray</a>
<a href='https://apps.apple.com/us/app/v2box-v2ray-client/id6446814690'>V2box</a>

📥 ویندۆوز:
<a href='https://github.com/MatsuriDayo/nekoray/releases'>Nekoray</a>
<a href='https://github.com/2dust/v2rayN/releases'>V2rayN</a>
<a href='https://github.com/hiddify/HiddifyN/releases'>HiddifyN</a>

📥 مەک و لینوکس:
<a href='https://github.com/MatsuriDayo/nekoray/releases'>Nekoray</a>
"""

    elif LANG == 'EN':
        return f"""
{header}

⭕️Required software for connecting to config

📥Android:
<a href='https://play.google.com/store/apps/details?id=com.v2ray.ang'>V2RayNG</a>
<a href='https://play.google.com/store/apps/details?id=ang.hiddify.com'>HiddifyNG</a>

📥iOS:
<a href='https://apps.apple.com/us/app/streisand/id6450534064'>Streisand</a>
<a href='https://apps.apple.com/us/app/foxray/id6448898396'>Foxray</a>
<a href='https://apps.apple.com/us/app/v2box-v2ray-client/id6446814690'>V2box</a>

📥Windows:
<a href='https://github.com/MatsuriDayo/nekoray/releases'>Nekoray</a>
<a href='https://github.com/2dust/v2rayN/releases'>V2rayN</a>
<a href='https://github.com/hiddify/HiddifyN/releases'>HiddifyN</a>

📥Mac and Linux:
<a href='https://github.com/MatsuriDayo/nekoray/releases'>Nekoray</a>
"""


# Support Info Template
# def support_template(owner_info, header=""):
#     username = None
#     owner_info = all_configs_settings()
#     if owner_info:
#         username = owner_info['support_username'] if owner_info['support_username'] else "-"
#     else:
#         username = "-"

#     if LANG == 'FA':
#         return f"""
# {header}

# 📞 بەڕێوەبەر: {username}
# """

#     elif LANG == 'EN':
#         return f"""
# {header}

# 📞Supporter: {username}
# """


# Alert Package Days Template
def package_days_expire_soon_template(sub_id, remaining_days):
    if LANG == 'FA':
        return f"""
تەنیا {remaining_days} ڕۆژ ماوە بۆ کۆتایی هەژمارەکەت.
ئەگەر حەزت لێبوو ماوەی هەژمارەکەت درێژ بکەوە.
پێناسەی هەژمارەکەت : <code>{sub_id}</code>
"""
    elif LANG == 'EN':
        return f"""
Only {remaining_days} days left until your package expires.
Please purchase a new package.
Your package ID: <code>{sub_id}</code>
"""


# Alert Package Size Template
def package_size_end_soon_template(sub_id, remaining_size):
    if LANG == 'FA':
        return f"""
تەنیا {remaining_size} گیگابایت ماوە بۆ کۆتایی هاتنی قەبارەی هەژمارەکەت.
قەبارەی هەژمارەکەت زیا بکە.

پێناسەی هەژمارەکەت : <code>{sub_id}</code>
"""
    elif LANG == 'EN':
        return f"""
Only {remaining_size} GB left until your package expires.
Please renewal package.
Your package ID: <code>{sub_id}</code>
"""

def renewal_unvalable_template(settings):
    if LANG == 'FA':
        return f"""
🛑 لە ئێستایا ناتوانی هەژمارەکەت نوێ بکەیتەوە.
چونکە ئەبێ:
1- کەمتر لە {settings['advanced_renewal_days']} ڕۆژت مابێ بۆ کۆتایی هاتنی ماوەی هەژمارەکەت .
2- قەبارەی بەکارنەهاتووی هەژمارەکەت کەمتر لە{settings['advanced_renewal_usage']} گیگابایت بێت.
"""
    elif LANG == 'EN':
        return f"""
🛑You cannot renew your subscription at this time.
To renew your subscription, one of the following conditions must be met:
1- Less than {settings['advanced_renewal_days']} days left until your subscription expires.
2- The remaining volume of your subscription is less than {settings['advanced_renewal_usage']} GB.
"""
