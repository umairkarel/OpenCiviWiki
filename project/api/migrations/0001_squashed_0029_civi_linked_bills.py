# Generated by Django 3.2.7 on 2021-09-20 08:23

import common.utils
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [('api', '0001_initial'), ('api', '0002_auto_20161215_0139'), ('api', '0003_auto_20161227_1342'), ('api', '0004_auto_20161230_0412'), ('api', '0005_auto_20170109_1813'), ('api', '0006_auto_20170110_0519'), ('api', '0007_auto_20170110_0850'), ('api', '0008_auto_20170110_0850'), ('api', '0009_auto_20170110_1828'), ('api', '0010_auto_20170110_1830'), ('api', '0011_activity'), ('api', '0012_auto_20170116_0856'), ('api', '0013_auto_20170116_1304'), ('api', '0014_auto_20170124_1944'), ('api', '0015_auto_20170331_0710'), ('api', '0016_remove_civiimage_last_modified'), ('api', '0017_auto_20170331_1233'), ('api', '0018_representative_official_full_name'), ('api', '0019_auto_20170418_0727'), ('api', '0020_auto_20170418_1652'), ('api', '0021_auto_20170418_2111'), ('api', '0022_auto_20170531_1316'), ('api', '0023_auto_20170615_0827'), ('api', '0024_remove_civi_links'), ('api', '0025_thread_is_draft'), ('api', '0026_account_country'), ('api', '0027_auto_20190226_1001'), ('api', '0028_auto_20190304_1834'), ('api', '0029_civi_linked_bills')]

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=63)),
                ('last_name', models.CharField(max_length=63)),
                ('about_me', models.CharField(blank=True, max_length=511)),
                ('longitude', models.DecimalField(decimal_places=6, default=0, max_digits=9)),
                ('latitude', models.DecimalField(decimal_places=6, default=0, max_digits=9)),
                ('address', models.CharField(max_length=255, null=True)),
                ('city', models.CharField(blank=True, max_length=63)),
                ('state', models.CharField(blank=True, choices=[(b'AL', b'Alabama'), (b'AK', b'Alaska'), (b'AZ', b'Arizona'), (b'AR', b'Arkansas'), (b'CA', b'California'), (b'CO', b'Colorado'), (b'CT', b'Connecticut'), (b'DE', b'Delaware'), (b'DC', b'District of Columbia'), (b'FL', b'Florida'), (b'GA', b'Georgia'), (b'HI', b'Hawaii'), (b'ID', b'Idaho'), (b'IL', b'Illinois'), (b'IN', b'Indiana'), (b'IA', b'Iowa'), (b'KS', b'Kansas'), (b'KY', b'Kentucky'), (b'LA', b'Louisiana'), (b'ME', b'Maine'), (b'MD', b'Maryland'), (b'MA', b'Massachusetts'), (b'MI', b'Michigan'), (b'MN', b'Minnesota'), (b'MS', b'Mississippi'), (b'MO', b'Missouri'), (b'MT', b'Montana'), (b'NE', b'Nebraska'), (b'NV', b'Nevada'), (b'NH', b'New Hampshire'), (b'NJ', b'New Jersey'), (b'NM', b'New Mexico'), (b'NY', b'New York'), (b'NC', b'North Carolina'), (b'ND', b'North Dakota'), (b'OH', b'Ohio'), (b'OK', b'Oklahoma'), (b'OR', b'Oregon'), (b'PA', b'Pennsylvania'), (b'RI', b'Rhode Island'), (b'SC', b'South Carolina'), (b'SD', b'South Dakota'), (b'TN', b'Tennessee'), (b'TX', b'Texas'), (b'UT', b'Utah'), (b'VT', b'Vermont'), (b'VA', b'Virginia'), (b'WA', b'Washington'), (b'WV', b'West Virginia'), (b'WI', b'Wisconsin'), (b'WY', b'Wyoming')], max_length=2)),
                ('zip_code', models.CharField(max_length=6, null=True)),
                ('fed_district', models.CharField(default=None, max_length=63, null=True)),
                ('state_district', models.CharField(default=None, max_length=63, null=True)),
                ('beta_access', models.BooleanField(default=False)),
                ('full_account', models.BooleanField(default=False)),
                ('profile_image', models.ImageField(blank=True, default=b'profile/default.png', null=True, upload_to=common.utils.PathAndRename(b'profile/'))),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=63)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_modified', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Civi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=127)),
                ('body', models.CharField(max_length=4095)),
                ('c_type', models.CharField(choices=[(b'problem', b'Problem'), (b'cause', b'Cause'), (b'solution', b'Solution')], default=b'problem', max_length=31)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_modified', models.DateTimeField(auto_now=True, null=True)),
                ('author', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='api.account')),
                ('votes_neutral', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Hashtag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=63)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_modified', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=127)),
                ('body', models.TextField(max_length=2047)),
                ('votes_vneg', models.IntegerField(default=0)),
                ('votes_neg', models.IntegerField(default=0)),
                ('votes_neutral', models.IntegerField(default=0)),
                ('votes_pos', models.IntegerField(default=0)),
                ('votes_vpos', models.IntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_modified', models.DateTimeField(auto_now=True, null=True)),
                ('author', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='api.account')),
                ('civi', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='api.civi')),
            ],
        ),
        migrations.CreateModel(
            name='Rebuttal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(max_length=1023)),
                ('votes_vneg', models.IntegerField(default=0)),
                ('votes_neg', models.IntegerField(default=0)),
                ('votes_neutral', models.IntegerField(default=0)),
                ('votes_pos', models.IntegerField(default=0)),
                ('votes_vpos', models.IntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_modified', models.DateTimeField(auto_now=True, null=True)),
                ('author', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='api.account')),
                ('response', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='api.response')),
            ],
        ),
        migrations.AddField(
            model_name='civi',
            name='hashtags',
            field=models.ManyToManyField(to='api.Hashtag'),
        ),
        migrations.AddField(
            model_name='account',
            name='ai_interests',
            field=models.ManyToManyField(related_name='ai_interests', to='api.Hashtag'),
        ),
        migrations.AddField(
            model_name='account',
            name='followers',
            field=models.ManyToManyField(related_name='_account_followers_+', to='api.Account'),
        ),
        migrations.AddField(
            model_name='account',
            name='following',
            field=models.ManyToManyField(related_name='_account_following_+', to='api.Account'),
        ),
        migrations.AddField(
            model_name='account',
            name='interests',
            field=models.ManyToManyField(related_name='interests', to='api.Hashtag'),
        ),
        migrations.AddField(
            model_name='account',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='account',
            name='followers',
            field=models.ManyToManyField(related_name='follower', to='api.Account'),
        ),
        migrations.AlterField(
            model_name='account',
            name='following',
            field=models.ManyToManyField(related_name='followings', to='api.Account'),
        ),
        migrations.CreateModel(
            name='Representative',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district', models.CharField(blank=True, max_length=63, null=True)),
                ('state', models.CharField(max_length=63)),
                ('level', models.CharField(choices=[(b'federal', b'Federal'), (b'state', b'State')], default=b'federal', max_length=31)),
                ('term_start', models.DateField()),
                ('term_end', models.DateField()),
                ('party', models.CharField(max_length=127)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_modified', models.DateTimeField(auto_now=True, null=True)),
                ('bioguideID', models.CharField(blank=True, max_length=7, null=True)),
                ('senate_class', models.CharField(blank=True, max_length=63, null=True)),
                ('about_me', models.CharField(blank=True, max_length=511)),
                ('first_name', models.CharField(default='', max_length=63)),
                ('last_name', models.CharField(default='', max_length=63)),
                ('official_full_name', models.CharField(blank=True, max_length=127, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=1023)),
                ('short_title', models.CharField(max_length=1023)),
                ('short_summary', models.CharField(max_length=1023)),
                ('number', models.CharField(max_length=20)),
                ('b_type', models.CharField(max_length=63)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_modified', models.DateTimeField(auto_now=True, null=True)),
                ('congress_url', models.URLField(blank=True, null=True)),
                ('govtrack_url', models.URLField(blank=True, null=True)),
                ('source', models.CharField(choices=[(b'sunlight', b'sunlight'), (b'propublica', b'propublica')], default=b'propublica', max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='civi',
            name='bill',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='api.bill'),
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote', models.CharField(choices=[(b'yes', b'Yes'), (b'no', b'No'), (b'abstain', b'Abstain')], default=b'abstain', max_length=31)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_modified', models.DateTimeField(auto_now=True, null=True)),
                ('bill', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='api.bill')),
                ('representative', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='api.representative')),
            ],
        ),
        migrations.CreateModel(
            name='Rationale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=127)),
                ('body', models.TextField(max_length=4095)),
                ('votes_vneg', models.IntegerField(default=0)),
                ('votes_neg', models.IntegerField(default=0)),
                ('votes_neutral', models.IntegerField(default=0)),
                ('votes_pos', models.IntegerField(default=0)),
                ('votes_vpos', models.IntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_modified', models.DateTimeField(auto_now=True, null=True)),
                ('bill', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='api.bill')),
                ('vote', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='api.vote')),
                ('representative', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='api.representative')),
            ],
        ),
        migrations.CreateModel(
            name='Fact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.CharField(max_length=511)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_modified', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=127)),
                ('summary', models.CharField(max_length=4095)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_modified', models.DateTimeField(auto_now=True, null=True)),
                ('author', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='api.account')),
                ('category', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='api.category')),
                ('facts', models.ManyToManyField(to='api.Fact')),
                ('hashtags', models.ManyToManyField(to='api.Hashtag')),
                ('num_civis', models.IntegerField(default=0)),
                ('num_solutions', models.IntegerField(default=0)),
                ('num_views', models.IntegerField(default=0)),
                ('image', models.ImageField(blank=True, null=True, upload_to=common.utils.PathAndRename(b''))),
                ('level', models.CharField(choices=[(b'federal', b'Federal'), (b'state', b'State')], default=b'federal', max_length=31)),
                ('state', models.CharField(blank=True, choices=[(b'AL', b'Alabama'), (b'AK', b'Alaska'), (b'AZ', b'Arizona'), (b'AR', b'Arkansas'), (b'CA', b'California'), (b'CO', b'Colorado'), (b'CT', b'Connecticut'), (b'DE', b'Delaware'), (b'DC', b'District of Columbia'), (b'FL', b'Florida'), (b'GA', b'Georgia'), (b'HI', b'Hawaii'), (b'ID', b'Idaho'), (b'IL', b'Illinois'), (b'IN', b'Indiana'), (b'IA', b'Iowa'), (b'KS', b'Kansas'), (b'KY', b'Kentucky'), (b'LA', b'Louisiana'), (b'ME', b'Maine'), (b'MD', b'Maryland'), (b'MA', b'Massachusetts'), (b'MI', b'Michigan'), (b'MN', b'Minnesota'), (b'MS', b'Mississippi'), (b'MO', b'Missouri'), (b'MT', b'Montana'), (b'NE', b'Nebraska'), (b'NV', b'Nevada'), (b'NH', b'New Hampshire'), (b'NJ', b'New Jersey'), (b'NM', b'New Mexico'), (b'NY', b'New York'), (b'NC', b'North Carolina'), (b'ND', b'North Dakota'), (b'OH', b'Ohio'), (b'OK', b'Oklahoma'), (b'OR', b'Oregon'), (b'PA', b'Pennsylvania'), (b'RI', b'Rhode Island'), (b'SC', b'South Carolina'), (b'SD', b'South Dakota'), (b'TN', b'Tennessee'), (b'TX', b'Texas'), (b'UT', b'Utah'), (b'VT', b'Vermont'), (b'VA', b'Virginia'), (b'WA', b'Washington'), (b'WV', b'West Virginia'), (b'WI', b'Wisconsin'), (b'WY', b'Wyoming')], max_length=2)),
                ('is_draft', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_type', models.CharField(choices=[(b'new_follower', b'New follower'), (b'response_to_yout_civi', b'Response to your civi'), (b'rebuttal_to_your_response', b'Rebuttal to your response')], default=b'new_follower', max_length=31)),
                ('read', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_modified', models.DateTimeField(auto_now=True, null=True)),
                ('account', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='api.account')),
                ('civi', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='api.civi')),
                ('thread', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='api.thread')),
            ],
        ),
        migrations.AddField(
            model_name='civi',
            name='thread',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='civis', to='api.thread'),
        ),
        migrations.AddField(
            model_name='account',
            name='categories',
            field=models.ManyToManyField(related_name='user_categories', to='api.Category'),
        ),
        migrations.AlterField(
            model_name='civi',
            name='c_type',
            field=models.CharField(choices=[(b'problem', b'Problem'), (b'cause', b'Cause'), (b'solution', b'Solution'), (b'response', b'Response')], default=b'problem', max_length=31),
        ),
        migrations.AddField(
            model_name='civi',
            name='linked_civis',
            field=models.ManyToManyField(related_name='_linked_civis_+', to='api.Civi'),
        ),
        migrations.AddField(
            model_name='civi',
            name='response_civis',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='responses', to='api.civi'),
        ),
        migrations.AlterField(
            model_name='civi',
            name='body',
            field=models.CharField(max_length=1023),
        ),
        migrations.AddField(
            model_name='civi',
            name='votes_neg',
            field=models.IntegerField(default=0),
        ),
        migrations.RenameField(
            model_name='civi',
            old_name='votes_neutral',
            new_name='votes_neutral',
        ),
        migrations.AddField(
            model_name='civi',
            name='votes_pos',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='civi',
            name='votes_vneg',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='civi',
            name='votes_vpos',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='civi',
            name='linked_civis',
            field=models.ManyToManyField(default=None, null=True, related_name='_linked_civis_+', to='api.Civi'),
        ),
        migrations.AlterField(
            model_name='civi',
            name='response_civis',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='responses', to='api.civi'),
        ),
        migrations.AlterField(
            model_name='civi',
            name='title',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='civi',
            name='linked_civis',
            field=models.ManyToManyField(related_name='_linked_civis_+', to='api.Civi'),
        ),
        migrations.AlterField(
            model_name='account',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to=common.utils.PathAndRename(b'profile/')),
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_type', models.CharField(choices=[(b'vote_vneg', b'Vote Strongly Disagree'), (b'vote_neg', b'Vote Disagree'), (b'vote_neutral', b'Vote Neutral'), (b'vote_pos', b'Vote Agree'), (b'vote_vpos', b'Vote Strongly Agree'), (b'favorite', b'Favor a Civi')], max_length=255)),
                ('read', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_modified', models.DateTimeField(auto_now=True, null=True)),
                ('account', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='api.account')),
                ('civi', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='api.civi')),
                ('thread', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='api.thread')),
            ],
        ),
        migrations.AlterField(
            model_name='account',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to=common.utils.PathAndRename(b'/')),
        ),
        migrations.AlterField(
            model_name='account',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to=common.utils.PathAndRename(b'')),
        ),
        migrations.CreateModel(
            name='CiviImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=common.utils.PathAndRename(b''))),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('civi', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='images', to='api.civi')),
            ],
        ),
        migrations.AddField(
            model_name='account',
            name='representatives',
            field=models.ManyToManyField(related_name='account', to='api.Representative'),
        ),
        migrations.CreateModel(
            name='Invitation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invitee_email', models.EmailField(default=None, max_length=254)),
                ('verification_code', models.CharField(max_length=31)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('host_user', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='hosts', to=settings.AUTH_USER_MODEL)),
                ('invitee_user', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='invitees', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='civi',
            name='c_type',
            field=models.CharField(choices=[(b'problem', b'Problem'), (b'cause', b'Cause'), (b'solution', b'Solution'), (b'response', b'Response'), (b'rebuttal', b'Rebuttal')], default=b'problem', max_length=31),
        ),
        migrations.AddField(
            model_name='account',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='account',
            name='profile_image_thumb',
            field=models.ImageField(blank=True, null=True, upload_to=common.utils.PathAndRename(b'')),
        ),
        migrations.AddField(
            model_name='account',
            name='country',
            field=models.CharField(blank=True, default=b'United States', max_length=63),
        ),
        migrations.AlterField(
            model_name='civi',
            name='author',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='civis', to='api.account'),
        ),
        migrations.AddField(
            model_name='civi',
            name='linked_bills',
            field=models.ManyToManyField(related_name='bills', to='api.Bill'),
        ),
    ]
