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

    message = (
        f"   📢 *Vakansiya!*\n"
        f"🏢 Kompaniya: {vacancy['company']}\n"
        f"💼 Lawazim: {vacancy['job_title']}\n"
        f"📍 Manzil: {vacancy['address']}\n"
        f"⏱ Jumis waqti: {vacancy['working_time']}\n"
        f"📋 Talaplar: {vacancy['requirements']}\n"
        f"💰 Ayliq: {vacancy['salary']}\n"
        f"📞 Baylanisiw: {vacancy['contacts']}\n"
        f"📝 Qosimsha: {vacancy['additional']}\n"
    )

    await send_telegram_message(message)
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

        # Magliwmatti DB dan alip kelemiz
        query = vacancies.select().where(vacancies.c.id == message_id)
        vacancy = await database.fetch_one(query)

        print("Reject callback vacancy:", vacancy)
        if not vacancy:
            await callback_query.answer("❌ Vakansiya tabilmadi")
            return

        # Statusdi o‘zgertemiz
        await database.execute(
            vacancies.update()
            .where(vacancies.c.id == message_id)
            .values(status="rejected")
        ) 

        await callback_query.message.edit_text("❌ Vakansiya biykar qilindi.")

        # Adminga alert
        await callback_query.answer("❌ Biykar etildi")

    except Exception as e:
        print(f"Reject callback xatosi: {e}")
        await callback_query.answer("❌ Qatelik boldi", show_alert=True)
