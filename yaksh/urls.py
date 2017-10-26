from django.conf.urls import patterns, url
from yaksh import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout),
    url(r'^update_email/$', views.update_email, name="update_email"),
    url(r'^activate/(?P<key>.+)$', views.activate_user, name="activate"),
    url(r'^new_activation/$', views.new_activation, name='new_activation'),
    url(r'^quizzes/$', views.quizlist_user, name='quizlist_user'),
    url(r'^quizzes/(?P<enrolled>\w+)/$', views.quizlist_user, name='quizlist_user'),
    url(r'^results/$', views.results_user),
    url(r'^start/$', views.start),
    url(r'^start/(?P<questionpaper_id>\d+)/$', views.start),
    url(r'^start/(?P<attempt_num>\d+)/(?P<questionpaper_id>\d+)/$', views.start),
    url(r'^quit/(?P<attempt_num>\d+)/(?P<questionpaper_id>\d+)/$', views.quit),
    url(r'^complete/$', views.complete),
    url(r'^complete/(?P<attempt_num>\d+)/(?P<questionpaper_id>\d+)/$',\
            views.complete),
    url(r'^register/$', views.user_register, name="register"),
    url(r'^(?P<q_id>\d+)/check/$', views.check, name="check"),
    url(r'^get_result/(?P<uid>\d+)/$', views.get_result),
    url(r'^(?P<q_id>\d+)/check/(?P<attempt_num>\d+)/(?P<questionpaper_id>\d+)/$',\
            views.check, name="check"),
    url(r'^(?P<q_id>\d+)/skip/(?P<attempt_num>\d+)/(?P<questionpaper_id>\d+)/$',
        views.skip),
    url(r'^(?P<q_id>\d+)/skip/(?P<next_q>\d+)/(?P<attempt_num>\d+)/(?P<questionpaper_id>\d+)/$',
        views.skip),
    url(r'^enroll_request/(?P<course_id>\d+)/$', views.enroll_request, name='enroll_request'),
    url(r'^self_enroll/(?P<course_id>\d+)/$', views.self_enroll, name='self_enroll'),
    url(r'^view_answerpaper/(?P<questionpaper_id>\d+)/$', views.view_answerpaper, name='view_answerpaper'),
    url(r'^manage/$', views.prof_manage, name='manage'),
    url(r'^manage/addquestion/$', views.add_question, name="add_question"),
    url(r'^manage/addquestion/(?P<question_id>\d+)/$', views.add_question,
                                        name="add_question"),
    url(r'^manage/addquiz/(?P<course_id>\d+)/$', views.add_quiz, name='add_quiz'),
    url(r'^manage/addquiz/(?P<course_id>\d+)/(?P<quiz_id>\d+)/$', views.add_quiz, name='edit_quiz'),
    url(r'^manage/gradeuser/$', views.grade_user, name="grade_user"),
    url(r'^manage/gradeuser/(?P<quiz_id>\d+)/$',views.grade_user, name="grade_user"),
    url(r'^manage/gradeuser/(?P<quiz_id>\d+)/(?P<user_id>\d+)/$',
            views.grade_user, name="grade_user"),
    url(r'^manage/gradeuser/(?P<quiz_id>\d+)/(?P<user_id>\d+)/(?P<attempt_number>\d+)/$',
            views.grade_user, name="grade_user"),
    url(r'^manage/questions/$', views.show_all_questions, name="show_questions"),
    url(r'^manage/monitor/$', views.monitor, name="monitor"),
    url(r'^manage/monitor/(?P<quiz_id>\d+)/$', views.monitor, name="monitor"),
    url(r'^manage/user_data/(?P<user_id>\d+)/(?P<questionpaper_id>\d+)/$',
        views.user_data, name="user_data"),
    url(r'^manage/user_data/(?P<user_id>\d+)/$', views.user_data),
    url(r'^manage/quiz/designquestionpaper/(?P<quiz_id>\d+)/$', views.design_questionpaper,
        name='design_questionpaper'),
    url(r'^manage/designquestionpaper/(?P<quiz_id>\d+)/(?P<questionpaper_id>\d+)/$',
        views.design_questionpaper, name='designquestionpaper'),
    url(r'^manage/statistics/question/(?P<questionpaper_id>\d+)/$',
        views.show_statistics, name="show_statistics"),
    url(r'^manage/statistics/question/(?P<questionpaper_id>\d+)/(?P<attempt_number>\d+)/$',
        views.show_statistics, name="show_statistics"),
    url(r'^manage/download_quiz_csv/(?P<course_id>\d+)/(?P<quiz_id>\d+)/$',
        views.download_quiz_csv, name="download_quiz_csv"),
    url(r'^manage/duplicate_course/(?P<course_id>\d+)/$', views.duplicate_course,
        name='duplicate_course'),
    url(r'manage/courses/$', views.courses, name='courses'),
    url(r'manage/add_course/$', views.add_course, name='add_course'),
    url(r'manage/edit_course/(?P<course_id>\d+)$', views.add_course, name='edit_course'),
    url(r'manage/course_detail/(?P<course_id>\d+)/$', views.course_detail, name='course_detail'),
    url(r'manage/enroll/(?P<course_id>\d+)/(?P<user_id>\d+)/$', views.enroll,
            name="enroll_user"),
    url(r'manage/enroll/rejected/(?P<course_id>\d+)/(?P<user_id>\d+)/$',
        views.enroll, {'was_rejected': True}),
    url(r'manage/send_mail/(?P<course_id>\d+)/$', views.send_mail, name="send_mail"),
    url(r'manage/reject/(?P<course_id>\d+)/(?P<user_id>\d+)/$', views.reject,
            name="reject_user"),
    url(r'manage/enrolled/reject/(?P<course_id>\d+)/(?P<user_id>\d+)/$',
        views.reject, {'was_enrolled': True}, name="reject_user"),
    url(r'manage/toggle_status/(?P<course_id>\d+)/$', views.toggle_course_status,
            name="toggle_course_status"),
    url(r'^ajax/questions/filter/$', views.ajax_questions_filter,
                name="questions_filter"),
    url(r'^editprofile/$', views.edit_profile, name='edit_profile'),
    url(r'^viewprofile/$', views.view_profile, name='view_profile'),
    url(r'^manage/enroll/(?P<course_id>\d+)/$', views.enroll, name="enroll_users"),
    url(r'manage/enroll/rejected/(?P<course_id>\d+)/$',
        views.enroll, {'was_rejected': True}),
    url(r'manage/enrolled/reject/(?P<course_id>\d+)/$',
        views.reject, {'was_enrolled': True}, name="reject_users"),
    url(r'^manage/searchteacher/(?P<course_id>\d+)/$', views.search_teacher),
    url(r'^manage/addteacher/(?P<course_id>\d+)/$', views.add_teacher, name='add_teacher'),
    url(r'^manage/remove_teachers/(?P<course_id>\d+)/$', views.remove_teachers, name='remove_teacher'),
    url(r'^manage/download_questions/$', views.show_all_questions,
                        name="show_questions"),
    url(r'^manage/upload_questions/$', views.show_all_questions,
                        name="show_questions"),
    url(r'^manage/grader/$', views.grader, name='grader'),
    url(r'^manage/regrade/question/(?P<course_id>\d+)/(?P<question_id>\d+)/$',
            views.regrade, name='regrade'),
    url(r'^manage/regrade/questionpaper/(?P<course_id>\d+)/(?P<question_id>\d+)/(?P<questionpaper_id>\d+)/$',
            views.regrade, name='regrade'),
    url(r'^manage/regrade/answerpaper/(?P<course_id>\d+)/(?P<question_id>\d+)/(?P<answerpaper_id>\d+)/$',
            views.regrade, name='regrade'),
    url(r'^manage/regrade/paper/(?P<course_id>\d+)/(?P<answerpaper_id>\d+)/$',
            views.regrade, name='regrade'),
    url(r'^manage/(?P<mode>[\w\-]+)/(?P<quiz_id>\d+)/$', views.test_quiz),
    url(r'^manage/create_demo_course/$', views.create_demo_course),
    url(r'^manage/courses/download_course_csv/(?P<course_id>\d+)/$',
        views.download_course_csv, name="download_course_csv"),
    url(r'^manage/download/user_assignment/(?P<question_id>\d+)/(?P<user_id>\d+)/(?P<quiz_id>\d+)/$',
        views.download_assignment_file, name="download_user_assignment"),
    url(r'^manage/download/quiz_assignments/(?P<quiz_id>\d+)/$',
        views.download_assignment_file, name="download_quiz_assignment"),
    url(r'^manage/courses/download_yaml_template/',
        views.download_yaml_template, name="download_yaml_template"),
]
