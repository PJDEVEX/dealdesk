[1mdiff --git a/client/admin.py b/client/admin.py[m
[1mindex 3493dee..2900397 100644[m
[1m--- a/client/admin.py[m
[1m+++ b/client/admin.py[m
[36m@@ -13,7 +13,7 @@[m [mclass ClientAdmin(admin.ModelAdmin):[m
         'salesman',[m
         'created_on',[m
         'updated_on'[m
[31m-        )[m
[32m+[m[32m    )[m
     # Define the list of fields to be used for filtering the change list view[m
     list_filter = ([m
         'client_type',[m
[36m@@ -21,4 +21,4 @@[m [mclass ClientAdmin(admin.ModelAdmin):[m
         'country',[m
         'salesman',[m
         'manager'[m
[31m-        )[m
[32m+[m[32m    )[m
[1mdiff --git a/lead_master/admin.py b/lead_master/admin.py[m
[1mindex 30ec4a0..9be1a3d 100644[m
[1m--- a/lead_master/admin.py[m
[1m+++ b/lead_master/admin.py[m
[36m@@ -15,13 +15,13 @@[m [mclass LeadMasterAdmin(admin.ModelAdmin):[m
         'category',[m
         'type_of_construction',[m
         'lead_status',[m
[31m-        'est_closing_date',        [m
[32m+[m[32m        'est_closing_date',[m
         'est_date_of_delivery',[m
         'potential_value',[m
         'winning_chance',[m
         'forecast_pxp',[m
         'salesman',[m
[31m-        )[m
[32m+[m[32m    )[m
     # Define the list of fields to be used for filtering the change list view[m
     list_filter = ([m
         'lead_status',[m
[36m@@ -30,7 +30,7 @@[m [mclass LeadMasterAdmin(admin.ModelAdmin):[m
         'brand',[m
         'category',[m
         'salesman',[m
[31m-        )[m
[32m+[m[32m    )[m
     # Search fields allow searching by lead_master name, location, brand, category,[m
     # salesman, or client company name.[m
     search_fields = [[m
[36m@@ -41,7 +41,7 @@[m [mclass LeadMasterAdmin(admin.ModelAdmin):[m
         'salesman__first_name',[m
         'salesman__last_name',[m
         'client__company_name',[m
[31m-        ][m
[32m+[m[32m    ][m
     # Add a helper text so that user finds it easy to search[m
     change_list_template = 'admin/lead_master/lead_master_change_list.html'[m
 [m
[36m@@ -52,7 +52,7 @@[m [mclass BrandAdmin(admin.ModelAdmin):[m
     list_display = ([m
         'id',[m
         'brand',[m
[31m-        )[m
[32m+[m[32m    )[m
 [m
 [m
 @admin.register(Category)[m
[36m@@ -61,4 +61,4 @@[m [mclass CategoryAdmin(admin.ModelAdmin):[m
     list_display = ([m
         'id',[m
         'category',[m
[31m-        )[m
[32m+[m[32m    )[m
[1mdiff --git a/task_manager/admin.py b/task_manager/admin.py[m
[1mindex 43e90a8..27ea213 100644[m
[1m--- a/task_manager/admin.py[m
[1m+++ b/task_manager/admin.py[m
[36m@@ -15,9 +15,9 @@[m [mclass TaskManagerAdmin(admin.ModelAdmin):[m
         'status',[m
         'priority',[m
         'assigned_to',[m
[31m-        )[m
[32m+[m[32m    )[m
     # Define the list of fields to be used for filtering the change list view[m
     list_filter = ([m
         'status',[m
         'priority',[m
[31m-        )[m
\ No newline at end of file[m
[32m+[m[32m    )[m
[1mdiff --git a/task_manager/migrations/0001_initial.py b/task_manager/migrations/0001_initial.py[m
[1mindex 42fb101..9bb8353 100644[m
[1m--- a/task_manager/migrations/0001_initial.py[m
[1m+++ b/task_manager/migrations/0001_initial.py[m
[36m@@ -14,18 +14,15 @@[m [mclass Migration(migrations.Migration):[m
 [m
     operations = [[m
         migrations.CreateModel([m
[31m-            name='TaskManager',[m
[31m-            fields=[[m
[31m-                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),[m
[31m-                ('title', models.CharField(max_length=55)),[m
[31m-                ('description', models.CharField(max_length=255)),[m
[31m-                ('due_date', models.DateField()),[m
[31m-                ('status', models.CharField(choices=[('TBD', 'To Do'), ('D', 'Done')], default='To Do', max_length=50)),[m
[31m-                ('priority', models.CharField(choices=[('N', 'Normal'), ('U', 'Urgent')], default='Normal', max_length=50)),[m
[31m-                ('assigned_to', models.ForeignKey(on_delete=models.SET(task_manager.models.get_salesman), related_name='tasks', to='team.sar')),[m
[31m-            ],[m
[31m-            options={[m
[31m-                'ordering': ['due_date'],[m
[31m-            },[m
[31m-        ),[m
[31m-    ][m
[32m+[m[32m            name='TaskManager', fields=[[m
[32m+[m[32m                ('id', models.BigAutoField([m
[32m+[m[32m                    auto_created=True, primary_key=True, serialize=False, verbose_name='ID')), ('title', models.CharField([m
[32m+[m[32m                        max_length=55)), ('description', models.CharField([m
[32m+[m[32m                            max_length=255)), ('due_date', models.DateField()), ('status', models.CharField([m
[32m+[m[32m                                choices=[[m
[32m+[m[32m                                    ('TBD', 'To Do'), ('D', 'Done')], default='To Do', max_length=50)), ('priority', models.CharField([m
[32m+[m[32m                                        choices=[[m
[32m+[m[32m                                            ('N', 'Normal'), ('U', 'Urgent')], default='Normal', max_length=50)), ('assigned_to', models.ForeignKey([m
[32m+[m[32m                                                on_delete=models.SET([m
[32m+[m[32m                                                    task_manager.models.get_salesman), related_name='tasks', to='team.sar')), ], options={[m
[32m+[m[32m                'ordering': ['due_date'], }, ), ][m
[1mdiff --git a/team/admin.py b/team/admin.py[m
[1mindex 61dfee4..33e4080 100644[m
[1m--- a/team/admin.py[m
[1m+++ b/team/admin.py[m
[36m@@ -13,7 +13,7 @@[m [mclass ManagerAdmin(admin.ModelAdmin):[m
         'email',[m
         'created_on',[m
         'updated_on',[m
[31m-        )[m
[32m+[m[32m    )[m
 [m
 [m
 @admin.register(Sar)[m
[36m@@ -28,8 +28,8 @@[m [mclass SarAdmin(admin.ModelAdmin):[m
         'manager',[m
         'created_on',[m
         'updated_on',[m
[31m-        )[m
[32m+[m[32m    )[m
     # Let the user to filer the Sar by manager[m
     list_filter = ([m
         ('manager', admin.RelatedOnlyFieldListFilter),[m
[31m-        )[m
[32m+[m[32m    )[m
