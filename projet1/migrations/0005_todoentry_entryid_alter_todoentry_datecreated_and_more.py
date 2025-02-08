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
            entry.save()
            print(f"Assigned entryid {index} to entry {entry.id}")  # Debug statement

            

class Migration(migrations.Migration):
    dependencies = [
        # Replace with the last migration file in your app
        ('projet1', '0004_auto_20250208_1049'),
    ]

    operations = [
        migrations.RunPython(populate_entryid),
    ]