from django.shortcuts import render, get_object_or_404, redirect
from friendship.models import Friend, Follow, Block, FriendshipRequest
from users.models import CustomUser

# Create your views here.

def friend_add(request, friendid):
    try:
        other_user = get_object_or_404(CustomUser, pk=friendid)
        if Block.objects.is_blocked(request.user, other_user) == True:
            if other_user.id in Block.objects.blocking(request.user):
                return render(request, 'error.html', {"reason":"You have blocked this user."})
            else:
                return render(request, 'error.html', {"reason":"You have been blocked by this user."})
        Friend.objects.add_friend(
            request.user,                               # The sender
            other_user)                                 # The recipient
    except Exception as e:
        print(e)
        if (e == "Friendship already requested"):
            return render(request, 'error.html', {"reason":"Request Already Sent"})
        else:
            return render(request, 'error.html', {"reason":e})
    return render(request, 'friend_sent.html',)


def request_accept(request, requestid):
    try:
        other_user = get_object_or_404(CustomUser, pk=requestid)
        touser = request.user.pk
        friend_request = FriendshipRequest.objects.filter(to_user=touser).get(from_user=requestid)
        friend_request.accept()
    except Exception as e:
        print(e)
        return render(request, 'error.html', {"reason":e})
    return redirect("/")

def request_reject(request, requestid):
    try:
        other_user = get_object_or_404(CustomUser, pk=requestid)
        touser = request.user.pk
        friend_request = FriendshipRequest.objects.filter(to_user=touser).get(from_user=requestid)
        friend_request.delete()
    except Exception as e:
        print(e)
        return render(request, 'error.html', {"reason":e})
    return redirect("/")


def friend_unfriend(request, requestid):
    try:
        blockuser = CustomUser.objects.get(pk=requestid)
        Friend.objects.remove_friend(request.user, blockuser)
    except Exception as e:
        print(e)
        return render(request, 'error.html', {"reason":e})
    return redirect("/")
