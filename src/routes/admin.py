"""Admin routes for viewing contact submissions"""
from fasthtml.common import *
from src.components import Layout
from src.db import get_db_session
from src.models import ContactSubmission
from sqlmodel import select
import logging


def register_admin_routes(rt):
    """Register admin routes."""
    
    @rt('/admin/submissions')
    def get():
        """View all contact submissions."""
        logging.info("📊 Serving admin submissions page")
        
        session = get_db_session()
        try:
            # Get all submissions, ordered by newest first
            statement = select(ContactSubmission).order_by(ContactSubmission.created_at.desc())
            submissions = session.exec(statement).all()
            
            # Build the submissions table
            if submissions:
                table_rows = []
                for sub in submissions:
                    # Format the date
                    date_str = sub.created_at.strftime("%Y-%m-%d %H:%M")
                    
                    # Status badge
                    if sub.email_sent:
                        status_badge = Span("✅ Отправлено", cls="text-green-600 font-semibold")
                    else:
                        status_badge = Span("❌ Ошибка", cls="text-red-600 font-semibold")
                    
                    table_rows.append(
                        Tr(
                            Td(str(sub.id), cls="border px-4 py-2"),
                            Td(date_str, cls="border px-4 py-2"),
                            Td(sub.name, cls="border px-4 py-2"),
                            Td(sub.email, cls="border px-4 py-2"),
                            Td(sub.phone or "-", cls="border px-4 py-2"),
                            Td(sub.subject or "-", cls="border px-4 py-2 max-w-xs truncate"),
                            Td(sub.company or "-", cls="border px-4 py-2"),
                            Td(status_badge, cls="border px-4 py-2 text-center"),
                            Td(
                                Button(
                                    "Подробнее",
                                    hx_get=f"/admin/submissions/{sub.id}",
                                    hx_target="#detail-modal",
                                    cls="bg-blue-500 text-white px-3 py-1 rounded hover:bg-blue-600"
                                ),
                                cls="border px-4 py-2 text-center"
                            )
                        )
                    )
                
                submissions_table = Table(
                    Thead(
                        Tr(
                            Th("ID", cls="border px-4 py-2 bg-gray-100"),
                            Th("Дата", cls="border px-4 py-2 bg-gray-100"),
                            Th("Имя", cls="border px-4 py-2 bg-gray-100"),
                            Th("Email", cls="border px-4 py-2 bg-gray-100"),
                            Th("Телефон", cls="border px-4 py-2 bg-gray-100"),
                            Th("Тема", cls="border px-4 py-2 bg-gray-100"),
                            Th("Компания", cls="border px-4 py-2 bg-gray-100"),
                            Th("Статус", cls="border px-4 py-2 bg-gray-100"),
                            Th("Действия", cls="border px-4 py-2 bg-gray-100")
                        )
                    ),
                    Tbody(*table_rows),
                    cls="w-full border-collapse"
                )
            else:
                submissions_table = Div(
                    P("📭 Пока нет обращений", cls="text-gray-500 text-center py-8 text-lg"),
                    cls="bg-gray-50 rounded-lg"
                )
            
            content = Div(
                H1("Обращения клиентов", cls="text-3xl font-bold mb-6"),
                Div(
                    P(f"Всего обращений: {len(submissions)}", cls="text-lg mb-4 text-gray-700"),
                    cls="mb-6"
                ),
                Div(submissions_table, cls="overflow-x-auto"),
                Div(id="detail-modal", cls="mt-6"),
                cls="container mx-auto px-4 py-8"
            )
            
            return Layout("Админ - Обращения", content)
            
        except Exception as e:
            logging.error(f"❌ Error loading submissions: {e}")
            return Layout(
                "Ошибка",
                Div(
                    H1("Ошибка загрузки данных", cls="text-2xl text-red-600 mb-4"),
                    P(str(e), cls="text-gray-600"),
                    cls="container mx-auto px-4 py-8"
                )
            )
        finally:
            session.close()
    
    @rt('/admin/submissions/{id}')
    def get(id: int):
        """Get detailed view of a single submission."""
        session = get_db_session()
        try:
            submission = session.get(ContactSubmission, id)
            if not submission:
                return Div(
                    P("❌ Обращение не найдено", cls="text-red-600"),
                    cls="p-4 bg-red-50 rounded"
                )
            
            # Status badge
            if submission.email_sent:
                status = Div(
                    Span("✅ Email отправлен успешно", cls="text-green-600 font-semibold"),
                    cls="mb-4"
                )
            else:
                status = Div(
                    Span("❌ Ошибка отправки email", cls="text-red-600 font-semibold"),
                    P(submission.email_error or "Неизвестная ошибка", cls="text-sm text-gray-600 mt-1"),
                    cls="mb-4"
                )
            
            return Div(
                Div(
                    H2(f"Обращение №{submission.id}", cls="text-2xl font-bold mb-4"),
                    Div(
                        P(Strong("Дата: "), submission.created_at.strftime("%Y-%m-%d %H:%M:%S"), cls="mb-2"),
                        P(Strong("Имя: "), submission.name, cls="mb-2"),
                        P(Strong("Email: "), submission.email, cls="mb-2"),
                        P(Strong("Телефон: "), submission.phone or "-", cls="mb-2"),
                        P(Strong("Компания: "), submission.company or "-", cls="mb-2"),
                        P(Strong("Тема: "), submission.subject or "-", cls="mb-4"),
                        Div(
                            Strong("Сообщение:"),
                            P(submission.message, cls="mt-2 p-4 bg-gray-50 rounded whitespace-pre-wrap"),
                            cls="mb-4"
                        ),
                        status,
                        cls="text-gray-700"
                    ),
                    Button(
                        "Закрыть",
                        onclick="document.getElementById('detail-modal').innerHTML = ''",
                        cls="mt-4 bg-gray-500 text-white px-4 py-2 rounded hover:bg-gray-600"
                    ),
                    cls="bg-white p-6 rounded-lg shadow-lg border border-gray-200"
                ),
                cls="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-4",
                onclick="if(event.target === this) this.innerHTML = ''"
            )
            
        finally:
            session.close()
