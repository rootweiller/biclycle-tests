from django.urls import path

from bicycle import views

urlpatterns = [
    path('list/', views.BicycleView.as_view(), name='list_bicycle'),
    path('update/<int:pk>', views.BicycleUpdateView.as_view(),
         name='update_bicycle'),
    path('delete/<int:pk>', views.BicycleDestroyView.as_view(),
         name='delete_bicycle')
]
