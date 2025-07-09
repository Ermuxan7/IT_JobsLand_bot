import hmac
import hashlib
import urllib.parse
from bot.config import BOT_TOKEN

def verify_init_data(init_data: str) -> dict | None:
    try:
        if not init_data:
            print("⚠️ init_data bos.")
            return None

        print("📦 Kelgen init_data:", init_data)

        parsed = urllib.parse.parse_qsl(init_data, strict_parsing=True)
        data_dict = dict(parsed)

        hash_from_telegram = data_dict.pop("hash", None)
        if not hash_from_telegram:
            print("❌ hash tabilmadi.")
            return None

        # ❗ signature ni hammasidan chiqaramiz
        data_dict.pop("signature", None)

        # 🔄 data_check_string yaratamiz
        sorted_data = sorted(data_dict.items())
        data_check_string = "\n".join([f"{k}={v}" for k, v in sorted_data])
        print("📄 HMAC uchun data_check_string:", repr(data_check_string))

        # 🔐 HMAC hisoblash
        secret_key = hashlib.sha256(BOT_TOKEN.encode()).digest()
        hmac_hash = hmac.new(secret_key, data_check_string.encode(), hashlib.sha256).hexdigest()
        print("🔑 HMAC esaplangan:", hmac_hash)
        print("🔐 Telegramdan hash:", hash_from_telegram)

        if hmac_hash != hash_from_telegram:
            print("❌ Hashlar mas emes!")
            return None

        print("✅ Hash duris!")
        return data_dict

    except Exception as e:
        print("❌ Exception:", e)
        return None


