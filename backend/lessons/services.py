from .choices import APPROVED_STATUS, FINISHED_STATUS, DECLINED_STATUS


def approve_lesson_session(lesson_session):
    lesson_session.status = APPROVED_STATUS
    lesson_session.save(update_fields=['status'])


def decline_lesson_session(lesson_session):
    lesson_session.status = DECLINED_STATUS
    lesson_session.save(update_fields=['status'])

def finish_lesson_session(lesson_session):
    lesson_session.status = FINISHED_STATUS
    lesson_session.save(update_fields=['status'])