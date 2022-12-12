from django.urls import path

#from todolist.goals import views
from goals import views


urlpatterns = [
    path("board/create", views.BoardCreateView.as_view(), name="create-board"),
    path("board/list", views.BoardListView.as_view(), name="list-board"),
    path("board/<pk>", views.BoardView.as_view(), name="Retrieve-Update-Destroy-board"),

    path("goal_category/create", views.GoalCategoryCreateView.as_view()),
    path("goal_category/list", views.GoalCategoryListView.as_view()),
    path("goal_category/<pk>", views.GoalCategoryView.as_view()),

    path("goal/create", views.GoalCreateView.as_view()),
    path("goal/list", views.GoalListView.as_view()),
    path("goal/<pk>", views.GoalView.as_view()),

    path("goal_comment/create", views.GoalCommentCreateView.as_view()),
    path("goal_comment/list", views.GoalCommentListView.as_view()),
    path("goal_comment/<pk>", views.GoalCommentView.as_view()),
]
