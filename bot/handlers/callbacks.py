from aiogram import types, Router
from sqlalchemy import select
from web.db import database, vacancies, resumes, projects
from web.utils.telegram import send_telegram_message
import uuid

router = Router()

table_map = {
    "vacancy": vacancies,
    "resume": resumes,
    "project": projects
}

#2
@router.callback_query(lambda c: c.data.startswith(('approve_', 'reject_')))
async def handle_callback(callback_query: types.CallbackQuery):
    try:
        action, form_type, msg_id = callback_query.data.split("_", 2)
        item_id = uuid.UUID(msg_id)

        table = table_map.get(form_type)
        # Magliwmat turin tekseremiz
        if table is None:
            await callback_query.answer("❌ Qatelik boldi")
            return
        
        # Magliwmatti DB dan alip kelemiz
        item = await database.fetch_one(select(table).where(table.c.id == item_id))
        if not item:
            await callback_query.answer("❌ Magliwmat tabilmadi")
            return

        if action == 'approve':
            # Kanalga jiberiletugin magliwmat turleri
            if form_type == 'vacancy':
                message = (
                    f"   📢 *Vakansiya!*\n"
                    f"🏢 Kompaniya: {item['company']}\n"
                    f"💼 Lawazim: {item['position']}\n"
                    f"📍 Manzil: {item['address']}\n"
                    f"⏱ Jumis waqti: {item['working_time']}\n"
                    f"📋 Talaplar: {item['requirements']}\n"
                    f"💰 Ayliq: {item['salary']}\n"
                    f"📞 Baylanisiw: {item['contacts']}\n"
                    f"📝 Qosimsha: {item['additional']}\n"
                )
            elif form_type == 'resume':
                message = (
                    f"   📄 *Rezyume!*\n"
                    f"👤 Ati: {item['full_name']}\n"
                    f"💼 Lawazim: {item['profession']}\n"
                    f"⏱ Jasi: {item['age']}\n"
                    f"📍 Manzil: {item['address']}\n"
                    f"📋 Talaplar: {item['skills']}\n"
                    f"📈 Tajiriybe: {item['experience']}\n"
                    f"💰 Ayliq: {item['salary']}\n"
                    f"🎯 Maqseti: {item['goal']}\n"
                    f"📞 Baylanisiw: {item['contacts']}\n"
                )
            elif form_type == 'project':
                message = (
                    f"   📊 *Proyekt!*\n"
                    f"👤 Specialist: {item['specialist']}\n"
                    f"📋 Task: {item['task']}\n"
                    f"💰 Byudjet: {item['budget']}\n"
                    f"📞 Baylanisiw: {item['contacts']}\n"
                    f"📝 Qosimsha: {item['additional']}\n"
                )
        
            # telegram kanalga jiberiw
            await send_telegram_message(message)
            # statusdi o‘zgertemiz
            await database.execute(table.update().where(table.c.id == item_id).values(status = "approved"))

            await callback_query.message.edit_text("✅ Kanalga jiberildi")
            await callback_query.answer("✅ Kanalga jiberildi")

        # Biykarlaw statusdi reject qilip ozgertiw
        elif action == 'reject':
            await database.execute(table.update().where(table.c.id == item_id).values(status = "rejected"))
            await callback_query.message.edit_text("❌ Magliwmat biykar qilindi.")
            await callback_query.answer("❌ Biykar etildi")
    
    except Exception as e:
        print(f"Callback parsing error: {e}")
        await callback_query.answer("❌ Qatelik boldi")
        return



#1
# @router.callback_query(lambda c: c.data.startswith(('approve_', )))
# async def approve_callback(callback_query: types.CallbackQuery):
#     message_id = uuid.UUID(callback_query.data.split("_", 1)[1])

#     query = vacancies.select().where(vacancies.c.id == message_id)
#     vacancy = await database.fetch_one(query)

#     if not vacancy:
#         await callback_query.answer("❌ Vakansiya tabilmadi")
#         return
    
#     print("Vacancy found:", vacancy)

#     message = (
#         f"   📢 *Vakansiya!*\n"
#         f"🏢 Kompaniya: {vacancy['company']}\n"
#         f"💼 Lawazim: {vacancy['position']}\n"
#         f"📍 Manzil: {vacancy['address']}\n"
#         f"⏱ Jumis waqti: {vacancy['working_time']}\n"
#         f"📋 Talaplar: {vacancy['requirements']}\n"
#         f"💰 Ayliq: {vacancy['salary']}\n"
#         f"📞 Baylanisiw: {vacancy['contacts']}\n"
#         f"📝 Qosimsha: {vacancy['additional']}\n"
#     )

#     await send_telegram_message(message)
#     await database.execute(
#         vacancies.update()
#         .where(vacancies.c.id == message_id)
#         .values(status="approved")
#     )

#     await callback_query.message.edit_text("✅ Kanalga jiberildi")
#     await callback_query.answer("✅ Kanalga jiberildi")

# @router.callback_query(lambda c: c.data.startswith("reject::"))
# async def reject_callback(callback_query: types.CallbackQuery):
#     try:
#         message_id = uuid.UUID(callback_query.data.split("::", 1)[1])

#         # Magliwmatti DB dan alip kelemiz
#         query = vacancies.select().where(vacancies.c.id == message_id)
#         vacancy = await database.fetch_one(query)

#         print("Reject callback vacancy:", vacancy)
#         if not vacancy:
#             await callback_query.answer("❌ Vakansiya tabilmadi")
#             return

#         # Statusdi o‘zgertemiz
#         await database.execute(
#             vacancies.update()
#             .where(vacancies.c.id == message_id)
#             .values(status="rejected")
#         ) 

#         await callback_query.message.edit_text("❌ Vakansiya biykar qilindi.")

#         # Adminga alert
#         await callback_query.answer("❌ Biykar etildi")

#     except Exception as e:
#         print(f"Reject callback xatosi: {e}")
#         await callback_query.answer("❌ Qatelik boldi", show_alert=True)
