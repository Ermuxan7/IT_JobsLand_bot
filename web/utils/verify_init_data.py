import hmac
import hashlib
import urllib.parse
from bot.config import BOT_TOKEN

def verify_init_data(init_data: str) -> dict | None:
    import hmac, hashlib, urllib.parse
    from bot.config import BOT_TOKEN

    try:
        if not init_data:
            print("⚠️ init_data bo‘sh.")
            return None

        print("📦 Kelgen init_data:", init_data)

        # Telegram documentation: https://core.telegram.org/bots/webapps#validating-data-received-via-the-web-app

        parsed_data = urllib.parse.parse_qsl(init_data, strict_parsing=True)
        data_dict = dict(parsed_data)

        hash_from_telegram = data_dict.pop("hash", None)
        if not hash_from_telegram:
            print("❌ Hash topilmadi.")
            return None

        # 1. Keylarni tartiblash va '\n' bilan birlashtirish
        sorted_data = sorted((k, v) for k, v in data_dict.items())
        data_check_string = '\n'.join([f"{k}={v}" for k, v in sorted_data])

        print("📄 HMAC uchun data_check_string:", repr(data_check_string))

        # 2. Secret key: sha256(BOT_TOKEN)
        secret = hashlib.sha256(BOT_TOKEN.encode()).digest()

        # 3. HMAC
        computed_hash = hmac.new(secret, data_check_string.encode(), hashlib.sha256).hexdigest()
        print("🔑 HMAC hisoblangan:", computed_hash)
        print("🔐 Telegramdan hash:", hash_from_telegram)

        if computed_hash != hash_from_telegram:
            print("❌ Hashlar mos emas!")
            return None

        print("✅ Hash tekshiruvdan o‘tdi.")
        return data_dict

    except Exception as e:
        print("❌ Exception:", e)
        return None

