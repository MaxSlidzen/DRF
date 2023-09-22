from rest_framework.permissions import BasePermission


class AuthorOrModerator(BasePermission):
    def has_permission(self, request, view):
        # Изменение объекта либо автором, либо модератором
        return request.user.is_staff or request.user == view.get_object().author


class NotModerator(BasePermission):
    def has_permission(self, request, view):
        # Создание объекта кем-угодно, но не модератором
        return not request.user.is_staff


class AuthorOrModeratorOrCustomer(BasePermission):
    def has_permission(self, request, view):
        # Просмотр объекта либо автором, либо модератором, либо тем, кто оплатил учебный материал
        return request.user == view.get_object().author or request.user.is_staff or len(
            view.get_object().payment.filter(user=request.user)) > 0


class OnlyAuthor(BasePermission):
    def has_permission(self, request, view):
        # Удаление объекта только автором
        return request.user == view.get_object().author
