from .serializers import LessonSessionSerializer

def approve_lesson_session(lesson_session):
    data = {
        'status' : 'approved'
    }
    return LessonSessionSerializer(instance=lesson_session, data=data, partial=True)

def decline_lesson_session(lesson_session):
    data = {
            'status' : 'declined'
    }
    return LessonSessionSerializer(instance=lesson_session,data=data,partial=True)

def finish_lesson_session(lesson_session):
    data = {
            'status' : 'finished'
    }
    return LessonSessionSerializer(instance=lesson_session,data=data,partial=True)