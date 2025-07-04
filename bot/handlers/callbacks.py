from aiogram import types, Router
from web.db import database, vacancies
from web.utils.telegram import send_telegram_message
import uuid

router = Router()

@router.callback_query(lambda c: c.data.startswith('approve::'))
async def approve_callback(callback_query: types.CallbackQuery):
    message_id = uuid.UUID(callback_query.data.split("::", 1)[1])

    query = vacancies.select().where(vacancies.c.id == message_id)
    vacancy = await database.fetch_one(query)

    if not vacancy:
        await callback_query.answer("❌ Vakansiya tabilmadi")
        return
    
    print("Vacancy found:", vacancy)
    await send_telegram_message(vacancy['message'])
    await database.execute(
        vacancies.update()
        .where(vacancies.c.id == message_id)
        .values(status="approved")
    )

    await callback_query.message.edit_text("✅ Kanalga jiberildi")
    await callback_query.answer("✅ Kanalga jiberildi")

@router.callback_query(lambda c: c.data.startswith("reject::"))
async def reject_callback(callback_query: types.CallbackQuery):
    try:
        message_id = uuid.UUID(callback_query.data.split("::", 1)[1])

        # Ma'lumotni DB dan olib kelamiz
        query = vacancies.select().where(vacancies.c.id == message_id)
        vacancy = await database.fetch_one(query)

        print("Reject callback vacancy:", vacancy)
        if not vacancy:
            await callback_query.answer("❌ Vakansiya tabilmadi", show_alert=True)
            return

        # Statusni o‘zgartiramiz
        await database.execute(
            vacancies.update()
            .where(vacancies.c.id == message_id)
            .values(status="rejected")
        ) 


        await callback_query.message.edit_text("❌ Vakansiya rad etildi.")

        # Adminga alert
        await callback_query.answer("❌ Biykar etildi", show_alert=True)

    except Exception as e:
        print(f"Reject callback xatosi: {e}")
        await callback_query.answer("❌ Xatolik yuz berdi", show_alert=True)
