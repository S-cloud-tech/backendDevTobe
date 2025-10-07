from django.shortcuts import render, redirect
from .models import Notification

def notification_dropdown(request):
    notifications = Notification.objects.filter(user=request.user).order_by('-created_at')[:10]
    unread_count = notifications.filter(is_read=False).count()

    context = {
        'notifications': notifications,
        'unread_count': unread_count,
    }
    return render(request, 'partials/notification_dropdown.html', context)

def mark_all_read(request):
    if request.method == "POST":
        Notification.objects.filter(user=request.user, is_read=False).update(is_read=True)
    return redirect(request.META.get('HTTP_REFERER', '/'))

def notifications_list(request):
    notifications = Notification.objects.filter(user=request.user)
    return render(request, 'notifications/notifications_list.html', {'notifications': notifications})
