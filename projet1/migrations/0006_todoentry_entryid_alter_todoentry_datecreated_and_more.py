from django.db import migrations

def populate_entryid(apps, schema_editor):
    TodoEntry = apps.get_model('projet1', 'TodoEntry')
    User = apps.get_model('auth', 'User')

    # Iterate over all users
    for user in User.objects.all():
        print(f"Processing user: {user.id}")  # Debug statement
        # Get all entries for the user, ordered by dateCreated
        entries = TodoEntry.objects.filter(user=user).order_by('dateCreated')
        print(f"Found {entries.count()} entries for user {user.id}")  # Debug statement
        
        # Assign entryid starting from 1
        for index, entry in enumerate(entries, start=1):
            entry.entryid = index
        
        # Bulk update all entries for the user
        TodoEntry.objects.bulk_update(entries, ['entryid'])
        print(f"Updated {len(entries)} entries for user {user.id}")  # Debug statement

            

class Migration(migrations.Migration):
    dependencies = [
        # Replace with the last migration file in your app
        ('projet1', '0005_todoentry_entryid_alter_todoentry_datecreated_and_more'),
    ]

    operations = [
        migrations.RunPython(populate_entryid),
    ]