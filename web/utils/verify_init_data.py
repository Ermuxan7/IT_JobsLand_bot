# web/utils/verify_init_data.py
import hmac, hashlib, urllib.parse
from bot.config import BOT_TOKEN

def verify_init_data(init_data: str) -> dict | None:
    try:
        parsed = urllib.parse.parse_qs(init_data, strict_parsing=True)

        hash_check = parsed.get('hash', [None])[0]
        if not hash_check:
            return None

        # Bu 'hash'dan tashqari barcha kalit-qiymatlarni tekshirish uchun kerak
        data_check_arr = []
        for key in sorted(parsed):
            if key != 'hash':
                value = parsed[key][0]
                data_check_arr.append(f"{key}={value}")
        data_check_string = '\n'.join(data_check_arr)

        # Telegram secret key bilan hesh
        secret_key = hashlib.sha256(BOT_TOKEN.encode()).digest()
        hmac_hash = hmac.new(secret_key, data_check_string.encode(), hashlib.sha256).hexdigest()

        if hmac_hash != hash_check:
            return None

        # Agar hesh to‘g‘ri bo‘lsa, user ma’lumotlarini qaytaramiz
        return {
            key: parsed[key][0]
            for key in parsed
            if key != 'hash'
        }
    
    except Exception as e:
        print("init_data verify xatosi:", e)
        return None