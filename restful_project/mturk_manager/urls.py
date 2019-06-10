from django.urls import path, include
from mturk_manager import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r"accounts", views.Accounts)
router.register(r"keywords", views.Keywords)
router.register(r"messages-reject", views.MessagesReject)
router.register(r"qualifications", views.Qualifications)
router.register(r"workers", views.Workers)
# Ctrl + Shift + P --> Formating --> Save Without Formatting

urlpatterns = [
    path("", include(router.urls)),
    # Project lookup
    # path("projects/", views.Projects.as_view(), name="projects"),
    # path("projects/<slug:slug_project>/", views.ProjectDetail.as_View(), name="project_detail"),

    # path("projects/<slug:slug_project>/settings/", views.ProjectSettingsBatch.as_view(), name="project_settings_batch"),
    # path("projects/<slug:slug_project>/settings/<int:settings_id>/", views.ProjectSettingsBatchDetail.as_view(), name="project_settings_batch_detail"),

    # path("projects/<slug:slug_project>/templates-worker/", views.ProjectTemplatesWorker.as_view(), name="project_templates_worker"),
    # path("projects/<slug:slug_project>/templates-worker/<int:template_id>/", views.ProjectTemplatesWorkerDetail.as_view(), name="project_templates_worker_detail"),

    # path("projects/<slug:slug_project>/batches/", views.ProjectBatches.as_view(), name="project_batches"),
    # path("projects/<slug:slug_project>/batches/<int:batch_id>", views.ProjectBatchesDetail.as_view(), name="project_batches_detail"),
    # path("projects/<slug:slug_project>/batches/<int:batch_id>/hits/", views.ProjectBatchesDetailHITs.as_view(), name="project_batch_hits"),

    # path("projects/<slug:slug_project>/hits/", views.ProjectHITs.as_view(), name="project_hits"),
    # path("projects/<slug:slug_project>/hits/<int:hit_id>", views.ProjectHITDetail.as_view(), name="project_hit_detail"),

    # path("projects/<slug:slug_project>/hits/<int:hit_id>/assignments/", views.Assignments.as_view(), name="assignments"),
    # path("projects/<slug:slug_project>/hits/<int:hit_id>/assignments/<int:assignment_id>/", views.AssignmentsDetail.as_view(), name="assignments_detail"),

    # path("projects/workers/", views.ProjectWorkers.as_view(), name="project_workers"),
    # path("projects/workers/<int:id_worker>/", views.ProjectWorkersDetail.as_view(), name="project_workers_detail"),
    # path("projects/blocked-workers/", views.ProjectBlockedWorkers.as_view(), name="project_blocked_workers"),



    # # Global lookup
    # path("accounts/", views.Accounts.as_view(), name="accounts"),
    # path("accounts/<str:name>/", views.AccountsDetail.as_view(), name="accounts_detail"),
    # path("hits/", views.HITs.as_view(), name="hits"),
    # path("hits/<int:hit_id>/", views.HITDetail.as_view(), name="hit_detail"),
    # path("settings/", views.SettingsBatch.as_view(), name="settings_batch"),
    # path("keywords/", views.Keywords.as_view(), name="keywords"),
    # path("messages-reject/", views.MessagesReject.as_view(), name="messages_reject"),
    # path("messages-reject/<int:id>/", views.MessageRejectDetail.as_view(), name="message_reject_detail"),
    # path("qualifications/", views.Qualifications.as_view(), name="qualifications"),
    # path("qualifications/<int:id>/", views.QualificationsDetail.as_view(), name="qualifications_detail"),
    # path("templates_worker/", views.TemplatesWorker.as_view(), name="templates_worker"),
    # path("workers/", views.Workers.as_view(), name="workers"),
    # path("workers/<int:id_worker>", views.WorkersDetail.as_view(), name="workers_detail")
]
