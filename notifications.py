"""
مكونات إرسال الإشعارات عبر الرسائل النصية باستخدام Twilio
"""
import os
import logging

from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException

# استيراد بيانات الاعتماد من متغيرات البيئة
TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.environ.get("TWILIO_PHONE_NUMBER")

# إعداد التسجيل
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def send_sms_notification(to_phone_number, message):
    """
    إرسال إشعار SMS باستخدام Twilio
    
    المعلمات:
        to_phone_number (str): رقم الهاتف المستقبل بالتنسيق الدولي (مثال: +212612345678)
        message (str): نص الرسالة المراد إرسالها
        
    العائد:
        dict: قاموس يحتوي على حالة الإرسال و sid الرسالة إذا نجحت
    """
    # التحقق من وجود بيانات الاعتماد
    if not all([TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_PHONE_NUMBER]):
        logger.error("بيانات اعتماد Twilio غير موجودة")
        return {
            "success": False,
            "error": "بيانات اعتماد Twilio غير موجودة. تأكد من تعيين المتغيرات البيئية المطلوبة."
        }
    
    # إنشاء عميل Twilio
    try:
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        
        # إرسال الرسالة
        twilio_message = client.messages.create(
            body=message,
            from_=TWILIO_PHONE_NUMBER,
            to=to_phone_number
        )
        
        logger.info(f"تم إرسال الرسالة بنجاح. SID: {twilio_message.sid}")
        return {
            "success": True,
            "message_sid": twilio_message.sid
        }
        
    except TwilioRestException as e:
        logger.error(f"خطأ في إرسال الرسالة: {str(e)}")
        return {
            "success": False,
            "error": str(e)
        }
    except Exception as e:
        logger.error(f"خطأ غير متوقع: {str(e)}")
        return {
            "success": False,
            "error": str(e)
        }