from django.contrib import admin
from .models import Department, Course, Video

# Register your models here.

class VideoAdmin(admin.ModelAdmin):
    exclude = ('published_by', )
    list_display = ('video_title','publication_date','video_file')

    def has_change_permission(self, request, obj=None):
        has_class_permission = super(VideoAdmin, self).has_change_permission(request, obj)
        if not has_class_permission:
            return False
        if obj is not None and not request.user.is_superuser and request.user.id != obj.published_by.id:
            return False
        return True

    def has_delete_permission(self, request, obj=None):
        has_class_permission = super(VideoAdmin, self).has_delete_permission(request, obj)
        if not has_class_permission:
            return False
        if obj is not None and not request.user.is_superuser and request.user.id != obj.published_by.id:
            return False
        return True


    def queryset(self, request):
        if request.user.is_superuser:
            return Video.objects.all()
        return Video.objects.filter(published_by=request.user.id)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.published_by = request.user
        obj.save()
        """obj.user = request.user
        super().save_model(request, obj,form,change)"""
class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'department_short_name', 'course_description', 'course_code')

    def has_change_permission(self, request, obj=None):
        has_class_permission = super(CourseAdmin, self).has_change_permission(request, obj)
        if not has_class_permission:
            return False
        if obj is not None and not request.user.is_superuser:
            return False
        return True
    
    def has_delete_permission(self, request, obj=None):
        has_class_permission = super(CourseAdmin, self).has_delete_permission(request, obj)
        if not has_class_permission:
            return False
        if obj is not None and not request.user.is_superuser:
            return False
        return True

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('department_name', 'department_description', 'department_short_name')

    def has_change_permission(self, request, obj=None):
        has_class_permission = super(DepartmentAdmin, self).has_change_permission(request, obj)
        if not has_class_permission:
            return False
        if obj is not None and not request.user.is_superuser:
            return False
        return True
    
    def has_delete_permission(self, request, obj=None):
        has_class_permission = super(DepartmentAdmin, self).has_delete_permission(request, obj)
        if not has_class_permission:
            return False
        if obj is not None and not request.user.is_superuser:
            return False
        return True

admin.site.register(Department, DepartmentAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Video, VideoAdmin)